class Vehicle:
    def __init__(self, color: str, model: str, year: str, vin: int):
        self.color = color
        self.model = model
        self.year = year
        self.__vin = vin

    def get_type(self) -> None:
        pass

    @property
    def vin(self) -> int:
        return self.__vin


class Car(Vehicle):
    def __init__(self, color: str, model: str, year: str, doors: int, vin: int) -> None:
        super().__init__(color, model, year, vin)
        self.doors = doors

    def get_type(self) -> str:
        return 'Car'


class Truck(Car):
    def __init__(self, color, model, year, doors, vin):
        super().__init__(color, model, year, doors, vin)

    def get_type(self) -> str:
        return 'Truck'


class Airplane:
    def __init__(self, color: str, model: str, year: str, doors: int) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.doors = doors

    @staticmethod
    def get_type() -> str:
        return 'Airplane'

    def fly(self) -> None:
        pass


class Boeing(Airplane):
    def fly(self) -> str:
        return "Boeing is flying high."


class Airbus(Airplane):
    def fly(self) -> str:
        return "Airbus is flying across the continents."


if __name__ == '__main__':

    car = Car('red', 'ЛАМБА', '2019', 5, 1231231)
    truck = Truck('blue-white', 'УАЗ', '2019', 5, 123123)
    boeing = Boeing("Boeing", "737", '2000', 4)
    airbus = Airbus("Airbus", "A320", '2013', 4)
    vehicles = [car, truck, boeing, airbus]

    for i in vehicles:
        if isinstance(i, Car):
            print(i.get_type(), i.vin)
        else:
            print(i.fly(), i.get_type())
