""" 
Оценка сложности: 2/10
"""

from copy import deepcopy

values: list = [18, 42, 8, 122]
total_values: list = deepcopy(values)
for value in values:
    try:
        val_index: int = total_values.index(value)
        reversed_number: int = int(str(value)[::-1])
        total_values.insert(val_index + 1, reversed_number)
    except Exception as error:
        print(error)
else:
    print(total_values)
