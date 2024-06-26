# ETL Pipeline with Pandas and MySQL

![Project Visualization](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/blob/main/etl_to_mysql/etl_to_mysql.gif)

## **Overview**

In this project, we apply Data modelling with MySQL and build an ETL pipeline using Python. We're give a dataset of the stats of all the teams participating in USA NCAA. We are to build a pipeline that will transform the dataset leaving only the teams that are competing in this year's March Madness. After transforming the dataset, this will be inserted in our database in MySQL.


## Schema

**team_info_table** - This table contains vital information about the teams.

```
team_name, conference, seed, region, net_rating, post_season_tournament
```

**team_offensive_stats_table** - Contains all of the offensive stats per team. Column `team_name` references to `team_name` in team_info_table.
```
team_name, post_season_tournament, field_goal_percentage, field_goal_percentage_rank, turnover_percentage, turnover_percentage_rank, free_throw_rate, free_throw_rate_rank, free_throw_attempts, free_throw_attempts_rank, two_points_field_goals, two_points_field_goals_rank, three_points_field_goals, three_points_field_goals_rank
```
**team_defensive_stats_table** - Contains all of the defensive stats per team. Column `team_name` references to `team_name` in team_info_table.
```
team_name, post_season_tournament, field_goal_percentage, field_goal_percentage_rank, turnover_percentage, turnover_percentage_rank, free_throw_rate, free_throw_rate_rank, free_throw_attempts, free_throw_attempts_rank, two_points_field_goals, two_points_field_goals_rank, three_points_field_goals, three_points_field_goals_rank
```

## Project Files

```march_madness.csv``` -> Raw dataset of USA NCAA Teams.

```sql_queries.py``` -> Contains sql queries for dropping and creating tables. Also, contains insertion query template.

```create_tables.py``` -> Contains code for setting up database. Running this file creates **march_madness** database and also creates the tables.

```etl.py``` -> A python script that will transform the data and load it into the tables. 

```main.py``` -> Main driver script that will run the data pipeline.


## Environment 
Python 3.8 or above

MySQL 16.2

MySQL Connector - MySQL database adapter for Python


## How to run

Run the drive program ```main.py``` as below:
```
python main.py
``` 

The ```create_tables.py``` and ```etl.py``` file can also be run independently as below:
```
python create_tables.py 
python etl.py 
```


## Reference
[MySQL Connector](https://www.psycopg.org/docs/)

[MySQL Documentation](https://dev.mysql.com/doc/)

[Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
