from notes.connection import *
import notes.menu
from colorama import init, Fore, Back, Style
from datetime import date
init()

def showNotes():
    with conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT n.`id`, n.`title`, n.`description`, n.`deadline`, n.`ended`, c.name FROM `notes` n INNER JOIN categories c ON n.category_id=c.id ORDER BY n.`deadline` ASC")

        rows = cur.fetchall()

        row_count = cur.rowcount

        if row_count == 0:
            print(Fore.RED + 'Brak notatek, przenoszę do menu')
            print(Style.RESET_ALL)
            notes.menu.menuMain()
        else:
            print("Notatki:")
            for row in rows:
                print(Fore.BLUE + "ID: {0}".format(row[0]))
                print("Tytuł: {0}".format(row[1]))
                print("Szczegóły: {0}".format(row[2]))
                print("Deadline: {0}".format(row[3]))

                napis = "tak"
                if int(row[4]) == 0:
                    napis = "nie"

                print("Wykonane: {0}".format(napis))
                print("Nazwa kategorii: {0}".format(row[5]))
                print('\n\n')
            print(Style.RESET_ALL)
            znak = input('Wpisz q aby wrócić do menu lub podaj numer notatki aby ją zmodyfikować')
            if znak == 'q':
                cls()
                notes.menu.menuMain()
            else:
                cls()
                cur = conn.cursor()
                cur.execute("SELECT n.`id`, n.`title`, n.`description`, n.`deadline`, n.`ended`, c.name FROM `notes` n INNER JOIN categories c ON n.category_id=c.id WHERE n.`id`={0}".format(int(znak)))

                rows = cur.fetchall()
                row_count = cur.rowcount

                if row_count == 0:
                    print(Fore.RED + 'Brak notatki o takim ID, przenoszę do notatek')
                    print(Style.RESET_ALL)
                    showNotes()
                else:
                    id = -1
                    for row in rows:
                        id = row[0]
                        print(Fore.BLUE + "ID: {0}".format(row[0]))
                        print("Tytuł: {0}".format(row[1]))
                        print("Szczegóły: {0}".format(row[2]))
                        print("Deadline: {0}".format(row[3]))

                        napis = "tak"
                        if int(row[4]) == 0:
                            napis = "nie"

                        print("Wykonane: {0}".format(napis))
                        print("Nazwa kategorii: {0}".format(row[5]))

                        print(Style.RESET_ALL)

                    print('--------------')
                    print(Fore.RED + '1. Zmień Tytuł')
                    print('2. Zmień Szczegóły')
                    print('3. Zmień Deadline')
                    print('4. Ustaw jako wykonane(usunie i przeniesie do pliku archiwum.txt')
                    print('5. Zmień kategorię')
                    print(Style.RESET_ALL)
                    print('--------------')

                    nazwa = input('Podaj co chcesz zmodyfikować lub wpisz q żeby wrócić do menu')
                    if nazwa == 'q':
                        cls()
                        notes.menu.menuMain()
                    else:
                        nazwa = int(nazwa)
                        if nazwa == 1:
                            cls()
                            nazwa = input('Podaj nowy tytuł notatki')
                            cur = conn.cursor()
                            cur.execute("UPDATE notes SET `title`='{0}' WHERE id={1}".format(nazwa, id))
                            print(Fore.GREEN + 'Tytuł pomyślnie zaktualizowany!')
                            print(Style.RESET_ALL)
                            showNotes()
                        elif nazwa == 2:
                            cls()
                            nazwa = input('Podaj nowe szczegóły notatki')
                            cur = conn.cursor()
                            cur.execute("UPDATE notes SET `description`='{0}' WHERE id={1}".format(nazwa, id))
                            print(Fore.GREEN + 'Szczegóły pomyślnie zaktualizowane!')
                            print(Style.RESET_ALL)
                            showNotes()
                        elif nazwa == 3:
                            cls()
                            nazwa = input('Podaj nowy deadline(w formie RRRR-MM-DD')
                            cur = conn.cursor()
                            cur.execute("UPDATE notes SET `deadline`='{0}' WHERE id={1}".format(nazwa, id))
                            print(Fore.GREEN + 'Deadline pomyślnie zaktualizowany!')
                            print(Style.RESET_ALL)
                            showNotes()
                        elif nazwa == 4:
                            cls()
                            cur = conn.cursor()
                            cur.execute("DELETE FROM notes WHERE id={1}".format(nazwa, id))
                            print(Fore.GREEN + 'Notatka usunięta i dodana do archiwum.txt!')
                            print(Style.RESET_ALL)

                            plik = open("archiwum.txt", "a+")
                            today = date.today()
                            d1 = today.strftime("%Y/%m/%d")
                            dane = "ID notatki: " + str(row[0]) + " Tytuł: " + str(row[1]) + ' Szczegóły: ' + str(row[2]) + " Deadline: " + str(row[3]) + " Nazwa kategorii: " + str(row[5]) + "  Data wykonania: " + str(d1)
                            plik.write(dane)
                            plik.close()
                            showNotes()
                        elif nazwa == 5:
                            cls()
                            cur.execute("SELECT * FROM categories")

                            rows = cur.fetchall()

                            print("Kategorie:")
                            for row in rows:
                                print("{0} - {1}".format(row[0], row[1]))

                            nazwa = input('Podaj nowy numer kategorii')
                            cur = conn.cursor()
                            cur.execute("UPDATE notes SET `category_id`={0} WHERE id={1}".format(nazwa, id))
                            print(Fore.GREEN + 'Kategoria pomyślnie zaktualizowana!')
                            print(Style.RESET_ALL)
                            showNotes()

                        else:
                            cls()
                            print(Fore.RED + 'Nieznana opcja!')
                            print(Style.RESET_ALL)
                            showNotes()


def addNote():
    with conn:
        cls()
        title = input("Podaj tytuł nowej notatki")
        description = input("Podaj szczegóły nowej notatki")
        deadline = input("Podaj deadline nowej notatki (w formie YYYY-MM-DD)")

        cur.execute("SELECT * FROM categories")

        rows = cur.fetchall()

        print("Kategorie:")
        for row in rows:
            print("{0} - {1}".format(row[0], row[1]))

        category = input('Podaj numer kategorii dla nowej notatki')

        cls()
        cur.execute("INSERT INTO `notes` (`id`, `title`, `description`, `deadline`, `ended`, `category_id`) VALUES (NULL, '{0}', '{1}', '{2}', '0', '{3}');".format(title, description, deadline, category))
        print(Fore.GREEN + 'Notatka pomyślnie dodana!')
        print(Style.RESET_ALL)
        showNotes()


def delNote():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM notes")

        rows = cur.fetchall()

        print("Notatki:")
        for row in rows:
            print("{0} - {1} - {2}".format(row[0], row[1], row[2]))
        znak = input('Wpisz q aby wrócić do menu lub podaj id notatki do usunięcia')
        if znak == 'q':
            cls()
            notes.menu.menuMain()
        else:
            cls()
            cur.execute("DELETE FROM notes WHERE id={0}".format(int(znak)))
            print(Fore.GREEN + 'Kategoria pomyślnie usunięta!')
            print(Style.RESET_ALL)

            showNotes()
