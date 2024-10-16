{% test valid_day_of_week(model, column_name) %}

SELECT *
FROM {{ model }}
WHERE {{ column_name }} NOT IN ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')

{% endtest %}