class Carrier:
    def __init__(self):
        # [Точка отправки - Точка назначения]: Расстояние

        self.departure_city = "Москва"
        # destination_cities = {"Стамбул", "Берлин", "Париж", "Рим", "Хельсинки"}
        self.city_and_distance: dict = {
            "Стамбул": 2200,
            "Берлин": 1800,
            "Париж": 2800,
            "Рим": 3000,
            "Хельсинки": 1100,
        }
        self.currency = "euro"

    def get_countries(self):
        return self.city_and_distance

    def get_departure_city(self):
        return self.departure_city

    def get_average_time_until_destination(self, distance: int, average_speed: int):
        return distance / average_speed

    def average_speed_formula(self, min_speed: int, max_speed: int):
        return (min_speed + max_speed) / 2

    def get_total_price_for_distance(self, distance: int, price_per_km: int):
        return distance * price_per_km

    def get_total_price_for_distance_Car(
        self,
        distance: int,
        fuel_flow_distance: int,
        fuel_flow: int,
        fuel_price_per_litre: float,
    ):
        return (distance / fuel_flow_distance) * fuel_flow * fuel_price_per_litre

    def get_total_price_for_distance(self, distance: int, average_price: float):
        return distance * average_price


class Plane(Carrier):
    def __init__(self, distance_to_distantion):
        super().__init__()
        # Указаваем данные в часах
        self.registration_time = 2
        self.get_and_send_luggage = 0.5

        self.total_registration_time = (
            self.registration_time + self.get_and_send_luggage
        )

        self.price_per_km = 0.15

        # км/ч
        min_speed = 800
        max_speed = 950
        # Получаем среднюю скорость транспорта.
        self.average_speed = self.average_speed_formula(
            min_speed=min_speed, max_speed=max_speed
        )

        self.time_to_distanation = self.get_average_time_until_destination(
            distance=distance_to_distantion, average_speed=self.average_speed
        )
        self.total_time_to_distanation = (
            self.time_to_distanation + self.total_registration_time
        )

        self.total_price_for_distance = self.get_total_price_for_distance(
            distance=distance_to_distantion, average_price=self.price_per_km
        )


class Car(Carrier):
    def __init__(self, distance_to_distantion):
        super().__init__()

        # Учитываем расход топлива и стоимость бензина
        self.fuel_flow_per_100km = 8  # 8 литров допутим на 100 км.
        self.fuel_price_per_litre = 1.5  # 1.5 за литр.
        self.fuel_flow_distance = 100  # 100км

        min_speed = 90
        max_speed = 130

        self.average_speed = self.average_speed_formula(
            min_speed=min_speed, max_speed=max_speed
        )

        self.time_to_distanation = self.get_average_time_until_destination(
            distance=distance_to_distantion, average_speed=self.average_speed
        )

        self.total_price_for_distance = self.get_total_price_for_distance_Car(
            distance=distance_to_distantion,
            fuel_flow_distance=self.fuel_flow_distance,
            fuel_flow=self.fuel_flow_per_100km,
            fuel_price_per_litre=self.fuel_price_per_litre,
        )


class Train(Carrier):
    def __init__(self, distance_to_distantion):
        super().__init__()

        default_min_speed = 91
        default_max_speed = 200

        self.average_speed = self.average_speed_formula(
            min_speed=default_min_speed, max_speed=default_max_speed
        )

        default_min_price_per_km = 0.05  # euro
        default_max_price_per_km = 0.1  # euro
        average_price_formula = lambda min_price, max_price: (min_price + max_price) / 2

        self.average_price: float = average_price_formula(
            min_price=default_min_price_per_km, max_price=default_max_price_per_km
        )

        self.time_to_distanation = self.get_average_time_until_destination(
            distance=distance_to_distantion, average_speed=self.average_speed
        )

        self.total_price_for_distance = self.get_total_price_for_distance(
            distance=distance_to_distantion, average_price=self.average_price
        )
