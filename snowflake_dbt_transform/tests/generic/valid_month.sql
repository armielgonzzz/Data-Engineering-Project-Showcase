{% test valid_month(model, column_name) %}

SELECT * FROM {{ model }}
WHERE {{ column_name }} NOT BETWEEN 0 and 13

{% endtest %}