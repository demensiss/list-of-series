"""Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć.
W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i oceny.
Dodaj serial do spisu."""

# TODO Create unit tests in Pytest

import sys


def add_series(my_series: dict):
    while True:
        name = input("Podaj nazwę serialu, który chcesz zapisać: ").strip().title()
        try:
            rate = int(input("Podaj ocenę tego serialu (skala od 1 do 10): ").strip())
            if rate == 0:
                rate = 1
            elif rate > 10:
                rate = 10
        except ValueError as e:
            print(f"Ocena musi być liczbą!")
            continue

        my_series.update({name: rate})

        more = input("Dodać jeszcze jeden? [T]ak / [N]ie : ").upper()
        if more == 'T':
            continue
        elif more == 'N':
            break
        else:
            print('Wpisz "T", jeśli chcesz dodać kolejny serial lub "N", jeśli nie chcesz tego robić.')

    return my_series


def save_to_file(filename: str, my_series: dict):
    with open(filename, 'w') as file:
        for series, rate in my_series.items():
            file.write(f"Serial: {series}, ocena: {rate} / 10\n")


def show_series(my_series: dict):
    for title, rate in my_series.items():
        print(f"Serial: {title}, ocena: {rate} / 10")


def read_file(filename: str):
    series = {}

    with open(filename, 'r') as file:
        for line in file.readlines():
            title, rate = line.split(',')
            title = title.split(':')[1].title().strip()
            rate = int(rate.split()[1].strip())
            series.update({title: rate})

    return series


def search_series(my_series: dict):
    searched_series = input("Podaj nazwę serialu, którego szukasz: ").title().strip()

    (print(f"Ten serial otrzymał ocenę: {my_series.get(searched_series)} / 10")
     if searched_series in my_series.keys()
     else print("Nie ma takiego serialu w bazie."))


if __name__ == "__main__":
    choice = 'default'
    filename = 'series.txt'
    my_series = read_file(filename)

    while choice:
        print()
        print("1. Dodaj serial")
        print("2. Szukaj serialu")
        print("3. Pokaż wszystkie seriale")
        print("0. Zamknij program")
        print()

        choice = input("Wybierz co chcesz zrobić: ")
        print()

        if choice == '1':
            my_series = add_series(my_series)
        elif choice == '2':
            search_series(my_series)
        elif choice == '3':
            show_series(my_series)
        elif choice == '0':
            save_to_file(filename, my_series)
            sys.exit(0)
        else:
            choice = 'default'
            print("Nie ma takiej opcji. Wybierz ponownie.")
