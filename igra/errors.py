class Characternotfound(Exception):
    def __init__(self,message='Character not found', *args: object) -> None:
        super().__init__(message,*args)
class InvalidCommand(Exception):
    def __init__(self,message='Invalid Command', *args: object) -> None:
        super().__init__(message,*args)
class InvalidDataFormat(Exception):
    def __init__(self,message='Invalid Data Format', *args: object) -> None:
        super().__init__(message,*args)
class CharacterExist(Exception):
    def __init__(self,message='Character already exist', *args: object) -> None:
        super().__init__(message,*args)
class InvalidCharacterclass(Exception):
    def __init__(self,message='Invalid character class', *args: object) -> None:
        super().__init__(message,*args)

