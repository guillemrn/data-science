from account import Account


class User(Account):
    def __init__(self, name, document):
        super().__init__(name, document)
        # self.id = id
        # self.license = license
        # self.driver = driver
        # self.passenger = passenger