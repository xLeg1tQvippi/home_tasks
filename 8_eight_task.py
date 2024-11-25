""" 
Сколько слов и в каком количестве используется в этой книге.
Написать программу, которая подсчитывает слова, разделенные пробелом и вывести получившуюся статистику.

// Программа должна считывать одну строку с стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений.
(Без учета регистра.) слово кол-во. 
Порядок произвольный, каждые уникальные слова должны выводится только один раз.

Оценка сложности: O(n)
"""

import war_and_peace

# values = input().lower().split(" ")
values: list = war_and_peace.text.lower().split(" ")  # O(m)
values_list: list = []
values_dict: dict = {}

for value in values:  # O(n)
    if value not in values_list:  # O(n)
        values_list.append(value)  # O(1)
        values_dict[value] = 1  # O(1)
    else:
        values_dict[value] += 1  # O(1)
else:
    for key, value in values_dict.items():  # O(u) - u - кол-во уник. слов
        print(f"{key}: {value}")
