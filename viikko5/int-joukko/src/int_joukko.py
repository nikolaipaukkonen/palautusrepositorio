KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetti on väärässä muodossa")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoko on väärässä muodossa")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lukumaara = 0

    def kuuluu_joukkoon(self, luku):
        kuuluu_joukkoon = False

        for i in range(0, self.alkioiden_lukumaara):
            if luku == self.lukujono[i]:
                kuuluu_joukkoon = True

        return kuuluu_joukkoon

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
        for i in range(0, self.alkioiden_lukumaara):
            if poistettava == self.lukujono[i]:
                del self.lukujono[i]
                self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
                return True

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
