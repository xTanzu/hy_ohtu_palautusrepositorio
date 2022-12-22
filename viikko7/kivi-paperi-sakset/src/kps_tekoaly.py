from kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def pelaa(self):
        self.tekoaly = Tekoaly()
        super().pelaa()

    def hae_kilpailijan_siirto(self, ekan_siirto):
        tekoalyn_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tekoalyn_siirto}")
        return tekoalyn_siirto
