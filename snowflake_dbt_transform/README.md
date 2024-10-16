# Snowflake Datawarehouse ELT using Fivetran & dbt

![Project Visualization](https://github.com/armielgonzzz/Data-Engineering-Project-Showcase/blob/main/snowflake_dbt_transform/snowflake_dbt_transform.gif)

## Overview

In this project, we will create an ELT Pipeline using the tools **Fivetran** and **dbt**. **Fivetran** will handle the extraction and loading of data from Azure MySQL database to Snowflake Data Warehouse. While, **dbt** will transform the raw OLTP data that was loaded from Azure MySQL Database into an OLAP Data to Snowflake Data Warehouse.

## Schema

**dim_customers** - Dimension table for customer informations.

**dim_manufacturers** - Dimension table for manufacturers of all products

**dim_products** - Dimension table for all available products

**dim_order_dates** - Dimension table for the dates of all orders

**fact_orders** - Fact table that will store the measures of each dimensions

## Project Files

```macros``` - This directory contains all macros or functions that will be used in data transformations

```models``` - This folder contains all SQL Transformations done in the raw data, including the .yml files that describes all the models

```profile``` - Contains the .yml file that stores the Snowflake Data Warehouse credentials

```tests``` - SQL Files for customer tests done in the output tables in the data warehouse

```dbt_project.yml``` - The main configuration file for dbt that defines settings and behaviors of the project

```dbt_run.py``` - Python script that will execute dbt and all tests

```requirements.txt``` - Dependencies required to run the transformations

## Environment

Python 3.10.11

dbt 1.8.7

Snowflake Adapter 1.8.3

Azure MySQL Database 8.0

Fivetran


## Reference

[dbt Documentation](https://docs.getdbt.com/docs/build/documentation)

[Fivetran Documentation](https://fivetran.com/docs/getting-started)

[Snowflake Documentation](https://docs.snowflake.com/)

[Azure MySQL Documentation](https://learn.microsoft.com/en-us/azure/mysql/)