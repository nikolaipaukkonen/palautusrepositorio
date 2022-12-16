from tuomari import Tuomari
from tekoaly import Tekoaly
from kivipaperisakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        toisen_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {toisen_siirto}")
        return toisen_siirto