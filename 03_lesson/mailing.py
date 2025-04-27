from address import Address


class Mailing:
    def __init__(self, track, to_address, from_address, cost):
        self.track = track
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost

    def __str__(self):
        print(f"Debug: to_address = {self.to_address}")  # Отладочный вывод
        print(f"Debug: from_address = {self.from_address}")  # Отладочный вывод

        return f"{self.track} Отправление из {self.to_address} в {self.from_address}. Стоимость: {self.cost} рублей."
