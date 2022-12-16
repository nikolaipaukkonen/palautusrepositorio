from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kivipaperisakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = TekoalyParannettu()

    def _toisen_siirto(self, ensimmaisen_siirto):
        toisen_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {toisen_siirto}")
        return toisen_siirto
