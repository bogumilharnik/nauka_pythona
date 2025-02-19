import os
import csv

def wczytaj_wydatki():
    wydatki = []
    while True:
        insert = input("Podaj kwotę i kategorię w postaci: 'kwota - kategoria', np.: '25 - jedzenie'. Wpisanie 'stop' kończy: ")
        if insert == 'stop':
            break
        czesc = insert.split(" - ")
        kwota = float(czesc[0])
        kategoria = " - ".join(czesc[1:])
        wydatki.append((kwota, kategoria))
    return wydatki


def utworz_folder(sciezka):
    directory = os.path.dirname(sciezka)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Utworzono ścieżkę '{directory}'.")
        except OSError as error:
            print(f"Błąd tworzenia ścieżki '{directory}': {error}")
            return False
        return True
    
def wczytaj_plik_wydatkow():
    path_file = input("Podaj ścieżkę do pliku CSV z wydatkami: ")
    wydatki = []
    try:
        with open(path_file, 'r', newline='', encoding='utf-8') as plik_csv:
            reader = csv.reader(plik_csv)
            next(reader)
            for row in reader:
                kwota = float(row[0])
                kategoria = row[1]
                wydatki.append((kwota, kategoria))
    except FileNotFoundError as error:
        print(f"Błąd odczytu pliku: {error}")
    except ValueError as error:
        print(f"Błąd danych w pliku: {error}")
    except csv.Error as error:
        print(f"Błąd formatu pliku CSV")
    return wydatki

def dodaj_wydatki(lista_wydatkow):
    try:
        kwota = float(input("Podaj kwotę wydatku: "))
        kategoria = input("Podaj kategorię wydatku: ")
        lista_wydatkow.append((kwota, kategoria))
        print(f"Dodano nowy wydatek: {kwota} zł - {kategoria}.")
    except ValueError as error:
        print(f"Błąd danych - niewłaściwa kwota lub kategoria: {error}")
        
def edytuj_wydatek(lista_wydatkow):
    if len(lista_wydatkow) == 0:
        print("Lista wydatków jest pusta.")
        return

    for i, (kwota, kategoria) in enumerate(lista_wydatkow):
        print(f"{i + 1}. {kwota:.2f} zł - {kategoria}")

    try:
        numer = int(input("Podaj numer wydatku do edycji: ")) - 1

        if numer < 0 or numer >= len(lista_wydatkow):
            print("Błąd: Nie ma takiego numeru.")
            return

        nowa_kwota = float(input("Podaj nową kwotę: "))
        nowa_kategoria = input("Podaj nową kategorię: ")

        lista_wydatkow[numer] = (nowa_kwota, nowa_kategoria)
        print("Wydatek został zaktualizowany.")

    except ValueError:
        print("Błąd: Nieprawidłowy numer lub kwota.")
        
def usun_wydatek(lista_wydatkow):
    if len(lista_wydatkow) == 0:
        print("Lista wydatków jest pusta.")
        return

    for i, (kwota, kategoria) in enumerate(lista_wydatkow):
        print(f"{i + 1}. {kwota:.2f} zł - {kategoria}")

    try:
        numer = int(input("Podaj numer wydatku do usunięcia: ")) - 1

        if numer < 0 or numer >= len(lista_wydatkow):
            print("Błąd: Nie ma takiego numeru.")
            return

        usuniety = lista_wydatkow.pop(numer)
        print(f"Usunięto wydatek: {usuniety[0]:.2f} zł - {usuniety[1]}")

    except ValueError:
        print("Błąd: Nieprawidłowy numer.")
            
    
def save_to_txt(plik_txt, suma, srednia, max_k_w, kategorie, najdrozsza_kat):
    if not utworz_folder(plik_txt):
        return

    try:
        with open(plik_txt, 'w', encoding='utf-8') as plik:
            plik.write(f"Suma wszystkich wydatków: {suma:.2f} zł\n")
            plik.write(f"Średnia wartość wydatków: {srednia:.2f} zł\n")
            plik.write(f"Największy wydatek: {max_k_w[0]:.2f} zł (kategoria: {max_k_w[1]})\n\n")

            plik.write("Wydatki według kategorii:\n")
            for kategoria, suma in kategorie.items():
                plik.write(f"- {kategoria}: {suma:.2f} zł\n")
            
            plik.write(f"\nNajdroższa kategoria sumarycznie: {najdrozsza_kat[0]} ({najdrozsza_kat[1]:.2f} zł)\n")

        print(f"Zapisano raport do pliku '{plik_txt}'.")
    except IOError as error:
        print(f"Błąd zapisu pliku: {error}")


def save_to_csv(plik_csv, lista_wydatkow):
    if not utworz_folder(plik_csv):
        return

    try:
        with open(plik_csv, 'w', newline='', encoding='utf-8') as plik_csv_f:
            writer = csv.writer(plik_csv_f)
            writer.writerow(['Kwota', 'Kategoria'])

            for kwota, kategoria in lista_wydatkow:
                writer.writerow([kwota, kategoria])

        print(f"Zapisano dane do pliku '{plik_csv}'.")
    except IOError as error:
        print(f"Błąd zapisu pliku: {error}")
