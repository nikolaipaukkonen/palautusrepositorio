from kivipaperisakset import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        pass
    
    def _toisen_siirto(self, ensimmaisen_siirto):
            return input("Toisen pelaajan siirto: ")
