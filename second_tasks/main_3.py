from web_shop_3 import Client
from web_shop_3 import Seller
from web_shop_3 import Web_Shop
from web_shop_3 import Storage

#! Сделать функцию для проверки исключения.


def input_validator(text: str):
    while True:
        try:
            input_value = int(input(text))
        except ValueError as error:
            print("Ошибка при вводе, введите число.")
        else:
            if input_value > -1 and input_value < 3:
                return input_value
            else:
                print("Введите правильные данные.")
                continue


def client_pay_for_product(
    product_amount: int, stock_status: list[bool, list[bool, int]], product: str
):
    total_product_price: int = product_amount * stock_status[1][0]
    print(
        f"Seller: К оплате за {product_amount} {product}, выходит: {total_product_price}\nБудете покупать?\n1 - Да.\n2 - Нет."
    )
    would_client_buy = input_validator(">>>")
    if would_client_buy == 1:
        # Теперь клиент проверяет хватает ли денег на покупку товаров.
        can_buy_status = client.pay(
            product_price=stock_status[1][0], product_amount=product_amount
        )
        if can_buy_status == True:
            # Клиент может позволить себе данный товар.
            print("Client: Да, я покупаю.")
            # Клиент проводит оплату.
            payment_status = client.pay(
                product_price=stock_status[1][0], product_amount=product_amount
            )
            if payment_status == True:
                print("Seller: Оплата проведена успешно!\nSeller: Хорошего дня.")
                web_shop.reduce_product_amount(product=product, amount=product_amount)
            elif payment_status == False:
                print("Client: К сожалению у меня не хватает средств для оплаты.")
        elif can_buy_status == False:
            print("Client: К сожалению, у меня не хватает денег чтобы провести оплату.")
            # * В целом, можно дополнить код, тем, что клиент может убрать один из товаров к оплате, чтобы ему хватило денег покупку.
    elif would_client_buy == 2:
        pass


def request_from_shop_to_vault(
    product_amount: int, stock_status: list[bool, list[bool, int]]
):
    # Функция для запроса товара с склада в магазин.
    # В таком случае, мы делаем запрос на склад.
    # Отнимаем от запрашиваемого количества, то количество которое есть в магазине.
    left_to_send_in_stock: int = product_amount - stock_status[1][1]
    try:
        product_in_vault_status = storage.request_product_from_shop(
            product=product,
            amount=left_to_send_in_stock,
        )
    except Exception as error:
        print(error)

    else:
        print(
            "Seller: Да, количество товара которые вы запросили, есть на складе, мы его отправили уже в магазин.\nПродолжаем покупку?\n1 - Да.\n2 - Нет."
        )
        # TODO Сделать исключение
        client_pay_choice = input_validator(">>>")
        if client_pay_choice == 1:
            pay_status = client_pay_for_product(
                product_amount=product_amount,
                stock_status=stock_status,
                product=product,
            )
            if pay_status == True:
                # Возвращаем значение того, что клиент может совершить покупку.
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    client = Client()
    seller = Seller()
    web_shop = Web_Shop()
    storage = Storage()
    # Основной диалог и концепт
    # Клиент интересуется есть ли продукт в магазине.
    while True:
        product = input("0 - Чтобы выйти\nВведите продукт\nClient: >>>")
        if product == "0":
            break
        product: str = client.ask_for_product(product=product)
        # Возвращаемся к продавцу.
        stock_status = web_shop.check_in_stock(product=product)
        if len(stock_status) > 1:
            # товар есть
            if stock_status[0] == True:
                print(
                    "Seller: Да, товар который вы ищете, есть в магазине, в количестве: {} шт.".format(
                        stock_status[1][1]
                    )
                )
                # * Спрашиваем у клиента будет ли он покупать товар.
                # TODO Сделать исключение
                print("Seller: Будете покупать товар?")
                would_client_buy = input_validator("1 - Да.\n2 - Нет.\nClient: >>>")
                if would_client_buy == 1:
                    # * Клиент покупает товар.
                    print(f"Seller: Сколько {product} вам нужно?")
                    # TODO Исключение
                    product_amount = input_validator(
                        "Введите количество товара.\nClient: >>>"
                    )
                    if product_amount <= stock_status[1][1]:
                        client_pay_for_product(
                            product_amount=product_amount,
                            stock_status=stock_status,
                            product=product,
                        )
                        #     # * В целом, можно дополнить код, тем, что клиент может убрать один из товаров к оплате, чтобы ему хватило денег покупку.
                    else:
                        print(
                            "Seller: К сожалению, в данный момент, количество товара который вы хотите купить, не достаточно в магазине.\nМы можем сделать запрос на склад, но это займет время."
                        )
                        print("Делаем запрос на склад?\n1 - Да.\n2 - Нет.")
                        # TODO Сделать исключение
                        check_product_in_stock_status = input_validator(">>>")
                        if check_product_in_stock_status == 1:
                            request_status = request_from_shop_to_vault(
                                product_amount=product_amount,
                                stock_status=stock_status,
                            )
                            if request_status == True:
                                payment_status = client_pay_for_product(
                                    product_amount=product_amount,
                                    stock_status=stock_status,
                                    product=product,
                                )
                            else:
                                break

            if stock_status[0] == False:
                # Если количество товара равно = 0.
                print(
                    "К сожалению, товар закончился в магазине.\nЕсли хотите, мы можем посмотреть есть ли данный товар на складе."
                )
                # TODO Сделать вариант исключения.
                check_product_in_stock_status = input_validator(
                    "1 - Да.\n2 - Нет.\nClient: >>>"
                )
                if check_product_in_stock_status == 1:
                    request_status = request_from_shop_to_vault(
                        product_amount=product_amount,
                        stock_status=stock_status,
                    )
                    if request_status == True:
                        payment_status = client_pay_for_product(
                            product_amount=product_amount,
                            stock_status=stock_status,
                            product=product,
                        )
                    else:
                        break
        else:
            if stock_status[0] == False:
                print("Товар отсутствует в магазине.")
                # TODO Сделать вариант исключения.
                check_in_vault = input_validator(
                    "Seller: Если хотите, можем посмотреть на складе.\n1 - Да.\n2 - Нет.\nClient: >>>"
                )
                if check_in_vault == 1:
                    # клиент хочет чтобы мы посмотрели на складе.
                    vault_product_status = storage.check_product_in_vault(
                        product=product
                    )
                    if vault_product_status == True:
                        print(
                            "Seller: Товар есть на складе, отправляем его в магазин.\nПродолжаем покупку товара?\n1 - Да.\n2 - Нет."
                        )
                        # TODO Сделать исключение
                        would_client_buy = input_validator(">>>")
                        if would_client_buy == 1:
                            request_status = request_from_shop_to_vault(
                                product_amount=product_amount,
                                stock_status=stock_status,
                            )
                            if request_status == True:
                                payment_status = client_pay_for_product(
                                    product_amount=product_amount,
                                    stock_status=stock_status,
                                    product=product,
                                )
                            else:
                                break
                    elif vault_product_status == False:
                        print("Seller: К сожалению данного продукта нету и на складе.")
