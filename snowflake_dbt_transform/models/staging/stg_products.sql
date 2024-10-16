{{
    config(
        materialized = 'incremental',
        unique_key = 'product_id',
        incremental_strategy = 'merge'
    )
}}

WITH clean_products AS (
    SELECT
        product_id,
        UPPER(product_name) AS product_name,
        product_price,
        manufacturer_id,
        DATE(_FIVETRAN_SYNCED) AS sync_date
    FROM {{ source('mysql_azure_sales_raw', 'products') }}
)

SELECT
    product_id,
    product_name,
    product_price,
    manufacturer_id,
    sync_date
FROM clean_products

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}