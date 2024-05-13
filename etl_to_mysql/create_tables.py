import mysql.connector
from sql_queries import create_table_queries, drop_table_queries
from config_info import host, user, password


def create_database():
    '''
    This function will connect to the local database (MySQL)
    and will return the connection and cursor.
    
    return: returns (cur, db), a cursor and connection reference
    cur: cursor of MySQL
    db: connection of MySQL
    '''
    
    # connect first to default database 'postgres'
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database='sys'
    )
    
    cur = db.cursor()
        
    # create march_madness database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS march_madness")
    cur.execute("CREATE DATABASE march_madness")
    
    # close connection to default database
    db.close()
    
    # connect to 'march_madness' database
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database='march_madness'
    )
    
    # assign new cursor
    cur = db.cursor()

    return cur, db

def drop_tables(cur, db) -> None:
    '''
    This function will run all DROP queries in sql_queries.py to clean the database.
    
    cur: cursor of database
    db: connection reference of database
    '''
    
    # execute every query in drop_table_queries
    for query in drop_table_queries:
        cur.execute(query)
        db.commit()

def create_tables(cur, db) -> None:
    '''
    This function will run all CREATE queries in sql_queries.py to create the database tables.
    
    cur: cursor of database
    db: connection reference of database
    '''
    
    # execute every query in create_table_queries
    for query in create_table_queries:
        cur.execute(query)
        db.commit()

def main():
    '''
    This is a driver function that will drop and create tables.
    '''
    try:
        # connect to MySQL and get reference for cursor and database
        cur, db = create_database()
        print("Successfully CREATED database.")
        
        # drop all tables if exists
        drop_tables(cur, db)
        print("Successfully DROPPED tables.")
        
        # create all tables
        create_tables(cur, db)
        print("Successfully CREATED tables.")

    except Exception as e:
        print(f'Error while interacting with MySQL Database: {e}')    
    
    finally:
        # close cursor and database
        cur.close()
        db.close()

if __name__ == "__main__":
    main()
    print("Finished creating tables.")
    