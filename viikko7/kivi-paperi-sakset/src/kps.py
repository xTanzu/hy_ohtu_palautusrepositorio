from tuomari import Tuomari


class KPS:
    def pelaa(self):
        self.tuomari = Tuomari()
        peli_jatkuu = True
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        while peli_jatkuu:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self.hae_kilpailijan_siirto(ekan_siirto)
            peli_jatkuu = self._onko_ok_siirto(ekan_siirto) and \
                          self._onko_ok_siirto(tokan_siirto)
            if peli_jatkuu:
                self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(self.tuomari)

        print("Kiitos!")
        print(self.tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
