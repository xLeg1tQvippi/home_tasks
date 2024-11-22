""" 
Два вида запросов:
Строка - содержащая имя контакта и его номер. Ex: Ben 89001234050 (Разделеные пробелом).
Строка - содержащая имя контакта.

В первом случае - программа должна добавить в книгу новый номер, 
в втором - вывести номер контакта.

Если введенное имя уже содержится в списке кеонтаков, необходимо перезаписать номер.

Ben 89001234050

if ben in dictionary:
    rewrite ben number
elif ben not in dictionary:
    append ben, append number
elif ben:
    return ben's number
    
    
Оценка сложности: 6/10
"""

file_name = "u_fourth_contact_dictionary.py"


def check_data_file() -> dict:
    try:
        from fourth_contact_dictionary import contacts
    except Exception as error:
        with open(file_name, "w") as file:
            file.write("contacts = {}")
    else:
        return contacts


def rewriting_contact_number(name: str, number: str, contact_book: dict):
    previous_contact_number: str = contact_book[name]
    contact_book[name] = number
    with open(file_name, "w") as file:
        file.write(f"contacts = {contact_book}")
    print(
        f"Предыдущий номер контакта {name}: {previous_contact_number}\nУспешно перезаписан на новый номер: {number}"
    )


def get_contact_information(name: str, contact_book: dict):
    try:
        person_number: str = contact_book[name]
        print(f"Номер контакта {name}: {person_number}")
    except Exception as error:
        print(f"Введенный контакт {name} не найден в списке контактов.")


def search_info(data: str, contact_book: dict):
    # Получаем данные для запроса
    try:
        data_unpacking: list = data.split(" ")
    except Exception as error:
        print(f"Произошла ошибка!\n{error}")
    else:
        # Если все гуд, распределяем данные и запросы
        try:
            amount_of_objects: int = len(data_unpacking)
            if amount_of_objects == 2:
                print("Перезапиcиываем номер!")
                # Если объектов 2, то это Имя и номер - Что означает перезапись номера.
                rewriting_contact_number(
                    name=data_unpacking[0],
                    number=data_unpacking[1],
                    contact_book=contact_book,
                )
            elif amount_of_objects == 1:
                get_contact_information(
                    name=data_unpacking[0], contact_book=contact_book
                )

        except Exception as error:
            print(f"Произошла ошибка!\n{error}")


if __name__ == "__main__":
    contact_book: function = check_data_file()
    print("Дoбро пожаловать в книгу контактов!\nВведите '.' чтобы выйти из программы.")
    while True:
        try:
            command: str = input(">>>")
        except Exception as error:
            print(f"Произошла ошибка!\n{error}")
            print("Пожалуйста введите еще раз.")
            continue
        else:
            if command == ".":
                input(
                    "Спасибо за использование нашей программы!\nНажмите Enter чтобы выйти из программы..."
                )
                break
            else:
                # Находим в списке введенные данные.
                get_information = search_info(command, contact_book=contact_book)
