""" 
Дан список. Вычислить сколько раз в нем встречается каждый элемент, не используя сортировки.

Оценка сложности: O(n * n)
"""

values: list = ["Дом", "Здание", "Дом", 1, 5, 7, 1.2, 5, 1.2, 2]

values_list: list = []
values_dict: dict = {}

for value in values:  # O(n)
    if value not in values_list:  # O(n * n)
        values_list.append(value)  # O(1)
        values_dict[value] = 1  # O(1)
    else:
        values_dict[value] += 1  # O(1)
else:
    print(values_dict)
    print(values_list)
