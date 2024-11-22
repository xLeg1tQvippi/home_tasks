""" 
Сколько слов и в каком количестве используется в этой книге.
Написать программу, которая подсчитывает слова, разделенные пробелом и вывести получившуюся статистику.

// Программа должна считывать одну строку с стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений.
(Без учета регистра.) слово кол-во. 
Порядок произвольный, каждые уникальные слова должны выводится только один раз.

Оценка сложности: 4/10
"""

import war_and_peace

# values = input().lower().split(" ")
values: list = war_and_peace.text.lower().split(" ")
values_list: list = []
values_dict: dict = {}

for value in values:
    if value not in values_list:
        values_list.append(value)
        values_dict[value] = 1
    else:
        values_dict[value] += 1
else:
    for key, value in values_dict.items():
        print(f"{key}: {value}")
