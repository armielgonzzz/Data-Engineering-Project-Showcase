{{
    config(
        materialized = 'incremental',
        unique_key = 'manufacturer_id',
        incremental_strategy = 'merge'        
    )
}}

SELECT
    manufacturer_id,
    manufacturer_name,
    manufacturer_state
FROM {{ ref('stg_manufacturers') }}

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}