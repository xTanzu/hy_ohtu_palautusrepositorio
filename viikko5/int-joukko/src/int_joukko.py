class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [None] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        lisays_paikka_olemassa, paikka = self.luvun_lisays_paikka_binaarihaulla(luku)
        return not lisays_paikka_olemassa

    def lisaa(self, lisattava):

        def kasvata_lukujonoa():
            self.kapasiteetti += self.kasvatuskoko
            uusiLukujono = [None] * self.kapasiteetti
            self.kopioi_taulukko(self.lukujono, uusiLukujono, self.alkioiden_lkm)
            self.lukujono = uusiLukujono

        def sijoita_ja_jarjesta():
            for i in reversed(range(lisays_paikka, self.alkioiden_lkm)):
                self.lukujono[i+1] = self.lukujono[i]
            self.lukujono[lisays_paikka] = lisattava
            self.alkioiden_lkm += 1

        if self.alkioiden_lkm == self.kapasiteetti:
            kasvata_lukujonoa()
        olemassa, lisays_paikka = self.luvun_lisays_paikka_binaarihaulla(lisattava)
        if olemassa is False:
            return False
        sijoita_ja_jarjesta()
        return True

    def luvun_lisays_paikka_binaarihaulla(self, luku):
        ala = 0
        yla = self.alkioiden_lkm
        indx = None
        while True:
            if ala == yla:
                return True, ala
            indx = ala + ((yla - ala) // 2)
            luku_indx = self.lukujono[indx]
            if luku_indx == luku:
                return False, indx
            elif luku < luku_indx:
                yla = indx
            else:
                ala = indx + 1

    def poista(self, poistettava):

        def poista_ja_jarjesta():
            self.alkioiden_lkm -= 1
            for i in range(paikka, self.alkioiden_lkm):
                self.lukujono[i] = self.lukujono[i+1]
            self.lukujono[self.alkioiden_lkm] = None

        lisays_paikka_olemassa, paikka = self.luvun_lisays_paikka_binaarihaulla(poistettava)
        if lisays_paikka_olemassa:
            return False
        poista_ja_jarjesta()
        return True

    def kopioi_taulukko(self, lahde, kohde, pituus):
        for i in range(0, pituus):
            kohde[i] = lahde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [None] * self.alkioiden_lkm
        self.kopioi_taulukko(self.lukujono, taulu, self.alkioiden_lkm)
        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            yhdiste_joukko.lisaa(luku)

        for luku in b_taulu:
            yhdiste_joukko.lisaa(luku)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        return IntJoukko.kilpailu_valinta(a_taulu, b_taulu, "leikkaus")

    @staticmethod
    def erotus(a, b):
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        return IntJoukko.kilpailu_valinta(a_taulu, b_taulu, "erotus")

    @staticmethod
    def kilpailu_valinta(a_taulu, b_taulu, valinta_strategia):
        joukko = IntJoukko()
        a_indx = b_indx = 0

        while a_indx < len(a_taulu) and b_indx < len(b_taulu):
            a_val = a_taulu[a_indx]
            b_val = b_taulu[b_indx]
            if a_val == b_val:
                if valinta_strategia == "leikkaus":
                    joukko.lisaa(a_val)
                a_indx += 1
                b_indx += 1
                continue
            if a_val < b_val:
                if valinta_strategia == "erotus":
                    joukko.lisaa(a_val)
                a_indx += 1
            else:
                b_indx += 1

        if valinta_strategia == "erotus" and a_indx < len(a_taulu) and b_indx == len(b_taulu):
            for luku in a_taulu[a_indx:]:
                joukko.lisaa(luku)

        return joukko

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
