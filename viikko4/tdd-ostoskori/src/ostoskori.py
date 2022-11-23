from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self.ostokset()])

    def hinta(self):
        return sum([ostos.hinta() for ostos in self.ostokset()])

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi not in self._ostokset.keys():
            self._ostokset[lisattava.nimi] = Ostos(lisattava)
        else:
            self._ostokset[lisattava.nimi].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._ostokset.values())
