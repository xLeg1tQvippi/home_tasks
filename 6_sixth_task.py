"""
Дан список . Продублировать все неповторяющиеся элементы.

Оценка сложности: 6/10
"""

values: list = [1, 2, 2, "House", "Flight", 4, 4, -2]

new_values_list: list = []

for value in values:
    if value not in new_values_list:
        new_values_list.append(value)
    else:
        print(f"value {value} is repeated element")
        new_values_list.remove(value)
else:
    for value in new_values_list:
        values.append(value)
print(new_values_list)
print(values)
