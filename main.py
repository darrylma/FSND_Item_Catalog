from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash
from functools import wraps
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "NBA Starting Lineups Application"

#### Connect to Database and create database session ####
engine = create_engine('sqlite:///nbaplayers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#### Helper Functions ####
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

#### JSON APIs to view team and player information ####
@app.route('/team/<int:team_id>/player/JSON')
def teamPlayerJSON(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(Player).filter_by(
        team_id=team_id).all()
    return jsonify(players=[p.serialize for p in players])

@app.route('/team/<int:team_id>/player/<int:player_id>/JSON')
def playerJSON(team_id, player_id):
    player = session.query(Player).filter_by(id=player_id).one()
    return jsonify(player=player.serialize)

@app.route('/team/JSON')
def teamsJSON():
    teams = session.query(Team).all()
    return jsonify(teams=[t.serialize for t in teams])

#### Login Functions ####
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
        for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = ('https://graph.facebook.com/v2.8/oauth/access_token?'
           'grant_type=fb_exchange_token&client_id=%s&client_secret=%s'
           '&fb_exchange_token=%s') % (app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    # Extract the access token from response
    token = 'access_token=' + data['access_token']

    # Use token to get user info from API
    url = 'https://graph.facebook.com/v2.8/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout,
    # let's strip out the information before the equals sign in our token
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    print user_id
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h3>Welcome, '
    output += login_session['username']

    output += '!</h3>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 100px; height: 100px;'
    output += 'border-radius: 150px;-webkit-border-radius: 150px;'
    output += '-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output

@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (
        facebook_id,access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    print user_id
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 100px; height: 100px;border-radius: '
    output += '150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showTeamPlayer'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showTeamPlayer'))

#### View, edit, and delete team details ####
# Main screen
@app.route('/')
@app.route('/team/')
def showTeamPlayer():
    teams = session.query(Team).order_by(asc(Team.name))
    players = session.query(Player).order_by(asc(Player.name))
    if 'username' not in login_session:
        return render_template('publicteams.html', teams=teams, players=players)
    else:
        return render_template('teams.html', teams=teams, players=players)

# Create new team. Disallows team from being created if user not logged in
@app.route('/team/new/', methods=['GET', 'POST'])
@login_required
def newTeam():
    if request.method == 'POST':
        newTeam = Team(name=request.form['name'],
            user_id=login_session['user_id'])
        session.add(newTeam)
        flash('The %s has been successfully created' % newTeam.name)
        session.commit()
        return redirect(url_for('showTeamPlayer'))
    else:
        return render_template('newteam.html')

# Edits existing team. Disallows team from being edited if user not
# logged in and not user that created team
@app.route('/team/<int:team_id>/edit/', methods=['GET', 'POST'])
@login_required
def editTeam(team_id):
    editedTeam = session.query(Team).filter_by(id=team_id).one()
    if editedTeam.user_id != login_session['user_id']:
        flash('You are not authorized to edit %s as you are not '
            'the creator' % editedTeam.name)
        return redirect('/team/')
    if request.method == 'POST':
        if request.form['name']:
            editedTeam.name = request.form['name']
            session.add(editedTeam)
            session.commit()
            flash('Successfully edited %s' % editedTeam.name)
            return redirect(url_for('showPlayers', team_id=team_id))
    else:
        return render_template('editteam.html', team=editedTeam)

# Deletes existing team. Disallows team from being deleted if user not
# logged in and not user that created team
@app.route('/team/<int:team_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteTeam(team_id):
    teamToDelete = session.query(Team).filter_by(id=team_id).one()
    playersToDelete = session.query(Player).filter_by(team_id=team_id).all()
    if teamToDelete.user_id != login_session['user_id']:
        flash('You are not authorized to delete %s as you are not '
            'the creator' % teamToDelete.name)
        return redirect('/team/')
    if request.method == 'POST':
        session.delete(teamToDelete)
        # Deletes all associated players in team
        for p in playersToDelete:
            session.delete(p)
        flash('%s and all associated players have been '
            'deleted' % teamToDelete.name)
        session.commit()
        return redirect(url_for('showTeamPlayer'))
    else:
        return render_template('deleteteam.html', team=teamToDelete)

#### View, edit, and delete player details ####
# Displays all players for selected team
@app.route('/team/<int:team_id>/')
def showPlayers(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    teams = session.query(Team).order_by(asc(Team.name))
    players = session.query(Player).filter_by(
        team_id=team_id).order_by(asc(Player.position)).all()
    creator = getUserInfo(team.user_id)
    if 'username' not in login_session:
        return render_template('publicteamplayers.html', team=team,
            teams=teams, players=players, creator=creator)
    elif creator.id != login_session['user_id']:
        return render_template('publicteamplayerswithaddteam.html',
            team=team, teams=teams, players=players, creator=creator)
    else:
        return render_template('teamplayers.html', team=team,
            teams=teams, players=players, creator=creator)

# Displays single player's details
@app.route('/player/<int:player_id>')
def showPlayer(player_id):
    player = session.query(Player).filter_by(id=player_id).one()
    creator = getUserInfo(player.user_id)
    if ('username' not in login_session) or (
        creator.id != login_session['user_id']):
        return render_template('publicplayer.html', player=player)
    else:
        return render_template('player.html', player=player)

# Create new player. Disallows player from being created
# if user not logged in and not user that created team
@app.route('/team/<int:team_id>/player/new/', methods=['GET', 'POST'])
@login_required
def newPlayer(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    if login_session['user_id'] != team.user_id:
        flash('You are not authorized to add players to the %s as you '
            'are not the creator' % team.name)
        return redirect('/team/')
    if request.method == 'POST':
        newPlayer = Player(name=request.form['name'],
            height_feet=request.form['height_feet'],
            height_inches=request.form['height_inches'],
            weight=request.form['weight'],
            age=request.form['age'],
            position=request.form['position'],
            team_id=team_id,
            user_id=team.user_id)
        session.add(newPlayer)
        session.commit()
        flash('%s added to the %s' % (newPlayer.name, newPlayer.team.name))
        return redirect(url_for('showPlayers', team_id=team_id))
    else:
        return render_template('newplayer.html', team_id=team_id)

# Edits existing player. Disallows player from being edited if
# user not logged in and not user that created team
@app.route('/team/<int:team_id>/player/<int:player_id>/edit',
    methods=['GET', 'POST'])
@login_required
def editPlayer(team_id, player_id):
    editedPlayer = session.query(Player).filter_by(id=player_id).one()
    team = session.query(Team).filter_by(id=team_id).one()
    if login_session['user_id'] != editedPlayer.user_id:
        flash('You are not authorized to edit %s as you are '
            'not the creator' % editedPlayer.name)
        return redirect('/team/%s' % team_id)
    if request.method == 'POST':
        if request.form['name']:
            editedPlayer.name = request.form['name']
        if request.form['height_feet']:
            editedPlayer.height_feet = request.form['height_feet']
        if request.form['height_inches']:
            editedPlayer.height_inches = request.form['height_inches']
        if request.form['weight']:
            editedPlayer.weight = request.form['weight']
        if request.form['age']:
            editedPlayer.age = request.form['age']
        if request.form['position']:
            editedPlayer.position = request.form['position']
        session.add(editedPlayer)
        session.commit()
        flash('%s successfully edited' % editedPlayer.name)
        return redirect(url_for('showPlayers', team_id=team_id))
    else:
        return render_template('editplayer.html', team_id=team_id,
            player_id=player_id, player=editedPlayer)

# Deletes existing player. Disallows player from being deleted if
# user not logged in and not user that created team
@app.route('/team/<int:team_id>/player/<int:player_id>/delete',
    methods=['GET', 'POST'])
@login_required
def deletePlayer(team_id, player_id):
    team = session.query(Team).filter_by(id=team_id).one()
    playerToDelete = session.query(Player).filter_by(id=player_id).one()
    if login_session['user_id'] != playerToDelete.user_id:
        flash('You are not authorized to delete %s as you are '
            'not the creator' % playerToDelete.name)
        return redirect('/team/')
    if request.method == 'POST':
        session.delete(playerToDelete)
        session.commit()
        flash('%s successfully deleted' % playerToDelete.name)
        return redirect(url_for('showPlayers', team_id=team_id))
    else:
        return render_template('deleteplayer.html', player=playerToDelete)

#### Main configuration ####
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
