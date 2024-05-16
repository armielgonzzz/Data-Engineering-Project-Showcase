# Azure Data Lake Storage Event-Triggered Data Transformation Using Azure Data Factory

![Project Visualization](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/blob/main/azure_adf_etl/azure_etl.gif)

## **Overview**

In this project, we will create an Event-Based Data Transformation using Azure Data Factory. A Blob-Created Event Trigger will be placed inside of a container in Azure Data Lake Storage Gen 2. This trigger will then automatically run our data pipeline in Azure Data Factory once a CSV File is uploaded to the container. The data ingestion, transformation and loading of data to sinks will be done using Azure Databricks. After the data is transformed, Azure Databricks will load the data in Azure SQL Database and Azure Synapse Analytics Dedicated SQL Pool.


## Schema

**top_grossing_movies** - This table contains name of the movie distributors and information about their movies.

```
distributor, avg_sale_per_distributor, distributor_n_movies, top_movie, top_movie_sales
```

## Project Files

```event_based_pyspark_transform.ipynb``` -> This notebook contains the steps and process of ingesting the data to Azure Databricks, transforming the data and loading the data to Azure SQL Database and Azure Synapse Analytics Dedicated SQL Pool

```event_based_trigger_unmount.ipynb``` -> In case when the main notebook run fails, this notebook will unmount the ADLS Container from Azure Databricks.


## Environment 
Apache Spark 3.4.1

Scala 2.12

Microsoft Azure

Azure Data Lake Storage Gen 2

Azure Data Factory

Azure Databricks

Azure SQL Database

Azure Synapse Analytics

Azure Key Vaults


## Reference
[Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/)

[Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/)

[Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/)
