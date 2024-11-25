""" 
Оценка сложности: O(n * n)
"""


def get_unique_values(text: list) -> str:
    dash = "-"
    sorted_list = []
    indexies = []
    default_text: str = "".join(text)  # O(1)
    for index, letter in enumerate(text):  # for & enumirate = O(n)
        index_letter = default_text.index(letter) # O(n)
        if index_letter not in indexies: # O(n)
            indexies.append(index_letter) # O(1)
        else:
            print("else")
            pass
    else:
        for index, letter in enumerate(text): # O(n)
            for sorted_index in indexies: # O(n)
                if index == sorted_index: # O(1)
                    sorted_list.append(letter) # O(1)
        else:
            return "".join(sorted_list)


try:
    string: list = list(input("Введите текст\n>>>"))  # O(n)
except Exception as error:
    print(f"Произошла ошибка, повторите попытку.\n{error}")
else:
    func = get_unique_values(text=string)
    print(f"Отсортированный текст:\n{func}")
