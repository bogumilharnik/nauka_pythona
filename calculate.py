

def lista_kategorii(lista_wydatkow):
    kategorie = {}
    for kwota, kategoria in lista_wydatkow:
        if kategoria not in kategorie:
            kategorie[kategoria] = 0
        kategorie[kategoria] += kwota
    return kategorie

def suma_wydatkow(lista_wydatkow):
    suma_wyd = sum(kwota for kwota, _ in lista_wydatkow)
    return suma_wyd

def srednia_wydatkow(lista_wydatkow):
    srednia = suma_wydatkow(lista_wydatkow) / len(lista_wydatkow)
    return srednia

def max_wydatek(lista_wydatkow):
    max_w = max(kwota for kwota, _ in lista_wydatkow)
    return max_w

def max_wydatek_kat(lista_wydatkow):
    max_w_k = max(lista_wydatkow, key=lambda x: x[0])
    return max_w_k

def najdrozsza_kategoria(kategorie):
    max_kategoria = max(kategorie.items(), key=lambda x: x[1])
    return max_kategoria