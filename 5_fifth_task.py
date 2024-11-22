""" 
Дан список. Вычислить сколько раз в нем встречается каждый элемент, не используя сортировки.

Оценка сложности: 7/10 
"""

values: list = ["Дом", "Здание", "Дом", 1, 5, 7, 1.2, 5, 1.2, 2]

values_list: list = []
values_dict: dict = {}

for value in values:
    if value not in values_list:
        values_list.append(value)
        values_dict[value] = 1
    else:
        values_dict[value] += 1
else:
    print(values_dict)
    print(values_list)
