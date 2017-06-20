from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Team, Player, User

engine = create_engine('sqlite:///nbaplayers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Admin", email="admin@gmail.com",
             picture='/static/nba_logo.png')
session.add(User1)
session.commit()

# Players for Atlanta Hawks
team1 = Team(user_id=1, name="Atlanta Hawks")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Dwight Howard", height_feet="6", height_inches="11", weight="265",
                     age="31", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Paul Millsap", height_feet="6", height_inches="8", weight="246",
                     age="32", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Taurean Prince", height_feet="6", height_inches="8", weight="220",
                     age="23", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Dennis Schroder", height_feet="6", height_inches="1", weight="172",
                     age="23", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Tim Hardaway Jr.", height_feet="6", height_inches="6", weight="205",
                     age="25", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Boston Celtics
team1 = Team(user_id=1, name="Boston Celtics")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Al Horford", height_feet="6", height_inches="10", weight="245",
                     age="30", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Amir Johnson", height_feet="6", height_inches="9", weight="249",
                     age="30", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Jae Crowder", height_feet="6", height_inches="6", weight="235",
                     age="26", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Isaiah Thomas", height_feet="5", height_inches="9", weight="185",
                     age="28", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Avery Bradley", height_feet="6", height_inches="2", weight="180",
                     age="26", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Brooklyn Nets
team1 = Team(user_id=1, name="Brooklyn Nets")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Brook Lopez", height_feet="7", height_inches="0", weight="268",
                     age="29", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Rondae Hollis-Jefferson", height_feet="6", height_inches="7", weight="214",
                     age="22", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Caris LeVert", height_feet="6", height_inches="7", weight="203",
                     age="22", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Jeremy Lin", height_feet="6", height_inches="3", weight="200",
                     age="28", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Randy Foye", height_feet="6", height_inches="4", weight="213",
                     age="33", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for New York Knicks
team1 = Team(user_id=1, name="New York Knicks")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Joakim Noah", height_feet="6", height_inches="11", weight="230",
                     age="32", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Kristaps Porzingis", height_feet="7", height_inches="3", weight="240",
                     age="21", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Carmelo Anthony", height_feet="6", height_inches="8", weight="240",
                     age="32", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Derrick Rose", height_feet="6", height_inches="3", weight="190",
                     age="28", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Courtney Lee", height_feet="6", height_inches="5", weight="200",
                     age="31", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Philadelphia 76ers
team1 = Team(user_id=1, name="Philadelphia 76ers")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Joel Embiid", height_feet="7", height_inches="0", weight="250",
                     age="23", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Dario Saric", height_feet="6", height_inches="10", weight="245",
                     age="23", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Robert Covington", height_feet="6", height_inches="9", weight="225",
                     age="26", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Ben Simmons", height_feet="6", height_inches="10", weight="240",
                     age="20", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Timothe Luwawu-Cabarrot", height_feet="6", height_inches="6", weight="205",
                     age="22", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Toronto Raptors
team1 = Team(user_id=1, name="Toronto Raptors")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Serge Ibaka", height_feet="6", height_inches="10", weight="235",
                     age="27", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Patrick Patterson", height_feet="6", height_inches="9", weight="230",
                     age="28", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Norman Powell", height_feet="6", height_inches="4", weight="215",
                     age="23", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Kyle Lowry", height_feet="6", height_inches="1", weight="196",
                     age="31", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="DeMar DeRozan", height_feet="6", height_inches="7", weight="219",
                     age="27", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Charlotte Hornets
team1 = Team(user_id=1, name="Charlotte Hornets")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Cody Zeller", height_feet="7", height_inches="0", weight="240",
                     age="24", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Marvin Williams", height_feet="6", height_inches="9", weight="237",
                     age="30", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Michael Kidd-Gilchrist", height_feet="6", height_inches="7", weight="232",
                     age="23", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Kemba Walker", height_feet="6", height_inches="1", weight="184",
                     age="27", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Nicolas Batum", height_feet="6", height_inches="8", weight="200",
                     age="28", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Miami Heat
team1 = Team(user_id=1, name="Miami Heat")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Hassan Whiteside", height_feet="7", height_inches="0", weight="265",
                     age="27", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Luke Babbitt", height_feet="6", height_inches="9", weight="225",
                     age="27", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Justise Winslow", height_feet="6", height_inches="7", weight="225",
                     age="21", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Goran Dragic", height_feet="6", height_inches="3", weight="190",
                     age="31", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Dion Waiters", height_feet="6", height_inches="4", weight="215",
                     age="25", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Orlando Magic
team1 = Team(user_id=1, name="Orlando Magic")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Nikola Vucevic", height_feet="7", height_inches="0", weight="260",
                     age="26", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Aaron Gordon", height_feet="6", height_inches="9", weight="220",
                     age="21", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Terrence Ross", height_feet="6", height_inches="7", weight="206",
                     age="26", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Elfrid Payton", height_feet="6", height_inches="4", weight="185",
                     age="23", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Evan Fournier", height_feet="6", height_inches="7", weight="205",
                     age="24", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Chicago Bulls
team1 = Team(user_id=1, name="Chicago Bulls")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Robin Lopez", height_feet="7", height_inches="0", weight="265",
                     age="29", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Nikola Mirotic", height_feet="6", height_inches="10", weight="240",
                     age="26", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Jimmy Butler", height_feet="6", height_inches="7", weight="231",
                     age="27", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Rajon Rondo", height_feet="6", height_inches="1", weight="186",
                     age="31", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Dwyane Wade", height_feet="6", height_inches="4", weight="220",
                     age="35", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Cleveland Cavaliers
team1 = Team(user_id=1, name="Cleveland Cavaliers")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Tristan Thompson", height_feet="6", height_inches="10", weight="238",
                     age="26", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Kevin Love", height_feet="6", height_inches="10", weight="251",
                     age="28", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="LeBron James", height_feet="6", height_inches="8", weight="250",
                     age="32", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Kyrie Irving", height_feet="6", height_inches="3", weight="193",
                     age="25", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="J.R. Smith", height_feet="6", height_inches="6", weight="225",
                     age="31", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Detroit Pistons
team1 = Team(user_id=1, name="Detroit Pistons")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Andre Drummond", height_feet="6", height_inches="11", weight="279",
                     age="23", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Jon Leuer", height_feet="6", height_inches="10", weight="228",
                     age="28", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Marcus Morris", height_feet="6", height_inches="9", weight="235",
                     age="27", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Reggie Jackson", height_feet="6", height_inches="3", weight="208",
                     age="27", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Kentavious Caldwell-Pope", height_feet="6", height_inches="5", weight="205",
                     age="24", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Indiana Pacers
team1 = Team(user_id=1, name="Indiana Pacers")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Myles Turner", height_feet="6", height_inches="11", weight="243",
                     age="21", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Thaddeus Young", height_feet="6", height_inches="8", weight="221",
                     age="28", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Paul George", height_feet="6", height_inches="9", weight="220",
                     age="27", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Jeff Teague", height_feet="6", height_inches="2", weight="186",
                     age="28", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="C.J. Miles", height_feet="6", height_inches="6", weight="225",
                     age="30", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Milwaukee Bucks
team1 = Team(user_id=1, name="Milwaukee Bucks")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Thon Maker", height_feet="7", height_inches="1", weight="216",
                     age="20", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Giannis Antetokounmpo", height_feet="6", height_inches="11", weight="222",
                     age="22", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Khris Middleton", height_feet="6", height_inches="8", weight="234",
                     age="25", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="Malcolm Brogdon", height_feet="6", height_inches="5", weight="215",
                     age="24", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Tony Snell", height_feet="6", height_inches="7", weight="225",
                     age="25", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

# Players for Washington Wizards
team1 = Team(user_id=1, name="Washington Wizards")
session.add(team1)
session.commit()

player1 = Player(user_id=1, name="Marcin Gortat", height_feet="6", height_inches="11", weight="240",
                     age="33", position="Center", team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Markieff Morris", height_feet="6", height_inches="10", weight="245",
                     age="27", position="Power Forward", team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1, name="Otto Porter", height_feet="6", height_inches="8", weight="205",
                     age="23", position="Small Forward", team=team1)
session.add(player3)
session.commit()

player4 = Player(user_id=1, name="John Wall", height_feet="6", height_inches="4", weight="210",
                     age="26", position="Point Guard", team=team1)
session.add(player4)
session.commit()

player5 = Player(user_id=1, name="Bradley Beal", height_feet="6", height_inches="5", weight="207",
                     age="23", position="Shooting Guard", team=team1)
session.add(player5)
session.commit()

print "Teams and players created!"
