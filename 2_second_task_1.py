""" 
Оценка сложности: O(n)
"""


def get_unique_values(text: list) -> str:
    sorted_text: list = list(set(text))  # O(n)
    new_text: str = "".join(sorted_text)  # O(k)
    return new_text


try:
    string: list = list(input("Введите текст\n>>>"))  # O(n)
except Exception as error:
    print(f"Произошла ошибка, повторите попытку.\n{error}")
else:
    func = get_unique_values(text=string)
    print(f"Отсортированный текст:\n{func}")
