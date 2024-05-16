# Data Engineering Projects

## Project 1: ETL Pipeline with Pandas and MySQL
In this project, we apply Data modelling with MySQL and build an ETL pipeline using Python. We're give a dataset of the stats of all the teams participating in USA NCAA. We are to build a pipeline that will transform the dataset leaving only the teams that are competing in this year's March Madness. After transforming the dataset, this will be inserted in our database in MySQL.

![Project Visualization](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/blob/main/etl_to_mysql/etl_to_mysql.gif)

Link : [ETL_with_Pandas_and_MySQL](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/tree/main/etl_to_mysql)

## Project 2: API Data to MySQL Data Pipeline
In this project, we are to extract data of all the Dota 2 Heroes from a public API. This data will then get transformed after going though the data pipeline. Finally, it will be loaded into the local MySQL Database.

![Project Visualization](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/blob/main/api_to_mysql_etl/api_to_mysql.gif)

Link : [ETL_Pipeline_API_to_MySQL](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/tree/main/api_to_mysql_etl)

## Project 3: API Data Extaction and Transformation to Azure Blob Storage
In this project, we apply data modelling to the data that is extracted from a public API of NBA Games. This data will be then transformed by the ETL pipeline and then uploaded to a Azure Blob Storage container. The file that is uploaded contains all of the games that we're played today in CSV format.

![Project Visualization](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/blob/main/api_to_azureblob_etl/api_to_blob.gif)

Link : [API_to_Azure_Blob_Storage_ETL_Pipeline](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/tree/main/api_to_azureblob_etl)

## Project 4: Azure Data Lake Storage Event-Triggered Data Transformation Using Azure Data Factory
In this project, we will create an Event-Based Data Transformation using Azure Data Factory. A Blob-Created Event Trigger will be placed inside of a container in Azure Data Lake Storage Gen 2. This trigger will then automatically run our data pipeline in Azure Data Factory once a CSV File is uploaded to the container. The data ingestion, transformation and loading of data to sinks will be done using Azure Databricks. After the data is transformed, Azure Databricks will load the data in Azure SQL Database and Azure Synapse Analytics Dedicated SQL Pool.

![Project Visualization](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/blob/main/azure_adf_etl/azure_etl.gif)

Link : [Azure Data Lake Storage Event-Triggered Data Transformation Using Azure Data Factory](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/tree/main/azure_adf_etl)