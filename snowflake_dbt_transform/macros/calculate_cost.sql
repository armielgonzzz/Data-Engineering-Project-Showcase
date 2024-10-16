{% macro calculate_cost(price, discount, quantity) %}

    ROUND(({{ price }} * (1 - {{ discount }})) * {{ quantity }}, 2)

{% endmacro %}