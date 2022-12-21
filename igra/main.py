from entities import character
from errors import InvalidCommand,InvalidDataFormat

class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print('2.Create a new weapon for existing character')
        print('3.Create new object for existing character')
        print('4.print all characters')
        print('5.Delete existing character')
        print('Exit')

    def command_create_character(self, name, sex, ch_class):
        pass

    def run(self):
        menu = Menu()
        while True:  
            self.print_menu()
            choice = input("Choose a number from the menu: \n>")

            try:
                if choice == "1":                    
                    name = input("Enter the character name (alpha-numeric): ")
                    if len(name) < 4 or not name.isalpha():
                        raise InvalidDataFormat()
                    if 
                elif choice == "2":
                    pass
                elif choice == "3":
                    pass
                elif choice == "4":
                    pass
                elif choice == "5":
                    pass
                elif choice == "6":
                    pass
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
