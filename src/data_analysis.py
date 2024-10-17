import pandas as pd
import numpy as np


def get_data():
    players = pd.read_csv('../basketballPlayoffs/players.csv')
    teams = pd.read_csv('../basketballPlayoffs/teams.csv')
    coaches = pd.read_csv('../basketballPlayoffs/coaches.csv')
    awards_players = pd.read_csv('../basketballPlayoffs/awards_players.csv')
    players_teams = pd.read_csv('../basketballPlayoffs/players_teams.csv')
    teams_post = pd.read_csv('../basketballPlayoffs/teams_post.csv')
    series_post = pd.read_csv('../basketballPlayoffs/series_post.csv')
    return players, teams, coaches, awards_players, players_teams, teams_post, series_post


def organize_data():
    players, teams, coaches, awards_players, players_teams, teams_post, series_post = get_data()
    awards_players = awards_players.drop(columns=['lgID'])
    coaches = coaches.drop(columns=['lgID'])
    coaches = coaches.drop(columns=['stint'])
    # from players_teams drop lgID, stint, dq, PostoRebounds, PostdRebounds, PostfgAttempted, PostfgMade, PostftAttempted, PostftMade, PostthreeAttempted, PostthreeMade, PostDQ
    players_teams = players_teams.drop(columns=['lgID'])
    players_teams = players_teams.drop(columns=['stint'])
    players_teams = players_teams.drop(columns=['dq'])
    players_teams = players_teams.drop(columns=['PostoRebounds'])
    players_teams = players_teams.drop(columns=['PostdRebounds'])
    players_teams = players_teams.drop(columns=['PostfgAttempted'])
    players_teams = players_teams.drop(columns=['PostfgMade'])
    players_teams = players_teams.drop(columns=['PostftAttempted'])
    players_teams = players_teams.drop(columns=['PostftMade'])
    players_teams = players_teams.drop(columns=['PostthreeAttempted'])
    players_teams = players_teams.drop(columns=['PostthreeMade'])
    players_teams = players_teams.drop(columns=['PostDQ'])
    # from players drop college, collegeOther, birthDate,deathDate
    players = players.drop(columns=['college'])
    players = players.drop(columns=['collegeOther'])
    players = players.drop(columns=['birthDate'])
    players = players.drop(columns=['deathDate'])
    # from series_post drop lgIDWinner, lgIDLoser, series
    series_post = series_post.drop(columns=['lgIDWinner'])
    series_post = series_post.drop(columns=['lgIDLoser'])
    series_post = series_post.drop(columns=['series'])
    # from teams_post drop lgID
    teams_post = teams_post.drop(columns=['lgID'])    
    # from teams drop lgID, franchID, confID, divID, name,min, attend, arena
    teams = teams.drop(columns=['lgID'])
    teams = teams.drop(columns=['franchID'])
    teams = teams.drop(columns=['confID'])
    teams = teams.drop(columns=['divID'])
    teams = teams.drop(columns=['name'])
    teams = teams.drop(columns=['min'])
    teams = teams.drop(columns=['attend'])
    teams = teams.drop(columns=['arena'])

    return players, teams, coaches, awards_players, players_teams, teams_post, series_post


