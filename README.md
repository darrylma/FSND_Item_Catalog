Contents
-------------------------------------
1. main.py - defines all functions and contains all routing information
2. database_setup.py - creates database
3. populate_database.py - populates database with team and player information
2. templates folder - contains all html code
3. static folder - contains all styling code (main.css, bootstrap, fonts)


Quick Start
-------------------------------------
Running on localhost
1. Ensure you have internet connection
2. Open up Gitbash
3. Navigate to location of vagrant file (Assumes virtualBox and Vagrant has been installed)
4. Type "vagrant up"
5. Type "vagrant ssh"
6. Type "cd /vagrant"
7. Navigate to location of nba_database folder where main.py is located
8. Type "python database_setup.py" to create database
9. Type "python populate_database.py" to populate database with values
10. Type "python main.py"
11. Open up Google Chrome and type in "localhost:8000/team/" in browser address bar
12. Click on "Click Here to Login" to login and start adding, updating and deleting teams and players into database
