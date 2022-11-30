from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Io:
    def __init__(self, input_field, output_field):
        self.input = input_field
        self.output = output_field

    def lue(self):
        return self.input.get()

    def kirjoita(self, viesti):
        self.output.set(str(viesti))

    def tyhjennaSyote(self):
        self.input.delete(0, constants.END)


class Laskutoimitus:
    def __init__(self, sovelluslogiikka,io):
        self.sovelluslogiikka = sovelluslogiikka
        self._io = io

class Summa(Laskutoimitus):
    def __init__(self, *args):
        super().__init__(*args)

    def suorita(self):
        luku = int(self._io.lue())
        self.sovelluslogiikka.plus(luku)

class Erotus(Laskutoimitus):
    def __init__(self, *args):
        super().__init__(*args)

    def suorita(self):
        luku = int(self._io.lue())
        self.sovelluslogiikka.miinus(luku)

class Nollaus(Laskutoimitus):
    def __init__(self, *args):
        super().__init__(*args)

    def suorita(self):
        self.sovelluslogiikka.nollaa()


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)
        self._io = Io(self._syote_kentta, self._tulos_var)

        self.komennot = {
                Komento.SUMMA: Summa(self._sovellus, self._io),
                Komento.EROTUS: Erotus(self._sovellus, self._io),
                Komento.NOLLAUS: Nollaus(self._sovellus, self._io)
                }

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        komento_olio = self.komennot.get(komento, None)
        if komento_olio:
            try:
                komento_olio.suorita()
            except Exception:
                print("Command not able to run")
        else:
            raise ValueError(f"Unknown command: {komento}")

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._io.tyhjennaSyote()
        self._io.kirjoita(self._sovellus.tulos)
