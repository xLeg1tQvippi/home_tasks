""" 
Оценка сложности: 4/10
"""


def get_unique_values(text: list) -> str:
    sorted_text: list = list(set(text))
    new_text: str = "".join(sorted_text)
    return new_text


try:
    string: list = list(input("Введите текст\n>>>"))
except Exception as error:
    print(f"Произошла ошибка, повторите попытку.\n{error}")
else:
    func = get_unique_values(text=string)
    print(f"Отсортированный текст:\n{func}")
