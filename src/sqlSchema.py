import sqlite3

con = sqlite3.connect("database.db")

con.execute("DROP TABLE IF EXISTS Awards")
con.execute("DROP TABLE IF EXISTS Coaches")
con.execute("DROP TABLE IF EXISTS Players")
con.execute("DROP TABLE IF EXISTS Teams")
con.execute("DROP TABLE IF EXISTS TeamPlayers")
con.execute("DROP TABLE IF EXISTS Teams")
con.execute("DROP TABLE IF EXISTS TeamsPost")
con.execute("DROP TABLE IF EXISTS SeriesPost")


# Create the awards_players table
con.execute("""
CREATE TABLE IF NOT EXISTS awards_players (
    awardID INTEGER PRIMARY KEY AUTOINCREMENT,
    playerID INTEGER NOT NULL,
    award TEXT NOT NULL,
    year INTEGER NOT NULL,
    FOREIGN KEY (playerID) REFERENCES players(playerID)
)
""")

# Create the coaches table
con.execute("""
CREATE TABLE IF NOT EXISTS coaches (
    coachID INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    tmID INTEGER NOT NULL,
    won INTEGER NOT NULL,
    lost INTEGER NOT NULL,
    post_wins INTEGER NOT NULL,
    post_losses INTEGER NOT NULL,
    FOREIGN KEY (tmID) REFERENCES teams(tmID)
)
""")

# Create the players table
con.execute("""
CREATE TABLE IF NOT EXISTS players (
    playerID INTEGER PRIMARY KEY AUTOINCREMENT,
    pos TEXT NOT NULL,
    firstseason INTEGER NOT NULL,
    lastseason INTEGER NOT NULL,
    height TEXT NOT NULL,
    weight INTEGER NOT NULL
)
""")

# Create the players_teams table
con.execute("""
CREATE TABLE IF NOT EXISTS players_teams (
    playersTeamID INTEGER PRIMARY KEY AUTOINCREMENT,
    playerID INTEGER NOT NULL,
    year INTEGER NOT NULL,
    tmID INTEGER NOT NULL,
    GP INTEGER NOT NULL,
    GS INTEGER NOT NULL,
    minutes INTEGER NOT NULL,
    points INTEGER NOT NULL,
    oRebounds INTEGER NOT NULL,
    dRebounds INTEGER NOT NULL,
    rebounds INTEGER NOT NULL,
    assists INTEGER NOT NULL,
    steals INTEGER NOT NULL,
    blocks INTEGER NOT NULL,
    turnovers INTEGER NOT NULL,
    PF INTEGER NOT NULL,
    fgAttempted INTEGER NOT NULL,
    fgMade INTEGER NOT NULL,
    ftAttempted INTEGER NOT NULL,
    ftMade INTEGER NOT NULL,
    threeAttempted INTEGER NOT NULL,
    threeMade INTEGER NOT NULL,
    PostGP INTEGER NOT NULL,
    PostGS INTEGER NOT NULL,
    PostMinutes INTEGER NOT NULL,
    PostPoints INTEGER NOT NULL,
    PostRebounds INTEGER NOT NULL,
    PostAssists INTEGER NOT NULL,
    PostSteals INTEGER NOT NULL,
    PostBlocks INTEGER NOT NULL,
    PostTurnovers INTEGER NOT NULL,
    PostPF INTEGER NOT NULL,
    FOREIGN KEY (playerID) REFERENCES players(playerID),
    FOREIGN KEY (tmID) REFERENCES teams(tmID)
)
""")

# Create the series_post table
con.execute("""
CREATE TABLE IF NOT EXISTS series_post (
    seriesID INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    round INTEGER NOT NULL,
    tmIDWinner INTEGER NOT NULL,
    tmIDLoser INTEGER NOT NULL,
    W INTEGER NOT NULL,
    L INTEGER NOT NULL
)
""")

# Create the teams table
con.execute("""
CREATE TABLE IF NOT EXISTS teams (
    year INTEGER NOT NULL,
    tmID INTEGER PRIMARY KEY AUTOINCREMENT,
    rank INTEGER NOT NULL,
    playoff INTEGER NOT NULL,
    seeded INTEGER NOT NULL,
    firstRound INTEGER NOT NULL,
    semis INTEGER NOT NULL,
    finals INTEGER NOT NULL,
    o_fgm INTEGER NOT NULL,
    o_fga INTEGER NOT NULL,
    o_ftm INTEGER NOT NULL,
    o_fta INTEGER NOT NULL,
    o_3pm INTEGER NOT NULL,
    o_3pa INTEGER NOT NULL,
    o_oreb INTEGER NOT NULL,
    o_dreb INTEGER NOT NULL,
    o_reb INTEGER NOT NULL,
    o_asts INTEGER NOT NULL,
    o_pf INTEGER NOT NULL,
    o_stl INTEGER NOT NULL,
    o_to INTEGER NOT NULL,
    o_blk INTEGER NOT NULL,
    o_pts INTEGER NOT NULL,
    d_fgm INTEGER NOT NULL,
    d_fga INTEGER NOT NULL,
    d_ftm INTEGER NOT NULL,
    d_fta INTEGER NOT NULL,
    d_3pm INTEGER NOT NULL,
    d_3pa INTEGER NOT NULL,
    d_oreb INTEGER NOT NULL,
    d_dreb INTEGER NOT NULL,
    d_reb INTEGER NOT NULL,
    d_asts INTEGER NOT NULL,
    d_pf INTEGER NOT NULL,
    d_stl INTEGER NOT NULL,
    d_to INTEGER NOT NULL,
    d_blk INTEGER NOT NULL,
    d_pts INTEGER NOT NULL,
    tmORB INTEGER NOT NULL,
    tmDRB INTEGER NOT NULL,
    tmTRB INTEGER NOT NULL,
    opptmORB INTEGER NOT NULL,
    opptmDRB INTEGER NOT NULL,
    opptmTRB INTEGER NOT NULL,
    won INTEGER NOT NULL,
    lost INTEGER NOT NULL,
    GP INTEGER NOT NULL,
    homeW INTEGER NOT NULL,
    homeL INTEGER NOT NULL,
    awayW INTEGER NOT NULL,
    awayL INTEGER NOT NULL,
    confW INTEGER NOT NULL,
    confL INTEGER NOT NULL,
    FOREIGN KEY (tmID) REFERENCES teams(tmID)
)
""")

# Create the teams_post table
con.execute("""
CREATE TABLE IF NOT EXISTS teams_post (
    year INTEGER NOT NULL,
    tmID INTEGER NOT NULL,
    W INTEGER NOT NULL,
    L INTEGER NOT NULL,
    PRIMARY KEY (year, tmID),
    FOREIGN KEY (tmID) REFERENCES teams(tmID)
)
""")
