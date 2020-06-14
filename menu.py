import notes.categories_functions
import notes.notes_functions
from colorama import init, Fore, Back, Style
init()


def cls():
    clear = "\n" * 100
    print(clear)

def menuMain():
    print('--------------')
    print('--------------')
    print(Fore.RED + '1. Wyświetl kategorie')
    print('2. Dodaj kategorię')
    print('3. Usuń kategorię')
    print('4. Wyświetl notatki')
    print('5. Dodaj notatkę')
    print('6. Usuń całkowicie notatkę')
    print(Style.RESET_ALL)
    print('--------------')
    print('--------------')

    choose = input("Podaj cyfrę z wyborem lub q żeby opuścić program")
    if choose == 'q':
        print('Koniec działania programu')
    else:
        choose = int(choose)
        if choose == 1:
            notes.categories_functions.showCategories()
        elif choose == 2:
            notes.categories_functions.addCategory()
        elif choose == 3:
            notes.categories_functions.delCategory()
        elif choose == 4:
            notes.notes_functions.showNotes()
        elif choose == 5:
            notes.notes_functions.addNote()
        elif choose == 6:
            notes.notes_functions.delNote()
        else:
            cls()
            print('Nieprawidłowy wybór!')
            menuMain()
