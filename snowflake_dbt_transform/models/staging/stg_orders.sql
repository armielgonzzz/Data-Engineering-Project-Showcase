{{
    config(
        materialized = 'incremental',
        unique_key = 'order_id',
        incremental_strategy = 'merge'
    )
}}

WITH format_date_id AS (
    SELECT
        order_id,
        product_id,
        customer_id,
        CAST(TO_CHAR(order_date, 'YYYYMMDD') AS INTEGER) AS date_id,
        item_quantity,
        DATE(_FIVETRAN_SYNCED) AS sync_date
    FROM {{ source('mysql_azure_sales_raw', 'orders') }}
)
, add_manufacturer_id AS (
    SELECT
        d.*,
        p.product_price,
        p.manufacturer_id
    FROM format_date_id d
    LEFT JOIN {{ ref('stg_products') }} p USING(product_id)
)

SELECT
    order_id,
    product_id,
    customer_id,
    date_id,
    {{ calculate_cost(
        'product_price',
        'c.customer_discount',
        'item_quantity') }} AS total_order_cost,
    manufacturer_id,
    sync_date
FROM add_manufacturer_id
LEFT JOIN {{ ref('dim_customers') }} c USING(customer_id)

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}