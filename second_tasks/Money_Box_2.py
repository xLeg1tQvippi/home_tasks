import time


class MoneyBox:
    def __init__(self):
        self.capacity()

    def capacity(self):
        # self.__value: int = value
        self._capacity_limit: int = (3200,)  #  перевести в tuple
        self._default_capacity_value: int = 0
        # limited_capacity - ограничение вместимости копилки.
        # total_capacity - это текущее значение копилки. Т.е. сколько сейчас она хранит в себе.
        self.__limited_capacity = self._capacity_limit
        self.__total_capacity = self._default_capacity_value

    def check_capacity(self):
        print(
            "Текущее количество монет в копилке: {}/{}".format(
                self.__total_capacity, self.__limited_capacity[0]
            )
        )
        print(
            "Количество монет которое можно внести: {}".format(
                self.__limited_capacity[0] - self.__total_capacity
            )
        )

    def _can_add(self, value: int):
        self.__value = value
        total_left = self.get_capacity_lasts()
        # print(total_left)
        if self.__value <= total_left:
            return True
        else:
            return False

    def get_capacity_lasts(self):
        capacity_lasts = self.__limited_capacity[0] - self.__total_capacity
        return capacity_lasts

    def add(self, value: int):
        add_status = self._can_add(value=value)
        if add_status == True:
            self.__total_capacity += value
            print(f"В копилку успешно добавлено {value} монет.")
            return
        else:
            print(f"Привышение лимита копилки.")
            return


if __name__ == "__main__":
    moneyBox = MoneyBox()
    print("Добро пожаловать в виртуальную копилку.")
    while True:
        try:
            menu = int(
                input(
                    "Введите:\n1 - Чтобы добавить монеты в копилку.\n2 - Посмотреть количество монет в копилке.\n0 - Чтобы выйти.\n>>>"
                )
            )
        except Exception as error:
            print(f"Произошла оишбка при выборе. Повторите попытку.\n{error}")
            time.sleep(2)
            continue
        else:
            if menu == 1:
                while True:
                    try:
                        value = int(input("Введите количество монет.\n>>>"))
                    except Exception as error:
                        print(
                            f"Произошла ошибка при вводе данных, повторите попытку.\n{error}"
                        )
                    else:
                        moneyBox.add(value=value)
                        break
            elif menu == 2:
                moneyBox.check_capacity()

            elif menu == 0:
                print("Выходим из программы...")
                time.sleep(2)
                break
