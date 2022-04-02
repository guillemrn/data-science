from car import Car
from account import Account
from User import User


if __name__ == "__main__":
    car = Car("ADF876", Account("Gabriela Quezada", "INE"))
    user = User("Francisco", "INE")
    print(vars(car))
    print(vars(car.driver))
    print(vars(user))