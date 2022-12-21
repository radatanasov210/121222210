from errors import InvalidCharacterclass
class Character:
    Klas_Types = ('WARRIOR','MAGE','PRIEST','ROGUE')
    def __init__(self,name,gender,klas) -> None:
        if klas not in Character.Klas_Types:
            raise InvalidCharacterclass()
        self.name=name
        self.gender=gender
        self.klas=klas
        self.characters = []
    def print(self):
        return f"Character={self.name},{self.gender},{self.klas}"
