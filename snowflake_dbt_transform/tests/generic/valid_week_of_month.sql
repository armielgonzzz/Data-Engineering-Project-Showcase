{% test valid_week_of_month(model, column_name) %}

SELECT * FROM {{ model }}
WHERE {{ column_name }} NOT BETWEEN 0 AND 6

{% endtest %}