# API to Azure Blob Storage Data Pipeline

## **Overview**

In this project, we will apply data modelling to the data that is extracted from a public API of NBA Games. This data will be then transformed by the ETL pipeline and then uploaded to a Azure Blob Storage container. The file that is uploaded contains all of the games that we're played today in CSV format.

## Schema

**gameday_date_games** - This table contains home and away teams score and teams that are playing on the gameday date.

```
home_team, home_team_score, visitor_team, visitor_team_score, period
```

## Project Files

```data``` -> Contains sample data that was extracted and transformed by the pipeline. This data will be uploaded to Azure Blob Container.

```etl``` -> This directory contains both Azure and Public API ETls.

```pipeline``` -> This directory contains driver scripts that will run the ETLs.

```info_config.py``` -> This script will parse the config.cfg file to get the sensitive informations that will be used to access the database, public API and Azure Blob Storage connection string.

```azure_blob_etl.py``` -> Contains functions that will connect to Azure Blob Container and create a blob that will be uploaded to the container.

```nba_games_etl.py``` -> This script will connect to the Public API and extract the data. This also contains all of the transformation that will be done to the data and save it to the local directory.

```nba_games_pipeline.py``` -> A pipeline script that will run the Public to Local Directory ETL.

```upload_to_blob_pipeline.py``` -> This pipeline script will get the transformed data from the local directory and create a blob off of it to be uploaded in Azure Blob Storage.

```main.py``` -> Main driver script that will run all of the data pipelines.

## Environment 
Python 3.8 or above

Microsoft Azure

Azure Blob Storage


## How to run

Run the drive program ```main.py``` as below:
```
python main.py
``` 

#### Reference: 
[Python Requests Documentation](https://requests.readthedocs.io/en/latest/)

[Azure Storage SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/storage?view=azure-python)

