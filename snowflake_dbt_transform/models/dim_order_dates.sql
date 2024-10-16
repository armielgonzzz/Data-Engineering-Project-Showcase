{{
    config(
        materialized = 'incremental',
        unique_key = 'date_id',
        incremental_strategy = 'merge'        
    )
}}
SELECT
    date_id,
    day_of_week,
    week_of_month,
    month,
    year
FROM {{ ref('stg_order_dates') }}

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}