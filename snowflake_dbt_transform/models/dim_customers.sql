{{
    config(
        materialized = 'incremental',
        unique_key = 'customer_id',
        incremental_strategy = 'merge'        
    )
}}

SELECT
    customer_id,
    full_name,
    state,
    customer_type,
    customer_discount,
    date_creation
FROM {{ ref('stg_customers') }}

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}