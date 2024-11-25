""" 
Оценка сложности: O(n * n)
"""

from copy import deepcopy

values: list = [18, 42, 8, 122]
total_values: list = deepcopy(values)  # O(n)
for value in values:  # O(n)
    try:
        val_index: int = total_values.index(
            value
        )  # O(m) - m текущее количество элементов в total_values
        reversed_number: int = int(
            str(value)[::-1]
        )  # Число в строку - O(d) # (d) - количество цифр в числе, # Разворот строки O(d)
        # Преобрзование обратно в число O(d), общее: O(d)
        total_values.insert(
            val_index + 1, reversed_number
        )  # O(m) - вставка, и сдвиг элементов
    except Exception as error:
        print(error)
else:
    print(total_values)
