from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self.ostoslista:
            maara += ostos.lukumaara()
        return maara
        
    def hinta(self):
        hinta = 0
        for ostos in self.ostoslista:
            hinta += ostos.hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        puuttuu_listalta = True
        for tuote in self.ostoslista:
            if tuote.tuotteen_nimi() == lisattava.nimi():
                tuote.muuta_lukumaaraa(1)
                puuttuu_listalta = False
                break
        if puuttuu_listalta:
            self.ostoslista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for tuote in self.ostoslista:
            if tuote.tuotteen_nimi() == poistettava.nimi():
                tuote.muuta_lukumaaraa(-1)
                if tuote.lukumaara() == 0:
                    self.ostoslista.remove(tuote)
                break

    def tyhjenna(self):
        self.ostoslista = []

    def ostokset(self):
        return self.ostoslista
