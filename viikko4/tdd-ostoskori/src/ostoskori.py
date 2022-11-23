from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []

    def tavaroita_korissa(self):
        return len(self.ostokset)

    def hinta(self):
        return sum([ostos.hinta() for ostos in self.ostokset])

    def lisaa_tuote(self, lisattava: Tuote):
        self.ostokset.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
