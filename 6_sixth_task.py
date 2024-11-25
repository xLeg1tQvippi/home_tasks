"""
Дан список . Продублировать все неповторяющиеся элементы.

Оценка сложности: O(n * n)
"""

values: list = [1, 2, 2, "House", "Flight", 4, 4, -2]

new_values_list: list = []

for value in values:  # O(n)
    if value not in new_values_list:  # O(k)
        new_values_list.append(value)  # O(1)
    else:
        print(f"value {value} is repeated element")
        new_values_list.remove(
            value
        )  # O(k) # Требуется поиск позиции элемента, и сдвиг оставшихся элемнтов O(2k) приблизительно O(k)
else:
    for value in new_values_list:  # O(n)
        values.append(value)  # O(1)
print(new_values_list)
print(values)
