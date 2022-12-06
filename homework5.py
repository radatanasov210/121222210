import random
class JungleAnimal:
    def __init__(self,name,age,sound):
        self.name=name
        self.age=age
        self.sound=sound
    def make_sound(self):
        print(f'{self.name} says {self.sound}!')
class InvalidParameterError(Exception):
    def __init__(self, invalid):
        message = f'Invalid parameter:{invalid}'
        super().__init__(message)
class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__('age')
class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        super().__init__('sound')
class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age>15:
            self.invalid_print()
            raise InvalidAgeError()
        if sound.count('r')<2 :
            self.invalid_print()
            raise InvalidSoundError()
    def print(self):
        print(f'Jaguar {self.name} {self.age} {self.sound}')
    def invalid_print(self):
        print(f'{self.name} {self.age} {self.sound}', end=' ')
    def daily_task(self,animals):
        for i in range(0,len(animals)-1):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                print(f'{self.name} the Jaguar hunted down {animals[i].name} the {type(animals[i]).__name__}')
                animals.pop(i)
                break
class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age >10:
            self.invalid_print()
            raise InvalidAgeError()
        if self.sound.count('e')== 0:
            self.invalid_print()
            raise InvalidSoundError()
    def print(self):
        print(f'Lemur {self.name} {self.age} {self.sound}')
    def invalid_print(self):
        print(f'{self.name} {self.age} {self.sound}', end=' ')
    def daily_task(self, fruits):
        if fruits >= 10:
            print(f'{self.name} the Lemur ate a full meal of 10 fruits')
            return fruits-10
        elif fruits <10 and fruits>0:
            print(f'{self.name} the Lemur could only find {fruits} fruits')
            return 0
        else:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0
class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age >10:
            self.invalid_print()
            raise InvalidAgeError()
        if self.sound.count('e') == 0:
            self.invalid_print()
            raise InvalidSoundError()
    def print(self):
        print(f'Human {self.name} {self.age} {self.sound} ')
    def invalid_print(self):
        print(f'{self.name} {self.age} {self.sound}', end=' ')
    def daily_task(self, animals, buildings):
        for i in range(0,len(animals)-1):
            if type(animals[i]) == Human:
                if i!=0 and i!=len(animals)-1:
                    if type(animals[i + 1]) == Human and type(animals[i - 1]) == Human:
                        typo = input('Suzdai sgrada')
                        buildings.append(Building(typo))
                elif i == 0:
                    if type(animals[i + 1]) == Human:
                        typo = input('Suzdai sgrada:')
                        buildings.append(Building(typo))
                elif i == len(animals) - 1:
                    if type(animals[i - 1]) == Human:
                        typo = input('Suzdai sgrada:')
                        buildings.append(Building(typo))
class Building:
    def __init__(self,typo):
        self.typo=typo
fruits = 100
animals =[]
buildings = []
names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]
sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]
for i in range(0,102):
    a = random.randint(0,9)
    print(a,end=' ')
    try:

        if a<4:
            animals.append(Lemur(str(names[random.randrange(len(names))]),int(random.randint(7,20)),str(sounds[random.randrange(len(sounds))])))
        elif a>3 and a<8:
            animals.append(Jaguar(str(names[random.randrange(len(names))]),int(random.randint(7,20)),str(sounds[random.randrange(len(sounds))])))
        elif a>7 and a<10:
            animals.append(Human(str(names[random.randrange(len(names))]),int(random.randint(7,20)),str(sounds[random.randrange(len(sounds))])))
    except InvalidSoundError as ex:
        print(ex)
    except InvalidAgeError as ex:
        print(ex)
print(f"The jungle now has {len(animals)} animals")
for anim in animals:
    if type(anim) == Lemur:
        anim.daily_task(fruits)
    elif type(anim) == Jaguar:
        anim.daily_task(animals)
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)
print(f"The jungle now has {len(animals)} animals")
for i in range(len(animals)):
    print(animals[i])
for i in range(len(buildings)):
    buildings[i].print()
