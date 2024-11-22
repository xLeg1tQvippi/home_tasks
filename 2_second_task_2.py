""" 
Оценка сложности: 7/10
"""


def get_unique_values(text: list) -> str:
    dash = "-"
    sorted_list = []
    indexies = []
    default_text: str = "".join(text)
    for index, letter in enumerate(text):
        print(dash * 20)
        index_letter = default_text.index(letter)
        find_letter = default_text.find(letter)
        print("find:", find_letter)
        print("index():", index_letter)
        print("letter:", letter)
        print("index:", index)
        print(dash * 20)
        if index_letter not in indexies:
            indexies.append(index_letter)
        else:
            print("else")
            pass
    else:
        for index, letter in enumerate(text):
            for sorted_index in indexies:
                if index == sorted_index:
                    sorted_list.append(letter)
        else:
            return "".join(sorted_list)


try:
    string: list = list(input("Введите текст\n>>>"))
except Exception as error:
    print(f"Произошла ошибка, повторите попытку.\n{error}")
else:
    func = get_unique_values(text=string)
    print(f"Отсортированный текст:\n{func}")
