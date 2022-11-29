from sovelluslogiikka import Sovelluslogiikka

class Komentotehdas:
    def __init__(self, io):
        self.io = io
        self.sovelluslogiikka = Sovelluslogiikka()

        self.komennot = {
            "1": self.sovelluslogiikka.plus(self.io),
            "2": self.sovelluslogiikka.miinus(self.io),
            "3": self.sovelluslogiikka.nollaa(self.io),
            "4": self.sovelluslogiikka.aseta_arvo(self.io)
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]

        return "Tuntematon komento"
