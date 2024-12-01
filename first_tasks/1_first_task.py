""" 
Задано два списка.
Найти наименьшие среди элементов первого списка,
которые не входят во второй список.

Оценка сложности: O(n * m)
"""

first_list: list = [4, 2, 1, 6, 8, -2]
second_list: list = [4, 7, 1, 4, 3, -2]
total: list = []

sorted_flist: list = sorted(first_list) # O(n log n)
for f_number in sorted_flist: # O(n)
    if f_number in second_list: # O(m) 
        print(f"{f_number} in second_list!")
    else:
        print(f"{f_number} not in second_list!")
        total.append(f_number) # O(n)
else:
    print(f"Минимальное число не входящее в второй список: {min(total)}") # O(n)
