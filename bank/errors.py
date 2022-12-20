# User
class InvalidUserData(Exception):
    def __init__(self, message = "Invalid data for user", *args: object) -> None:
        super().__init__(message, *args)

class UserNotFound(Exception):
    def __init__(self, message = "The user is not found", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyExists(Exception):
    def __init__(self, message = "User already exists", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyOwnsAccount(Exception):
    def __init__(self, message = "User already has an account", *args: object) -> None:
        super().__init__(message, *args)

# Account 
class AccountNotFound(Exception):
    def __init__(self, message = "Account not found", *args: object) -> None:
        super().__init__(message, *args)

class UnsufficientBalance(Exception):
    def __init__(self, message = "Not enough money in Balance", *args: object) -> None:
        super().__init__(message, *args)

class InvalidAccountData(Exception):
    def __init__(self, message = "Invalid account data", *args: object) -> None:
        super().__init__(message, *args)

class InvalidAccountType(Exception):
    def __init__(self, message = "Invalid account type. Try:SAVINGS, CREDIT or PAYMENT", *args: object) -> None:
        super().__init__(message, *args)

# Bank


# Menu
class InvalidMenuChoice(Exception):
    def __init__(self, message = "Enter a whole number between 1 and 7", *args: object) -> None:
        super().__init__(message, *args)
