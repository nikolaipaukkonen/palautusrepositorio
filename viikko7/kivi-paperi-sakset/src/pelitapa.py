from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kivipaperisakset import KiviPaperiSakset

class Pelitapa:
    def __init__(self):
        
        pass

    def pelitapa(pelitapa): 
        pelaajavspelaaja = KPSPelaajaVsPelaaja()
        tekoalypeli = KPSTekoaly()
        parempi_tekoalypeli = KPSParempiTekoaly()

        if pelitapa == "a":
            pelaajavspelaaja.pelaa()
        elif pelitapa == "b":
            tekoalypeli.pelaa()
        elif pelitapa == "c":
            parempi_tekoalypeli.pelaa()
        else:
            return None