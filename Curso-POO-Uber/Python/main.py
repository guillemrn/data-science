from car import Car
from account import Account


if __name__ == "__main__":
    car = Car("ADF876", Account("Gabriela Quezada", "INE"))
    print(vars(car))
    print(vars(car.driver))