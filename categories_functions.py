from notes.connection import *
import notes.menu
from colorama import init, Fore, Back, Style
init()


def showCategories():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories")


        rows = cur.fetchall()

        row_count = cur.rowcount

        if row_count == 0:
            print(Fore.RED + 'Brak kategorii, przenoszę do menu')
            print(Style.RESET_ALL)
            notes.menu.menuMain()
        else:
            print("Kategorie:")
            for row in rows:
                print(Fore.BLUE + "{0} - {1}".format(row[0], row[1]))

            print(Style.RESET_ALL)
            znak = input('Wpisz q aby wrócić do menu lub podaj numer kategorii aby ją zmodyfikować')
            if znak == 'q':
                cls()
                notes.menu.menuMain()
            else:
                cls()
                cur = conn.cursor()
                cur.execute("SELECT * FROM categories WHERE id={0}".format(int(znak)))

                rows = cur.fetchall()
                row_count = cur.rowcount

                if row_count == 0:
                    print(Fore.RED + 'Brak kategorii o takim ID, wracam do przeglądania kategorii')
                    print(Style.RESET_ALL)
                    showCategories()
                else:
                    id = -1
                    for row in rows:
                        id = row[0]
                        print(Fore.BLUE + "Obecna nazwa kategorii - {1}".format(row[0], row[1]))
                        print(Style.RESET_ALL)

                    nazwa = input('Podaj nową nazwę kategorii lub wpisz q żeby wrócić do menu')
                    if nazwa == 'q':
                        cls()
                        notes.menu.menuMain()
                    else:
                        cls()
                        cur = conn.cursor()
                        cur.execute("UPDATE categories SET `name`='{0}' WHERE id={1}".format(nazwa, int(id)))
                        print(Fore.GREEN + 'Kategoria pomyślnie zaktualizowana!')
                        print(Style.RESET_ALL)
                        showCategories()


def addCategory():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories")

        rows = cur.fetchall()

        print("Kategorie:")
        for row in rows:
            print("{0} - {1}".format(row[0], row[1]))
        znak = input('Wpisz q aby wrócić do menu lub wpisz nazwę kategorii aby ją dodac')
        if znak == 'q':
            cls()
            notes.menu.menuMain()
        else:
            cls()
            cur.execute("INSERT INTO `categories` (`id`, `name`) VALUES (NULL, '{0}');".format(znak))
            print(Fore.GREEN + 'Kategoria pomyślnie dodana!')
            print(Style.RESET_ALL)
            showCategories()


def delCategory():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories")

        rows = cur.fetchall()

        print("Kategorie:")
        for row in rows:
            print("{0} - {1}".format(row[0], row[1]))
        znak = input('Wpisz q aby wrócić do menu lub podaj id kategorii do usunięcia')
        if znak == 'q':
            cls()
            notes.menu.menuMain()
        else:
            cls()
            cur.execute("DELETE FROM categories WHERE id={0}".format(int(znak)))
            print(Fore.GREEN + 'Kategoria pomyślnie usunięta!')
            print(Style.RESET_ALL)
            showCategories()
