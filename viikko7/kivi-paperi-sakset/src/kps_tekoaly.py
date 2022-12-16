from tuomari import Tuomari
from tekoaly import Tekoaly
from kivipaperisakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = Tekoaly()
        toisen_siirto = tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {toisen_siirto}")
        return toisen_siirto