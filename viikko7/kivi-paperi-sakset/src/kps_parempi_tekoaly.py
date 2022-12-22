from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self, muistin_koko):
        self._muistin_koko = muistin_koko

    def pelaa(self):
        self.tekoaly = TekoalyParannettu(self._muistin_koko)
        super().pelaa()

    def hae_kilpailijan_siirto(self, ekan_siirto):
        tekoalyn_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tekoalyn_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tekoalyn_siirto
