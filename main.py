#  ------------------------------------------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------------------------------------------
# 
# # # # # # Zadania Chat_GPT

# # # Plan na start – Poziom 1 (Rozgrzewka)

# # # # 1️⃣ Dodawanie dwóch liczb
# # # # Plan:

# # # #     Poproś użytkownika o pierwszą liczbę.
# # # #     Poproś o drugą liczbę.
# # # #     Zamień obie na int.
# # # #     Dodaj je do siebie.
# # # #     Wyświetl wynik.

# # # liczba_pierwsza = int(input("podaj pierwszą liczbę: "))
# # # liczba_druga = int(input("podaj drugą liczbę: "))

# # # wynik = liczba_pierwsza + liczba_druga

# # # print(f"Wynik dodawania liczb to: {wynik}")


# # # # 2️⃣ Powielenie tekstu
# # # # Plan:

# # # #     Poproś użytkownika o słowo.
# # # #     Poproś o liczbę n.
# # # #     Powiel słowo n razy.
# # # #     Wyświetl wynik.

# # # txt = input("Podaj tekst do powielenia: ")

# # # ile_razy = int(input("Podaj ile razy go powielić: "))

# # # wynik = txt * ile_razy

# # # print(f"Tekst powielony {ile_razy} to: {wynik}")


# # # # 3️⃣ Ostatnia cyfra liczby
# # # # Plan:

# # # #     Poproś użytkownika o liczbę całkowitą.
# # # #     Zamień na int.
# # # #     Pobierz ostatnią cyfrę (podpowiedź: liczba % 10).
# # # #     Wyświetl ostatnią cyfrę.

# # # liczba=int(input("Podaj dowolną liczbę całkowitą: "))

# # # print(f"{liczba}")
# # # tekst = str(liczba)

# # # print(f"Ostatnia cyfra liczby {liczba} to: {tekst[-1]}")



# # # # 4️⃣ Długość tekstu
# # # # Plan:

# # # #     Poproś użytkownika o tekst.
# # # #     Użyj len() – podpowiedź 😉.
# # # #     Wyświetl długość.

# # # input_txt = input("Podaj tekst do obliczenia: ")

# # # wynik = input_txt.__len__()

# # # print(f"długość tekstu to: {wynik}")

#  ------------------------------------------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------------------------------------------

# # # 🧑‍💻 Poziom 2 – Zestaw zadań (Operacje na Tekście i Przetwarzanie Danych)
# # # 1️⃣ Pierwsza i ostatnia litera
# # # Plan (Twoja rozpiska – spróbuj sam):

# # #     Poproś użytkownika o tekst.
# # #     Pobierz pierwszą literę.
# # #     Pobierz ostatnią literę.
# # #     Wyświetl obie litery.

# # text = str(input("Podaj tekst niekoniecznie długi): "))


# # if len(text) == 0:
# #     print(f"Nie wprowadzono żadnego tekstu")
# # else:
# #     first_let = text[0]
# #     last_let = text[-1]
# #     print(f"Pierwsza litera to: {first_let}, a ostatnia to: {last_let} .")


# # # 2️⃣ Wycinanie fragmentu tekstu
# # # Plan:

# # #     Poproś użytkownika o tekst.
# # #     Poproś o dwie liczby a i b (początek i koniec fragmentu).
# # #     Wypisz fragment tekstu od a do b (włącznie).
# # # Podpowiedź: Indeksowanie tekstu tekst[a:b+1].

# # text_2 = str(input("Podaj tekst niekoniecznie długi): "))
# # fragm_a = int(input("Podaj liczbę jako początek fragmentu: "))
# # fragm_b = int(input("Podaj liczbę jako koniec fragmentu: "))

# # if fragm_a <= 0 or fragm_b <= 0 or fragm_a > fragm_b or fragm_b >= len(text_2):
# #     print(f"Dolna granica zakresu nie może być większa od górnej ani żadne z nich nie może być równe 0")
# # else:
# #     fragm = text_2[fragm_a:fragm_b+1]
# #     print(f"Fragment tekstu o który chodzi to: {fragm}. ")


# # # 3️⃣ Podmiana litery 'a' na '@'
# # # Plan:

# # #     Poproś użytkownika o tekst.
# # #     Zamień każde a na @.
# # #     Wyświetl wynik.

# # # Podpowiedź: Metoda .replace().

# # text_3 = str(input("Podaj tekst niekoniecznie długi): "))


# # input_a = str(input("Podaj co zamienić: "))
# # input_b = str(input("Podaj na co zamienić: "))

# # if input_a == "":
# #     print(f"Nie podano znaku czego szukać do zamiany")
# # else:
# #     wynik = text_3.replace(input_a,input_b)
# #     print(f"Tekst oryginalny to:\n\n {text_3}, a tekst zmieniony to:\n\n {wynik}.")

#  ------------------------------------------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------------------------------------------

# # 🧑‍💻 Poziom 3 – Zestaw zadań (Pętle i działania na liczbach)

# # Tutaj wprowadzą się pętle i sumowanie, liczenie, mnożenie, czyli rzeczy, które w programowaniu pojawiają się bardzo często.
# # 1️⃣ Wypisz liczby od 1 do n
# # Plan:

# #     Poproś użytkownika o liczbę n.
# #     Użyj pętli for, żeby wypisać liczby od 1 do n.

# liczba = int(input("Podaj liczbę: "))

# for i in range(1,liczba+1):
#     print(i)



# # 2️⃣ Suma liczb od 1 do n
# # Plan:

# #     Poproś użytkownika o liczbę n.
# #     Oblicz sumę liczb od 1 do n (1 + 2 + 3 + ... + n).
# #     Użyj pętli lub wzoru.

# wynik = 0
# liczba_2 = int(input("Podaj liczbę: "))

# for i in range(1,liczba_2+1):
#     wynik += i

# print(f"Wynik sumowania to: {wynik}.")


# # 3️⃣ Tabliczka mnożenia dla liczby
# # Plan:

# #     Poproś użytkownika o liczbę n.
# #     Wypisz tabliczkę mnożenia dla tej liczby od 1 do 10 (np. n * 1, n * 2, ...).

# wynik_2 = 0
# liczba_3 = int(input("Podaj liczbę: "))

# for i in range(1, 11):
#     mnozenie = liczba_3 * i
#     print(f"Wynik mnożenia {liczba_3} * {i} to: {liczba_3 * i}")
    
# # Zrób sumę liczb parzystych od 1 do n.

# wynik = 0
# liczba_n = int(input("Podaj liczbę górnego zakresu: "))

# for i in range(1,liczba_n+1):
#     if i % 2 == 0:
#         wynik += i
#         print(f"Wynik dodawania przechodząc przez pętlę to : {wynik}\n\n")

# print(f"Wynik dodawania to: {wynik}")


# # Zrób tabliczkę mnożenia, ale dla dwóch liczb naraz (np. użytkownik podaje a i b, a Ty wypisujesz tabliczkę mnożenia a i b obok siebie).

# wynik_1 = 0
# wynik_2 = 0

# liczba_a = int(input("Podaj pierwszą liczbę: "))
# liczba_b = int(input("Podaj drugą liczbę: "))

# for i in range(1, 11):
#     wynik_1 = liczba_a * i
#     wynik_2 = liczba_b * i
#     print(f"Wynik to: {liczba_a}*{i} = {wynik_1}, | \t {liczba_b}*{i} = {wynik_2}\n")


#  ------------------------------------------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------------------------------------------


# 🧑‍💻 Zestaw zadań – Pętle i liczby (Etap 2)
# 1️⃣ Liczby nieparzyste od 1 do n
# Cel:

#     Poproś użytkownika o n.
#     Wypisz liczby nieparzyste od 1 do n.

# Podpowiedź:

#     Liczby nieparzyste to te, które przy dzieleniu przez 2 mają resztę 1:

#     if i % 2 == 1

# liczba = int(input("Podaj liczbę do sprawdzenia: "))

# for i in range(1, liczba+1):
#     if i % 2 == 1:
#         print(i)


# 2️⃣ Silnia (n!)
# Cel:

#     Poproś użytkownika o n.
#     Oblicz silnię n! (czyli 1 * 2 * 3 * ... * n).
# Podpowiedź:

#     n = 5 → 5! = 1 * 2 * 3 * 4 * 5 = 120
#     Potrzebujesz pętli for i mnożenia zamiast dodawania.

# silnia = 1
# liczba_2 = int(input("Podaj liczbę dla silni: "))

# for i in range(1,liczba_2+1):
#     silnia *= i
#     print(f"Silnia dla liczby {liczba_2} wynosi: {silnia}.")

# 3️⃣ Suma cyfr liczby
# Cel:

#     Poproś użytkownika o liczbę np. 1234.
#     Oblicz sumę jej cyfr: 1 + 2 + 3 + 4 = 10.

# Podpowiedź:

#     Zamień liczbę na tekst: str(liczba)
#     Przejdź pętlą po każdej cyfrze w tekście.
#     Zamień każdą cyfrę na int() i dodaj do sumy.

# liczba_3 = int(input("Podaj liczbę, z której chcesz zsumować cyfry: "))

# suma = 0

# txt = str(liczba_3)

# print(type(txt))
# print(txt)

# for i in txt:
#     print(i)
#     suma += int(i)

# print(f"Suma wszystkich cyfr wynosi: {suma}")


# 4️⃣ Największa liczba
# Cel:

#     Poproś użytkownika o podanie 5 liczb (jedna po drugiej).
#     Wypisz największą z nich.

# Podpowiedź:

#     Na początku ustaw np. maksymalna = None albo maksymalna = -float('inf').
#     Porównuj każdą kolejną liczbę z maksymalna.
#     Jeśli liczba jest większa – podmień maksymalna.


# wynik = []

# for i in range(5):
#     liczba = int(input(f"Podaj liczbę do zgadnięcia: {i} / 5: "))
#     wynik.append(liczba)
    
# print(f"Największa liczba to: {max(wynik)}")





# 5️⃣ Odgadnij liczbę – mini gra
# Cel:

#     Wylosuj liczbę z zakresu od 1 do 10 (później nauczymy się, jak losować, ale na razie przyjmijmy np. sekretna_liczba = 7).
#     Poproś użytkownika o odgadywanie liczby.
#     Dopóki nie poda dobrej – proś go dalej (użyj while).

# Podpowiedź:

#     Pętla while działa tak długo, jak spełniony jest warunek.
#     Przykład while:

#     liczba = 0
#     while liczba != 5:
#         liczba = int(input("Zgadnij liczbę: "))
#     print("Brawo!")

# import random
# liczba = None
# licznik_prob = 0

# liczba_losowana = random.randint(1, 20)

# while liczba != liczba_losowana:
#     liczba = int(input(f"Podaj liczbę do zgadnięcia z zakresu od 1 do 20: "))
#     licznik_prob += 1
#     if liczba > liczba_losowana:
#         print(f"Liczba jest za duża. ")
#     elif liczba < liczba_losowana:
#         print(f"Liczba jest za mała. ")
    

# print(f"To właściwa liczba: {liczba}. Odgadłeś w tylu próbach: {licznik_prob}")


### Obliczanie średniej ocen dla ucznia ###

# oceny = []

# while True:
#     ocena = int(input("Podaj ocenę (wpisz 0, aby zakończyć): "))
#     if ocena == 0:
#         break  # Przerywa pętlę, gdy wpiszesz 0
#     oceny.append(ocena)

# print(f"Twoje oceny: {oceny}")

# if len(oceny) >= 0:  # Sprawdzamy, czy nie jest pusta
#     srednia = sum(oceny) / len(oceny)
#     print(f"Średnia ocen to: {srednia:.2f}")
# else:
#     print("Nie podano żadnych ocen.")
    

# 🧑‍💻 2️⃣ Największa i najmniejsza liczba z listy
# 🎯 Cel:

#     Użytkownik podaje dowolną liczbę liczb całkowitych.
#     Wpisuje je jedna po drugiej.
#     Kończy wpisywanie, gdy poda 0.
#     Program wypisuje największą i najmniejszą liczbę z listy.    

# liczby = []

# while True:
#     liczba = int(input("Podaj liczby: \"wciśnięcie 0 zatrzymuje program\"  "))
#     if liczba == 0:
#         break
#     liczby.append(liczba)
    
# if len(liczby) == 0:
#     print(f"Lista jest pusta")
# else:
#     print(f"Największa podana liczba to: {max(liczby)}, a najmniejsze liczba to {min(liczby)}")
    

# 🧑‍💻 Zadanie 3️⃣ – Parzyste i nieparzyste – rozdzielenie
# 🎯 Cel:

#     Użytkownik podaje 10 liczb całkowitych (np. w pętli).
#     Podziel je na dwie listy:
#         Liczby parzyste.
#         Liczby nieparzyste.
#     Wypisz obie listy na końcu.


# parzyste = []
# nieparzyste = []

# for i in range(1,11):
#     liczba = int(input(f"Podaj 10 liczb {i}/10 : "))
#     if liczba % 2 == 0:
#         parzyste.append(liczba)
#     else:
#         nieparzyste.append(liczba)
# print(f"Lista z parzystymi to: {parzyste}")
# print(f"Lista z nieparzystymi to: {nieparzyste}")

# 🧑‍💻 4️⃣ Wyszukiwanie w liście – zadanie
# 🎯 Cel:

#     Użytkownik podaje dowolną liczbę imion (np. koniec kończy podawanie).
#     Po zakończeniu wpisywania:
#         Program pyta: „Jakie imię mam wyszukać?”.
#         Sprawdza, czy to imię jest na liście.
#         Wypisuje odpowiedź:
#             ✅ „Imię znajduje się na liście!”
#             ❌ „Imienia nie ma na liście.”
            
# lista_imion = []

# while True:
#     imie = input("Podaj swoje imiona: (aby zakończyć wpisz \"koniec\")")
    
#     if imie == "koniec":
#         break
#     lista_imion.append(imie)
# print(f"Oto lista imion: {lista_imion}")

# szukane_imie = input("Podaj szukane imię: ")

# if szukane_imie in lista_imion:
#     print(f"Imię {szukane_imie} jest na liście")
# else:
#     print(f"Szukasz imienia {szukane_imie}, ale lista go nie zawiera")



# 🧑‍💻 5️⃣ Mini rejestr wydatków – Zadanie
# 🎯 Cel:

#     Twórz listę wydatków (każdy wydatek to liczba – np. 10, 200, 15.5).
#     Użytkownik podaje kolejne wydatki – dopóki nie wpisze stop.
#     Gdy wpisze stop:
#         Wypisz sumę wydatków.
#         Wypisz średni wydatek.
#         Wypisz największy wydatek.

# lista_wydatkow = []

# while True:
#     wydatki = input("Podaj kwoty wydatków: (\"stop\" kończy wprowadzanie)")

#     if wydatki == 'stop':
#         break
#     wydatki = float(wydatki)
#     lista_wydatkow.append(wydatki)
    
#     print(lista_wydatkow)
# if len(lista_wydatkow) == 0:
#     print(f"Nie można wykonać obliczeń - lista jest pusta")
# else:
#     suma_wydatkow = sum(lista_wydatkow)

#     srednia_wydatkow = suma_wydatkow / len(lista_wydatkow)
        
#     print(f"Suma wydatków to: {suma_wydatkow:.2f}")
#     print(f"Największy wydatek to: {max(lista_wydatkow)}")
#     print(f"Średnia wydatków to: {srednia_wydatkow:.2f}")

# 🚀 Pierwsze „poważniejsze” zadanie – Rejestr wydatków z funkcjami
# 🎯 Cel programu:

#     Użytkownik wpisuje wydatki – tak jak robiłeś wcześniej.
#     Program ma funkcje do:
#         wczytywania wydatków,
#         obliczania sumy,
#         znajdowania największego i najmniejszego wydatku,
#         obliczania średniej wydatków.
#     Na końcu wszystko się ładnie wyświetla.

# def wczytaj_wydatki():
#     lista_wydatkow = []
#     while True:
#         wydatki = input("Podaj swoje wydatki: ")
#         if wydatki == 'stop':
#             break
#         lista_wydatkow.append(float(wydatki))
#     return lista_wydatkow

# moja_lista = wczytaj_wydatki()

# print(f"Twoja lista wydatków: {moja_lista}")

# def suma_wydatkow():
#     suma = sum(moja_lista)
#     return suma

# def najwiekszy():
#     max_wydatek = max(moja_lista)
#     return max_wydatek

# def najmniejszy():
#     max_wydatek = min(moja_lista)
#     return max_wydatek

# def srednia_wydatkow():
#     srednia = sum(moja_lista) / len(moja_lista)
#     return srednia

# print(f"Suma wydatków wynosi: {suma_wydatkow():.2f}")
# print(f"Największy wydatek to: {najwiekszy():.2f}")
# print(f"Najmniejszy wydatek to: {najmniejszy():.2f}")
# print(f"Średnia wydatków to: {srednia_wydatkow():.2f}")

# 🧑‍💻 Zadanie: Rejestr wydatków z kategoriami
# 🎯 Cel programu:

#     Użytkownik podaje wydatki z kategorią (np. 50 jedzenie, 120 transport).
#     Wydatki są grupowane według kategorii.
#     Program ma funkcje, które:
#         Wczytują wydatki od użytkownika.
#         Sumują wszystkie wydatki.
#         Sumują wydatki dla każdej kategorii osobno.
#         Podają największy wydatek i jego kategorię.
#         Podają średnią wartość wydatków.
#     Na koniec program wyświetla:
#         Suma wszystkich wydatków.
#         Średni wydatek.
#         Największy wydatek + kategoria.
#         Wydatki pogrupowane według kategorii.

from file_operations import *
from calculate import *


# Main script
# lista_wydatkow = wczytaj_wydatki()

lista_wydatkow = wczytaj_plik_wydatkow()


while True:  
    print("1. Wczytaj wydatki z pliku")
    print("2. Dodaj wydatek")
    print("3. Edytuj wydatek")
    print("4. Usuń wydatek")
    print("5. Pokaż raport")
    print("6. Zapisz raport do TXT")
    print("7. Zapisz wydatki do CSV")
    print("0. Wyjście")

    wybor = input("Wybierz opcję: ")
    
    if wybor == '1':
        # wywołaj funkcję do wczytania pliku
        lista_wydatkow = wczytaj_plik_wydatkow()
        
    elif wybor == '2':
        # wywołaj funkcję do dodawania wydatku
        dodaj_wydatki(lista_wydatkow)
    
    elif wybor == '3':
        # wywołaj funkcję do edycji wydatku
        edytuj_wydatek(lista_wydatkow)
    
    elif wybor == '4':
        # wywołaj funkcję do usunięcia wydatku
        usun_wydatek(lista_wydatkow)
    
    elif wybor == '5':
        suma = suma_wydatkow(lista_wydatkow)
        srednia = srednia_wydatkow(lista_wydatkow)
        max_wyd = max_wydatek_kat(lista_wydatkow)  # <- ważne: max_wydatek_KAT !
        kategorie = lista_kategorii(lista_wydatkow)
        najdrozsza_kat = najdrozsza_kategoria(kategorie)

        print(f"Suma: {suma:.2f} zł")
        print(f"Średnia: {srednia:.2f} zł")
        print(f"Największy wydatek: {max_wyd[0]:.2f} zł - {max_wyd[1]}")
        print("Wydatki wg kategorii:")
        for kategoria, suma in kategorie.items():
            print(f"- {kategoria}: {suma:.2f} zł")

        print(f"Najdroższa kategoria: {najdrozsza_kat[0]} ({najdrozsza_kat[1]:.2f} zł)")


    
    elif wybor == '6':
        suma = suma_wydatkow(lista_wydatkow)
        srednia = srednia_wydatkow(lista_wydatkow)
        max_wyd = max_wydatek_kat(lista_wydatkow)  # <- to samo tutaj!
        kategorie = lista_kategorii(lista_wydatkow)
        najdrozsza_kat = najdrozsza_kategoria(kategorie)

        print(f"Suma: {suma:.2f} zł")
        print(f"Średnia: {srednia:.2f} zł")
        print(f"Największy wydatek: {max_wyd[0]:.2f} zł - {max_wyd[1]}")
        print("Wydatki wg kategorii:")
        for kategoria, suma in kategorie.items():
            print(f"- {kategoria}: {suma:.2f} zł")

        print(f"Najdroższa kategoria: {najdrozsza_kat[0]} ({najdrozsza_kat[1]:.2f} zł)")
        save_to_txt(suma, srednia, max_wyd, kategorie, najdrozsza_kat)
        
    
    elif wybor == '7':
        # zapisz wydatki do csv
        suma = suma_wydatkow(lista_wydatkow)
        srednia = srednia_wydatkow(lista_wydatkow)
        max_wyd = max_wydatek(lista_wydatkow)
        kategorie = lista_kategorii(lista_wydatkow)
        najdrozsza_kat = najdrozsza_kategoria(lista_wydatkow)

        print(f"Suma: {suma:.2f} zł")
        print(f"Średnia: {srednia:.2f} zł")
        print(f"Największy wydatek: {max_wydat[0]:.2f} zł - {max_wydat[1]}")
        print("Wydatki wg kategorii:")
        for kategoria, suma in kategorie.items():
            print(f"- {kategoria}: {suma:.2f} zł")

        print(f"Najdroższa kategoria: {najdrozsza_kat[0]} ({najdrozsza_kat[1]:.2f} zł)")
        save_to_csv(lista_wydatkow)
    
    elif wybor == '0':  # Wyjście – kończymy pętlę
        print("Kończę program.")
        break

    else:
        print("Nie ma takiej opcji, spróbuj ponownie.")
    

if len(lista_wydatkow) == 0:
    print("Nie wczytano żadnych wydatków - plik jest pusty lub go nie ma.")
    exit()
else:
    kategorie = lista_kategorii(lista_wydatkow)
    suma = suma_wydatkow(lista_wydatkow)
    srednia = srednia_wydatkow(lista_wydatkow)
    max_wyd = max_wydatek(lista_wydatkow)
    max_k_w = max_wydatek_kat(lista_wydatkow)
    najdrozsza_kat = najdrozsza_kategoria(kategorie)

print(f"Suma wszystkich wydatków: {suma:.2f}")
print(f"Srednia wydatków to: {srednia:.2f}.")
print(f"Największy z wydatków to: {max_wyd:.2f}.")
print(f"Twoja lista wydatków:")
for kwota, kategoria in lista_wydatkow:
    print(f"- {kwota:.1f}: {kategoria}")

print("Wydatki według kategorii:")
for kategoria, suma in kategorie.items():
    print(f"- {kategoria}: {suma:.2f}")

print(f"Najdroższa kategoria sumarycznie: {najdrozsza_kat[0]} ({najdrozsza_kat[1]:.2f})")

plik_txt = input("Podaj pełną ścieżkę do pliku TXT (z rozszerzeniem .txt): ")
plik_csv = input("Podaj pełną ścieżkę do pliku CSV (z rozszerzeniem .csv): ")

save_to_txt(plik_txt, suma, srednia, max_k_w, kategorie, najdrozsza_kat)
save_to_csv(plik_csv, lista_wydatkow)