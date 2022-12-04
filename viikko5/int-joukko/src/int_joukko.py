KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetti on väärässä muodossa")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetti on väärässä muodossa")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lukumaara = 0

    def kuuluu_joukkoon(self, luku):
        kuuluu_joukkoon = False

        for i in range(0, self.alkioiden_lukumaara):
            if luku == self.lukujono[i]:
                kuuluu_joukkoon = True

        if kuuluu_joukkoon:
            return True
        return False

    def lisaa(self, lisattava):
        if self.alkioiden_lukumaara == 0:
            self.lukujono[0] = lisattava
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1
            return True

        if not self.kuuluu_joukkoon(lisattava):
            self.lukujono[self.alkioiden_lukumaara] = lisattava
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1

            if self.alkioiden_lukumaara % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.kopioi_taulukko(self.lukujono, taulukko_old)
                self.lukujono = [0] * (self.alkioiden_lukumaara + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

            return True

        return False

    def poista(self, poistettava):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lukumaara):
            if poistettava == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lukumaara - 1):
                apu = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apu

            self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
            return True

        return False

    def kopioi_taulukko(self, kopioitava, kohde):
        for i in range(0, len(kopioitava)):
            kohde[i] = kopioitava[i]

    def get_alkioiden_lukumaara(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lukumaara

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(ensimmainen_joukko, toinen_joukko):
        int_joukko = IntJoukko()
        ensimmainen_taulu = ensimmainen_joukko.to_int_list()
        toinen_taulu = toinen_joukko.to_int_list()

        for i in range(0, len(ensimmainen_taulu)):
            int_joukko.lisaa(ensimmainen_taulu[i])

        for i in range(0, len(toinen_taulu)):
            int_joukko.lisaa(toinen_taulu[i])

        return int_joukko

    @staticmethod
    def leikkaus(ensimmainen_joukko, toinen_joukko):
        int_joukko = IntJoukko()
        ensimmainen_taulu = ensimmainen_joukko.to_int_list()
        toinen_taulu = toinen_joukko.to_int_list()

        for i in range(0, len(ensimmainen_taulu)):
            for j in range(0, len(toinen_taulu)):
                if ensimmainen_taulu[i] == toinen_taulu[j]:
                    int_joukko.lisaa(toinen_taulu[j])

        return int_joukko

    @staticmethod
    def erotus(ensimmainen_joukko, toinen_joukko):
        int_joukko = IntJoukko()
        ensimmainen_taulu = ensimmainen_joukko.to_int_list()
        toinen_taulu = toinen_joukko.to_int_list()

        for i in range(0, len(ensimmainen_taulu)):
            int_joukko.lisaa(ensimmainen_taulu[i])

        for i in range(0, len(toinen_taulu)):
            int_joukko.poista(toinen_taulu[i])

        return int_joukko

    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
        if self.alkioiden_lukumaara == 1:
            return "{" + str(self.lukujono[0]) + "}"

        tuotos = "{"
        for i in range(0, self.alkioiden_lukumaara - 1):
            tuotos = tuotos + str(self.lukujono[i])
            tuotos = tuotos + ", "
        tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1])
        tuotos = tuotos + "}"
        return tuotos
