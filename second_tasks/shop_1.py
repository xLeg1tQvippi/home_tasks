""" 
Реализуйте класс Shop.
Предусмотреть возможность работы с произвольным числом продуктов, 
поиска продуктов по названию,
добавления их в магазин и удаления продуктов из него.

Основной словарь с продуктами -> storage - dict
Освновной магазин с витриной -> shop - list
"""

import array
import time


class Shop:
    def __init__(self, products: list):
        self.__product_list = products

    def show_product_list(self):
        print("\nВитрина магазина:")
        if self.__product_list == []:
            print("Пусто.")
        else:
            # Для незатратного вывода/просмотра данных нужно использовать множества. (arrays) # Да, делаю замечания самому себе)
            [print(product) for product in self.__product_list]
        print()

    # Дополнительно: Можно реализовать выбор товара из витрины. Присвоить товару цену, и прочее.


class Storage:
    def __init__(self):
        self.__vault: dict = dict()
        self.__product_list: list = list()

    def check_product(self, product: str) -> bool:
        # Проверяем, есть ли введенный продукт уже в списке.
        if product in self.__product_list:  # O(1)
            return True
        else:
            return False

    def add_product(self, product: str, amount: int):
        # В этой функции, мы реализуем добавление продуктов в словарь.
        # Делаем проверку есть ли данный продукт
        validence = self.check_product(product=product)
        if validence == True:
            while True:
                # Кейс, когда продукт уже есть в списке товаров.
                try:
                    choice_to_add: int = int(
                        input(
                            f"Кажется продукт {product} уже есть на складе!\nВведите 1 - Чтобы добавить число товаров к его общему количеству.\nВведите 2 - Чтобы отменить добавление.\n>>>"
                        )
                    )
                except:
                    continue
                else:
                    if choice_to_add == 1:
                        # Кейс для добавления к общему количеству продукта в словарь.
                        self.__vault[product] += int(amount)
                        print(
                            f"Добавление успешно завершено.\nТекущее количество продукта {product}: {self.__vault[product]}"
                        )
                        return
                    if choice_to_add == 2:
                        print("Добавление товара отменено.")
                        return
        if validence == False:
            while True:
                try:
                    product_appending_choice = int(
                        input(
                            f"Данный продукт отсутствует на складе, желаете добавить?\nВведите 1 - Чтобы добавить.\nВведите 2 - Чтобы отменить добавление.\n>>>"
                        )
                    )
                except Exception as error:
                    print(
                        "Произошла ошибка при выборе, повторите попытку.\n{}".format(
                            error
                        )
                    )
                    time.sleep(2)
                    continue
                else:
                    if product_appending_choice == 1:
                        # Добавляем новый продукт на склад.
                        self.__vault[product] = int(amount)
                        self.__product_list.append(product)
                        print(
                            f"Добавление продукта {product} на склад успешно завершено!"
                        )
                        return
                    if product_appending_choice == 2:
                        print("Добавление продукта отменено.")
                        return

    def remove_product(self, product: str):
        # Функция удаления продукта из словаря.
        validence = self.check_product(product=product)
        if validence == True:
            # Кейс когда удаляемый продукт существует в списке.
            while True:
                try:
                    confirm_delete = int(
                        input(
                            f"Введите:\n1 - Чтобы подтвердить удаления продукта {product} из списка.\n2 - Чтобы отменить удаление.\n>>>"
                        )
                    )
                except Exception as error:
                    print(f"Произошла ошибка во время ввода.\nПовторите попытку.")
                    time.sleep(2)
                    continue
                else:
                    if confirm_delete == 1:
                        self.__vault.pop(product)
                        self.__product_list.remove(product)
                        print(f"Удаление продукта {product}, успешно завершено.")
                        return
                    else:
                        print("Удаление отменено.")
                        return
        else:
            print("Продукт не найден.")
            return 0

    def show_product_lists(self):
        # Функция вывода информации по количеству имеющихся продутков.
        print("\nСклад:")
        [print(f"{product}: {amount}") for product, amount in self.__vault.items()]
        print()


if __name__ == "__main__":
    storage = Storage()
    shop = Shop(products=[])
    print("Добро пожаловать!")
    greeting_menu = "Введите запрос:\n1 - Добавить продукт на склад и витрину.\n2 - Удалить продукт из склада и витрины.\n3 - Просмотреть наличие продуктов.\n4 - Витрина магазина.\n0 - Выйти из программы."
    while True:
        print(greeting_menu)
        try:
            menu = int(input(">>>"))
        except Exception as error:
            print(f"Произошла ошибка при выборе, повторите попытку.\n{error}")
            time.sleep(2)
            continue
        else:
            if menu == 1:
                while True:
                    print("Введите добавляемый продукт, и его количество через пробел.")
                    products = input(">>>").split(" ")

                    # Дополнительно: Можно сделать проверку на валидность данных. Первый элемент списка должен быть строковым типом данных.
                    # Второй элемент списка, должен быть числовым.
                    # Если оба условия истины, то добавляем продукт на склад.

                    if len(products) != 2:
                        print("При вводе продукта произошла ошибка, повторите попытку.")
                        continue
                    elif len(products) == 2:
                        storage.add_product(product=products[0], amount=products[1])
                        break
            elif menu == 2:
                while True:
                    print("Введите продукт для удаления (Введите 0 чтобы выйти.)")
                    products = input(">>>")
                    if products != "0":
                        removing = storage.remove_product(product=products)
                        if removing == 0:
                            continue
                        else:
                            break
                    else:
                        break
            elif menu == 3:
                storage.show_product_lists()
            elif menu == 4:
                shop.__init__(products=storage._Storage__product_list)
                shop.show_product_list()
            elif menu == 0:
                print("Выходим из программы...")
                time.sleep(2)
                break
