{{
    config(
        materialized = 'incremental',
        unique_key = 'product_id',
        incremental_strategy = 'merge'        
    )
}}

SELECT
    product_id,
    product_name,
    product_price
FROM {{ ref('stg_products') }}

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}