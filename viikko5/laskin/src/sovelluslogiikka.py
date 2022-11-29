class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        pass


class Summa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = 0
        self.lue_syote = lue_syote

    def suorita(self):
        self.syote = int(self.lue_syote())
        self.sovelluslogiikka.plus(self.syote, self)

    def kumoa(self):
        self.sovelluslogiikka.miinus(self.syote, 0)
        self.syote = 0


class Erotus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = 0
        self.lue_syote = lue_syote

    def suorita(self):
        self.syote = int(self.lue_syote())
        self.sovelluslogiikka.miinus(self.syote, self)

    def kumoa(self):
        self.sovelluslogiikka.plus(self.syote, 0)
        self.syote = 0

class Nollaus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
        self.edellinen = 0

    def suorita(self):
        self.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.nollaa(self)


class Kumoa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.kumoa()