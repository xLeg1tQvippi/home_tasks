if __name__ == "__main__":
    from transport_4 import Plane
    from transport_4 import Car
    from transport_4 import Train
    from transport_4 import Carrier

    dash = "-"

    carrier = Carrier()
    currency = carrier.currency
    cities_and_distances = carrier.get_countries()
    print(dash * 20)
    print("Travelling by Plane:")
    print(dash * 20)
    for k, v in cities_and_distances.items():
        print(
            f"{k} - Часы: {round(Plane(v).total_time_to_distanation, 2)}h",
            f"Цена: {round(Plane(v).total_price_for_distance, 2)} {currency}",
        )
    print(dash * 20)
    print("Travelling by Car:")
    print(dash * 20)
    for k, v in cities_and_distances.items():
        print(
            f"{k} - Часы {round(Car(v).time_to_distanation, 2)}",
            f"Цена: {round(Car(v).total_price_for_distance, 2)} {currency}",
        )
    print(dash * 20)
    print("Travelling by Train:")
    print(dash * 20)
    for k, v in cities_and_distances.items():
        print(
            f"{k} - Часы {round(Train(v).time_to_distanation, 2)}",
            f"Цена: {round(Train(v).total_price_for_distance, 2)} {currency}",
        )
    print(dash * 20)
