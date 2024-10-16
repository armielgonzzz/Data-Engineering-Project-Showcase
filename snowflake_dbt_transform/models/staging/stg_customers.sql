{{
    config(
        materialized = 'incremental',
        incremental_strategy = 'merge',
        unique_key = 'customer_id'
    )
}}

WITH clean_customers_table AS (
    SELECT
        c.customer_id,
        CONCAT_WS(' ', UPPER(c.first_name), UPPER(c.last_name)) AS full_name,
        UPPER(c.state) AS state,
        CAST(c.created_at AS DATE) AS date_creation,
        c.customer_type_id,
        DATE(c._FIVETRAN_SYNCED) AS sync_date
    FROM {{ source('mysql_azure_sales_raw', 'customers') }} c
)
, add_customer_type AS (
    SELECT
        c.*,
        UPPER(t.customer_type) AS customer_type,
        t.discount_rate AS customer_discount
    FROM clean_customers_table c
    JOIN {{ source('mysql_azure_sales_raw', 'customer_types') }} t USING(customer_type_id)
)

SELECT
    customer_id,
    full_name,
    state,
    customer_type,
    customer_discount,
    date_creation,
    sync_date
FROM add_customer_type

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}