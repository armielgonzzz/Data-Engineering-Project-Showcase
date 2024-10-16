{{
    config(
        materialized = 'incremental',
        unique_key = 'order_id',
        incremental_strategy = 'merge'        
    )
}}

SELECT
    order_id,
    product_id,
    customer_id,
    date_id,
    manufacturer_id,
    total_order_cost
FROM {{ ref('stg_orders') }}

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}