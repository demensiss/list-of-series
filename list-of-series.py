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
        next = int(input("Dodać jeszcze jeden? \n Y = 1 / N = 0: "))
    return my_series

def create_lists(my_series):
    with open('series.txt', 'w') as file:
        file.write('List of watched series: \n')
        for series, rate in my_series.items():
            file.write(f"Serial: {series}, ocena: {rate} / 10.\n")
    file.close()
    return file

def show_series():
    file = open('series.txt', 'r')
    for line in file.readlines():
        print(line)
    file.close()

def search_series(my_series):
    searched_series = input("Podaj nazwę serialu, którego szukasz: ")
    print(f"Ten serial otrzymał ocenę: {my_series[searched_series]} / 10")

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



