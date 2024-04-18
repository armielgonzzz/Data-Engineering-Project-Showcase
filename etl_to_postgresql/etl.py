import psycopg2
import pandas as pd
from sql_queries import *

def connect_to_postgres() -> tuple[psycopg2.extensions.cursor, psycopg2.extensions.connection]:
    '''
    Connecting to PostgreSQL database and returning the reference for
    cursor and connection.
    '''

    # assigning 'db' as connection to PostgreSQL
    db = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
        database='march_madness'
    )
    
    # assigning 'cur' as cursor
    cur = db.cursor()
    
    return cur, db

def create_team_info(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function will modify 'march_madness.csv' to a 
    dataframe with selected rows and columns for 'team_info' table in PostgreSQL.
    '''

    # filtering the columns and rows of dataframe needed for team_info table
    team_info_columns = ['Team Name', 'Conference', 'Seed', 'Region', 'Net Rating', 'Post-Season Tournament']
    team_info = df[team_info_columns]
    team_info = team_info.loc[team_info['Post-Season Tournament'] == 'March Madness', :]
    
    return team_info

def create_offensive_stats(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function will modify 'march_madness.csv' to a 
    dataframe with selected rows and columns for 'team_offensive_stats' table in PostgreSQL.
    '''

    # filtering the columns and rows of dataframe needed for team_offensive_stats table
    offensive_stats = ['Team Name', 'Post-Season Tournament'] + [col for col in df.columns if col.startswith('Off')]
    offensive_stats = df[offensive_stats].drop(columns=['Off.OR %', 'Off.OR % Rank'])
    offensive_stats = offensive_stats.loc[offensive_stats['Post-Season Tournament'] == 'March Madness', :]
    
    return offensive_stats

def create_defensive_stats(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function will modify 'march_madness.csv' to a 
    dataframe with selected rows and columns for 'team_defensive_stats' table in PostgreSQL.
    '''

    # filtering the columns and rows of dataframe needed for team_defensive_stats table
    defensive_stats = ['Team Name', 'Post-Season Tournament'] + [col for col in df.columns if col.startswith('Def')]
    defensive_stats = df[defensive_stats].drop(columns=['Def.OR %', 'Def.OR % Rank'])
    defensive_stats = defensive_stats.loc[defensive_stats['Post-Season Tournament'] == 'March Madness', :]

    return defensive_stats


def insert_to_database(db, cur, team_info, offensive_stats, defensive_stats) -> None:
    '''
    This driver function will load all of the dataframes that we have modified
    into PostgreSQL database using Psycopg2 Module.
    
    db: database connection reference
    cur: database cursor
    team_info: dataframe for team_info table
    offensive_stats: dataframe for team_offensive_stats table
    defensive_stats: dataframe for team_defensive_stats table
    '''

    try:

        # load team_info values into database
        team_info_values = [list(row) for row in team_info.values]
        cur.executemany(insert_team_info, team_info_values)
        db.commit()
        print("Succesfully loaded values to 'team_info' table.")
        
        
        # load offensive_stats values into team_offensive_stats table
        offensive_stats_values = [list(row) for row in offensive_stats.values]
        cur.executemany(insert_team_offensive_stats, offensive_stats_values)
        db.commit()
        print("Succesfully loaded values to 'team_offensive_stats' table.")
        
        
        # load defensive_stats values into team_defensive_stats table
        defensive_stats_values = [list(row) for row in defensive_stats.values]
        cur.executemany(insert_team_defensive_stats, defensive_stats_values)
        db.commit()
        print("Succesfully loaded values to 'team_defensive_stats' table.")
    
    except Exception as e:
        
        # incase of an error, roll back the transaction to undo any changes made before the exception occurred. 
        print('An error occured:', e)
        db.rollback()
        
def main():
    '''
    Main driver that will run all of the functions.
    '''
    
    # connect to PostgreSQL
    cur, db = connect_to_postgres()
    
    # reading the 'march_madness.csv' file and assigning it to 'df'
    df = pd.read_csv('march_madness.csv')
    
    # creating variables for returns of functions
    team_info = create_team_info(df)
    offensive_stats = create_offensive_stats(df)
    defensive_stats = create_defensive_stats(df)
    
    # loading the dataframes into PostgreSQL
    insert_to_database(db, cur, team_info, offensive_stats, defensive_stats)
    
    # closing cursor and database
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
    print('Finished loading all dataframes.')