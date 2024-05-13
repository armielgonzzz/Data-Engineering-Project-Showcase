import mysql.connector
from sql_queries import create_hero_info_table, drop_hero_info_table, insert_hero_info
from access_api import get_request
from config_info import host, user, password, database, url


def connect_to_database(host: str, user: str, password: str, database: str):
    '''
    Connects to the dota_heroes database and returns reference to
    database and cursor.
    
    return -> db, cur
    db: reference for database connection
    cur: reference for database cursor
    '''
    try:
        # connect to database
        db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        
        # cursor reference
        cur = db.cursor()

        return db, cur
    
    except Exception as e:
        print(f'Error upon creating connection: {e}')
        return None
        


def drop_create_table(db, cur) -> None:
    '''
    DROP then CREATE table inside the database
    
    db: reference for database connection
    cur: reference of database cursor
    '''
    
    # drop and create table
    cur.execute(drop_hero_info_table)
    cur.execute(create_hero_info_table)
    db.commit()
    
    
def modify_data(hero_info: dict) -> tuple:
    '''
    Transforms data retrieved from API to satisfy the table in database    
    
    hero_info: JSON Data from the public API
    '''
    
    # Extract values from the dict
    id = hero_info['id']
    hero_name = hero_info['localized_name']
    primary_attribute = hero_info['primary_attr']
    attack_type = hero_info['attack_type']
    
    return id, hero_name, primary_attribute, attack_type


def load_data(db, cur, data, func) -> None:
    '''
    Loads the passed the parsed data to PostgreSQL database.
    Modification will be done first by using the function parameter
    before loading it to database.
    
    db: reference for database connection
    cur: reference of database cursor
    data: parsed data from json file retrieved from API
    func: helper function that will modify the data from API 
    '''
    
    # run the function to modify the data
    modified_data = func(data)
    
    # load the modifed data to database
    cur.execute(insert_hero_info, modified_data)
    db.commit()


def main() -> None:
    '''
    Main driver function that will extract data from API, modify the data
    and load it to PostgreSQL.    
    '''

    # input the information from config into to 'connect_to_database' function
    db, cur = connect_to_database(host, user, password, database)
    
    # DROP, then CREATE table inside the database
    drop_create_table(db, cur)
        
    # retrieve data from the API
    response = get_request(url)
        
    try:
        # iterate through the list of json file retrieved from the API
        for data in response:

            # load data to PostgreSQL
            load_data(db, cur, data, modify_data)

        print('Loading data to database successful!')
    
    except Exception as e:
        print('An error occured while loading the data to database:', e)
        
        # rollback the database in case of error
        db.rollback()    

    finally:
        # close the cursor and database connection
        cur.close()
        db.close()


if __name__ == "__main__":
    main()