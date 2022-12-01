class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [None] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        on = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                on = on + 1

        if on > 0:
            return True
        else:
            return False

    def lisaa(self, lisattava):

        def kasvata_lukujonoa():
            self.kapasiteetti += self.kasvatuskoko
            uusiLukujono = [None] * self.kapasiteetti
            for i in range(0, self.alkioiden_lkm):
                uusiLukujono[i] = self.lukujono[i]
            self.lukujono = uusiLukujono

        def hae_lisays_paikka_binaarihaulla():
            ala = 0
            yla = self.alkioiden_lkm
            indx = None
            while True:
                if ala == yla:
                    return ala
                indx = ala + ((yla - ala) // 2)
                luku = self.lukujono[indx]
                if luku == lisattava:
                    return None
                elif lisattava < luku:
                    yla = indx
                else:
                    ala = indx + 1

        def sijoita_lisattava_paikalleen():
            for i in reversed(range(paikka, self.alkioiden_lkm)):
                self.lukujono[i+1] = self.lukujono[i]
            self.lukujono[paikka] = lisattava
            self.alkioiden_lkm += 1

        if self.alkioiden_lkm == self.kapasiteetti:
            kasvata_lukujonoa()
        paikka = hae_lisays_paikka_binaarihaulla()
        if paikka is None:
            return False
        sijoita_lisattava_paikalleen()
        return True

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
