import int_joukko

class JoukkoOppiService():
    @staticmethod
    def yhdiste(ensimmainen_joukko, toinen_joukko):
        int_joukko_palautus = ensimmainen_joukko
        
        for i in range(0, toinen_joukko.get_alkioiden_lukumaara()):
            int_joukko_palautus.lisaa(toinen_joukko.lukujono[i])

        return int_joukko_palautus

    @staticmethod
    def leikkaus(ensimmainen_joukko, toinen_joukko):
        int_joukko_palautus = int_joukko.IntJoukko()

        for i in range(0, ensimmainen_joukko.get_alkioiden_lukumaara()):
            for j in range(0, toinen_joukko.get_alkioiden_lukumaara()):
                if ensimmainen_joukko.lukujono[i] == toinen_joukko.lukujono[j]:
                    int_joukko_palautus.lisaa(ensimmainen_joukko.lukujono[i])

        return int_joukko_palautus

    @staticmethod
    def erotus(ensimmainen_joukko, toinen_joukko):
        int_joukko_palautus = ensimmainen_joukko

        for i in range(0, toinen_joukko.get_alkioiden_lukumaara()):
            int_joukko_palautus.poista(toinen_joukko.lukujono[i])

        return int_joukko_palautus
