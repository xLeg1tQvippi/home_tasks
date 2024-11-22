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

Оценка сложности: 5/10
"""


def join_last_words(splitted: list) -> str:
    splitted.pop(0)
    last_words = " ".join(splitted)
    return last_words


def post_func(value: str):
    if value.isdigit() == True:
        value: int = int(value)
    server.append(value)
    print(f"Успешно добавлено!\nТекущий список: {server}")


def get_func():
    print(server[-1])


def delete_func():
    server.pop(-1)


def qualify_request(request: list):
    try:
        if request[0] == "POST":
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
        print(f"Произошла ошибка\n{error}")


if __name__ == "__main__":
    server: list = []
    print("Добро пожаловать в сервер!\nВведите запрос")
    while True:
        try:
            request: list = input(">>>").split(" ")
        except Exception as error:
            print(f"Произошла ошибка!\n{error}")
        else:
            qualified_request = qualify_request(request=request)
