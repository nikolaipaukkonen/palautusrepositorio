from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return len(self.ostoslista)
        
    def hinta(self):
        hinta = 0
        for ostos in self.ostoslista:
            hinta += ostos.hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self.ostoslista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoslista