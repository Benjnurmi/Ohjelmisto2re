# Moduuli 11.1
# Luokkahierarkia

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def print_info(self):
        print(f"Julkaisun nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä ):
        self.sivumäärä = sivumäärä
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)

    def print_info(self):
        super().print_info()
        print(f"Kirjan kirjoittaja: {self.kirjoittaja}")
        print(f"Kirja on {self.sivumäärä}-sivuinen")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja,):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def print_info(self):
        super().print_info()
        print(f"Lehden päätoimittaja on {self.päätoimittaja}")


julkaisu = Lehti("Aku Ankka", "Aki Hyppää")
julkaisu1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
julkaisu.print_info()
julkaisu1.print_info()









#Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
"""
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettuMatka = kuljettu_matka
    def kiihdyta(
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kuljettu_matka, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
"""
