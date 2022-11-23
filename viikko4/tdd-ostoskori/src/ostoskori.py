from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tuotteet = []

    def tavaroita_korissa(self):
        return len(self.tuotteet)

    def hinta(self):
        if len(self.tuotteet) > 0:
            return self.tuotteet[0].hinta()
        return 0

    def lisaa_tuote(self, lisattava: Tuote):
        self.tuotteet.append(lisattava)

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
