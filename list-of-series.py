"""Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć.
W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i oceny.
Dodaj serial do spisu."""

my_series = {}
choice = -1


def add_series():
    next = -1
    while next != 0:
        name = input("Podaj nazwę serialu, który chcesz zapisać: ")
        rating = input("Podaj ocenę tego serialu (skala od 1 do 10): ")
        my_series[name] = int(rating)
        try:
            next = int(input("Dodać jeszcze jeden? \n Y = 1 / N = 0: "))
        except ValueError:
            print("Wpisz 1 jeśli chcesz dodać kolejny serial lub 0 jeśli nie chcesz tego robić.")
    return my_series


def create_lists(my_series):
    with open('series.txt', 'a') as file:
        for series, rate in my_series.items():
            file.write(f"Serial: {series}, ocena: {rate} / 10.\n")
    return file


def show_series():
    try:
        file = open('series.txt', 'r')
        for line in file.readlines():
            print(line, end="")
    finally:
        file.close()


def search_series():
    series = ""
    my_series = {}
    searched_series = input("Podaj nazwę serialu, którego szukasz: ")
    try:
        file = open('series.txt', 'r')
        for line in file.readlines():
            len_line = len(line)
            series = line[7:(len_line-17)]
            rate = line[-8]
            if rate == "0":
                rate = "1" + rate
            my_series[series] = rate
    finally:
        file.close()

    for serial in my_series:
        if serial == searched_series:
            print(f"Ten serial otrzymał ocenę: {my_series[series]} / 10")
        else:
            print("Nie znaleziono serialu.")


while choice != 0:
    print()
    print("1. Dodaj serial")
    print("2. Szukaj serialu")
    print("3. Pokaż wszystkie seriale")
    print("0. Zamknij program")

    choice = int(input("Wybierz co chcesz zrobić: "))

    if choice == 1:
        create_lists(add_series())
    elif choice == 2:
        search_series()
    elif choice == 3:
        show_series()
    else:
        print("Nie ma takiej opcji. Wybierz ponownie.")
