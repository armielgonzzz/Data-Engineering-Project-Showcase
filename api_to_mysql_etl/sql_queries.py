'''
This module contains all of the queries we will execute in psycopg2
to create tables, modify and load the data we extracted from the API to
PostgreSQL.

>>> create_hero_info_table
>>> insert_hero_info
>>> drop_hero_info_table 
'''

# create table query
create_hero_info_table = """
    CREATE TABLE IF NOT EXISTS hero_info (
        id INT NOT NULL,
        hero_name VARCHAR(50) NOT NULL PRIMARY KEY,
        primary_attribute VARCHAR(5) NOT NULL,
        attack_type VARCHAR(10) NOT NULL
    )
"""

# drop table query
drop_hero_info_table = """
    DROP TABLE IF EXISTS hero_info
"""

# insert value query
insert_hero_info = """
    INSERT INTO hero_info VALUES (%s, %s, %s, %s)
"""