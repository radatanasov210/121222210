from errors import InvalidAccountType
from errors import UnsufficientBalance
from errors import InvalidAccountData

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT","PAYMENT")

    def __init__(self, iban, currency, type) -> None:
        if type not in Account.ACC_TYPES:
            raise InvalidAccountType()
        try:
            currency = int(currency)
        except:
            raise InvalidAccountData()
        self.iban = iban
        self.currency = currency
        self.type = type
    def deposit(self,suma):
        try:
            suma = int(suma)
        except:
            raise InvalidAccountData()
        self.currency +=suma
    def withdraw(self,suma):
        try:
            suma = int(suma)
        except:
            raise InvalidAccountData()
        if self.currency-suma<0:
            raise UnsufficientBalance()
        else:
            self.currency -= suma
    def print_account(self):
        print(f"{self.iban}: {self.currency}, {self.type}")
