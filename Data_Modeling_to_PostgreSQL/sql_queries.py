# create table queries

team_info_table = ("""
    CREATE TABLE IF NOT EXISTS team_info (
        team_name VARCHAR(255) NOT NULL PRIMARY KEY,
        conference VARCHAR(255) NOT NULL,
        seed INT NOT NULL,
        region VARCHAR(255) NOT NULL,
        net_rating FLOAT NOT NULL,
        post_season_tournament VARCHAR(255) NOT NULL
    )""")

team_offensive_stats_table = ("""
    CREATE TABLE team_offensive_stats (
        team_name VARCHAR(255) NOT NULL,
        post_season_tournament VARCHAR(255) NOT NULL,
        field_goal_percentage FLOAT NOT NULL,
        field_goal_percentage_rank INT NOT NULL,
        turnover_percentage FLOAT NOT NULL,
        turnover_percentage_rank INT NOT NULL,
        free_throw_rate FLOAT NOT NULL,
        free_throw_rate_rank INT NOT NULL,
        free_throw_attempts FLOAT NOT NULL,
        free_throw_attempts_rank INT NOT NULL,
        two_points_field_goals FLOAT NOT NULL,
        two_points_field_goals_rank INT NOT NULL,
        three_points_field_goals FLOAT NOT NULL,
        three_points_field_goals_rank INT NOT NULL,
        FOREIGN KEY (team_name) REFERENCES team_info(team_name)
    )""")

team_defensive_stats_table = ("""
    CREATE TABLE team_defensive_stats (
        team_name VARCHAR(255) NOT NULL,
        post_season_tournament VARCHAR(255) NOT NULL,
        field_goal_percentage FLOAT NOT NULL,
        field_goal_percentage_rank INT NOT NULL,
        turnover_percentage FLOAT NOT NULL,
        turnover_percentage_rank INT NOT NULL,
        free_throw_rate FLOAT NOT NULL,
        free_throw_rate_rank INT NOT NULL,
        free_throw_attempts FLOAT NOT NULL,
        free_throw_attempts_rank INT NOT NULL,
        two_points_field_goals FLOAT NOT NULL,
        two_points_field_goals_rank INT NOT NULL,
        three_points_field_goals FLOAT NOT NULL,
        three_points_field_goals_rank INT NOT NULL,
        FOREIGN KEY (team_name) REFERENCES team_info(team_name)
    )""")


# drop table queries
drop_team_info = "DROP TABLE IF EXISTS team_info"
drop_team_offensive_stats = "DROP TABLE IF EXISTS team_offensive_stats"
drop_team_defensive_stats = "DROP TABLE IF EXISTS team_defensive_stats"

# insert values queries
insert_team_info = "INSERT INTO team_info VALUES (%s, %s, %s, %s, %s, %s);"
insert_team_offensive_stats = "INSERT INTO team_offensive_stats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
insert_team_defensive_stats = "INSERT INTO team_defensive_stats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# query list
create_table_queries = [team_info_table, team_offensive_stats_table, team_defensive_stats_table]
drop_table_queries = [drop_team_info, drop_team_offensive_stats, drop_team_defensive_stats]