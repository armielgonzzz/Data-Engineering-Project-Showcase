import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    '''
    This function will connect to the local database (PostgreSQL)
    and will return the connection and cursor.
    
    return: returns (cur, db), a cursor and connection reference
    cur: cursor of PostgreSQL
    db: connection of PostgreSQL
    '''
    
    # connect first to default database 'postgres'
    db = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
        database='postgres'
    )
    
    # set database autocommit to true and set the cursor
    db.set_session(autocommit=True)
    cur = db.cursor()
        
    # create march_madness database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS march_madness")
    cur.execute("CREATE DATABASE march_madness WITH ENCODING 'utf8'")
    
    # close connection to default database
    db.close()
    
    # connect to 'march_madness' database
    db = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
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
    
    # connect to PostgreSQL and get reference for cursor and database
    cur, db = create_database()
    
    # drop all tables if exists
    drop_tables(cur, db)
    print("Successfully DROPPED tables.")
    
    # create all tables
    create_tables(cur, db)
    print("Successfully CREATED tables.")
    
    # close cursor and database
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
    print("Finished creating tables.")
    