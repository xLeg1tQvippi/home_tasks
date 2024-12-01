class InsufficientProductException(Exception):
    def __init__(self, text):
        super().__init__(text)


class ProductNotInStock(Exception):
    def __init__(self, text):
        super().__init__(text)




class Web_Shop:
    def __init__(self):
        # Продукт: [цена, количество]
        self.vault = {
            "Bread": [175, 2],
            "Milk": [315, 5],
            "Meat": [615, 3],
            "Apple": [95, 6],
            "Salt": [210, 2],
        }

    def check_in_stock(self, product: str) -> bool | list[bool, list[int, int]]:
        # Запрос в магазин, есть ли у нас опред. товар
        try:
            self.vault[product]
        except Exception as error:
            return [False]
        else:
            product_amount = self.vault[product]
            if product_amount[1] == 0:
                # Говорим, что товар закончился.
                return [False, product_amount]
            # Говорим, что да, товар есть, в таком-то количестве.
            if product_amount[1] > 0:
                return [True, product_amount]

    def reduce_product_amount(self, product: str, amount: int):
        # Основной принцип покупки, после подтверждения, что клиент покупает товар, отнимаем количество купленного товара.
        self.vault[product][1] -= amount

    def add_product_amount(self, product: str, amount: int):
        # Добавляем полученный товар с скалада в магазин.
        self.vault[product][1] += amount


class Storage:
    def __init__(self):
        # Представим что, у нас на складе уже есть товар.
        self.__product_vault = {
            "Bread": 7,
            "Milk": 3,
            "Cheese": 9,
            "Apple": 12,
            "Bubble": 17,
            "Sugar": 4,
            "Lolipop": 8,
        }

    def check_product_in_vault(self, product: str) -> bool:
        # Реализуем проверку наличия продукта на складе.
        if product in self.__product_vault.keys():
            return True
        else:
            return False

    def check_product_amount(self, product: str, amount: int) -> bool:
        default_product_value = self.__product_vault[product]
        if default_product_value <= amount:
            return True
        else:
            return False

    def set_new_vault_value(self, product: str, amount: int):
        self.__product_vault[product] -= amount
        # Возвращаем значение amount, "чтобы отправить его в магазин"
        return amount

    def request_product_from_shop(self, product: str, amount: int) -> list | None:
        # Реализуем отправку продуктов с склада в магазин по запросу.
        # Для начала проверяем есть ли продукт на складе.
        product_in_vault_status = self.check_product_in_vault(product=product)
        # Если на складе имеется товар, то смотрим, есть ли полученное количество товара.
        if product_in_vault_status == True:
            amount_product_in_vault = self.check_product_amount(
                product=product, amount=amount
            )
            if amount_product_in_vault == True:
                set_and_return_value = self.set_new_vault_value(
                    product=product, amount=amount
                )
                return [product, set_and_return_value]
            if amount_product_in_vault == False:
                raise InsufficientProductException(
                    "Storage: Ошибка!\nЗапрашиваемое количество товара превышает имеющиеся количество товара на складе."
                )
        if product_in_vault_status == False:
            raise ProductNotInStock("Storage: Ошибка!\nТовар отсутствует на складе.")

    def add_products_to_vault(self):
        # Добавление продуктов на склад.
        pass


class Client:
    def __init__(self):
        self._money = 2900

    def ask_for_product(self, product: str):
        # Клиент спрашивает, есть ли определенный продукт в магазине.
        print(f"Есть ли у вас {product}?")
        return product

    def can_buy_product(self, product_price: int, product_amount: int) -> bool:
        # Проверяем наш кошелек, и смотрим можем ли мы купить желаемый продукт.
        if (product_price * product_amount) <= self._money:
            return True
        else:
            return False

    def pay(self, product_price: int, product_amount: int):
        # Оформление покупки товара.
        """
        Сделано неправильно, с точки зрения того, что можно сделать список/словарь, того что покупает клиент.
        После чего, счиатется весь список продуктов после - происходит оплата.
        """
        payment_status = self.can_buy_product(
            product_price=product_price, product_amount=product_amount
        )
        if payment_status == True:
            total_product_price = product_price * product_amount
            self._money -= total_product_price
            # Покупка успешно совершена.
            return True
        if payment_status == False:
            # Недстаточно средств для покупки.
            return False


class Seller(Web_Shop, Storage):
    # Товаровед, имеет доступ к запросам на склад.
    pass
