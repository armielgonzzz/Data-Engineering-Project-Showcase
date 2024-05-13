# API Data to MySQL Data Pipeline

## **Overview**

In this project, we are to extract data of all the Dota 2 Heroes from a public API. This data will then get transformed after going though the data pipeline. At the last step, it will be loaded into the local MySQL Database.

## Schema

**hero_info** - This table contains information and attributes of each of the heroes from Dota 2.

```
id, hero_name, primary_attribute, attack_type
```

## Project Files

```sql_queries.py``` -> Contains sql queries for dropping and creating tables. Also, contains insertion query template.

```access_api.py``` -> Contains custom function that will extract the JSON Data from the public API.

```config_info.py``` -> This script will parse the .config file to get the sensitive informations that will be used to access the database and the public API.

```main.py``` -> Main driver script that will run the data pipeline.

## Environment 
Python 3.8 or above

MySQL 8.0.36

MySQL Connector - MySQL database adapter for Python


## How to run

Run the drive program ```main.py``` as below:
```
python main.py
``` 


#### Reference: 
[MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)

[MySQL Documentation](https://dev.mysql.com/doc/)

[Python Requests Documentation](https://requests.readthedocs.io/en/latest/)
