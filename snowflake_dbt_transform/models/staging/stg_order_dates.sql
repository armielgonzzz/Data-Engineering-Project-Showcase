{{
    config(
        materialized = 'incremental',
        unique_key = 'date_id',
        incremental_strategy = 'merge'
    )
}}

WITH extract_date_info AS (
    SELECT DISTINCT
        CAST(TO_CHAR(order_date, 'YYYYMMDD') AS INTEGER) AS date_id,
        DAYNAME(order_date) AS day_of_week,
        CEIL(DAYOFMONTH(order_date) / 7.0) AS week_of_month,
        MONTH(order_date) AS month,
        YEAR(order_date) AS year,
        DATE(_FIVETRAN_SYNCED) AS sync_date
    FROM {{ source('mysql_azure_sales_raw', 'orders') }}
)

SELECT
    date_id,
    UPPER(day_of_week) AS day_of_week,
    week_of_month,
    month,
    year,
    sync_date
FROM extract_date_info

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}