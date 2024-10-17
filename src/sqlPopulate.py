import sqlite3
import data_analysis
con = sqlite3.connect("database.db")

# add the data from data_analysis.py to the database
players, teams, coaches, awards_players, players_teams, teams_post, series_post = data_analysis.organize_data()
players.to_sql('players', con, if_exists='replace', index=False)
teams.to_sql('teams', con, if_exists='replace', index=False)
coaches.to_sql('coaches', con, if_exists='replace', index=False)
awards_players.to_sql('awards_players', con, if_exists='replace', index=False)
players_teams.to_sql('players_teams', con, if_exists='replace', index=False)
teams_post.to_sql('teams_post', con, if_exists='replace', index=False)
series_post.to_sql('series_post', con, if_exists='replace', index=False)


# PRINT THE DATA
print("PLAYERS")
print(players)
print("\nTEAMS")
print(teams)
print("\nCOACHES")
print(coaches)
print("\nAWARDS PLAYERS")
print(awards_players)
print("\nPLAYERS TEAMS")
print(players_teams)
print("\nTEAMS POST")
print(teams_post)
print("\nSERIES POST")
print(series_post)

