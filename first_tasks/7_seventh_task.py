"""
У нас есть сервер.
Требуется реализовать запросы:
GET, POST, DELETE.

POST - Добавляет строку на сервер.
GET - Возвращает последнюю добавленную строку.
DELETE - Удаляет последнюю добавленную строку.

GET & DELETE - Не принимает параметров
POST - Принимает.

'.' - конец программы.

[12, 15, 81]
81
DELETE
[12, 15]
DELETE
[12]
[12, StackOverflow]
[12, StackOverFlow, Recursion]
[12, StackOverflow]

Оценка сложности: O(k+m+l), а так же зависит от количество запросов: q
total: O(q*(k+m+l))
"""


def join_last_words(splitted: list) -> str:
    splitted.pop(0)  # O(k)
    last_words = " ".join(splitted)  # O(m)
    return last_words  # total: O(k+m)


def post_func(value: str):
    if value.isdigit() == True:  # O(l) зависит от длины строки l.
        value: int = int(value)
    server.append(value)  # O(1)
    print(f"Успешно добавлено!\nТекущий список: {server}")  # total: O(l)


def get_func():
    print(server[-1])  # total O(1)


def delete_func():
    server.pop(-1)  # total: O(1)


def qualify_request(request: list):
    try:
        if request[0] == "POST":  # O(1)
            try:
                last_words = join_last_words(request)
                post_func(value=last_words)
            except Exception as error:
                print(f"Произошла ошибка\n{error}")
        elif request[0] == "GET":
            get_func()
        elif request[0] == "DELETE":
            delete_func()
        else:
            print("Запрос не распознан, повторите попытку.")
    except Exception as error:
        print(
            f"Произошла ошибка\n{error}"
        )  # total: POST = O(k+m+l) #total GET + DELETE = O(1)


if __name__ == "__main__":
    server: list = []
    print("Добро пожаловать в сервер!\nВведите запрос")
    while True:
        try:
            request: list = input(">>>").split(" ")  # O(m), split = O(m)
        except Exception as error:
            print(f"Произошла ошибка!\n{error}")
        else:
            qualified_request = qualify_request(request=request)
