{{
    config(
        materialized = 'incremental',
        unique_key = 'manufacturer_id',
        incremental_strategy = 'merge'
    )
}}

WITH clean_manufacturers AS (
    SELECT
        manufacturer_id,
        UPPER(name) AS manufacturer_name,
        UPPER(state) AS manufacturer_state,
        DATE(_FIVETRAN_SYNCED) AS sync_date
    FROM {{ source('mysql_azure_sales_raw', 'manufacturers') }}
)

SELECT
    manufacturer_id,
    manufacturer_name,
    manufacturer_state,
    sync_date
FROM clean_manufacturers

{% if is_incremental() %}

WHERE sync_date <= CURRENT_DATE()

{% endif %}