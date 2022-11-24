import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    # Step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # step 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tavaran_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    # step 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tavaroidenn_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(self.kori.hinta(), 7)

    # step 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tavaroiden_hintojen_summa(self):
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        self.assertEqual(self.kori.hinta(), 8)

    # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertTrue(isinstance(ostokset[0], Ostos))

    # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    # step 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kauramaito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
        for ostos in ostokset:
            self.assertTrue(isinstance(ostos, Ostos))

    # step 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertTrue(isinstance(ostokset[0], Ostos))

    # step 12
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_maara_(self):
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Kauramaito")
        self.assertEqual(ostos.lukumaara(), 2)

    # step 13
    def test_jos_korissa_kaksi_samaa_tuotetta_ja_toinen_poistetaan_jaa_yksi_tuote_jaljelle(self):
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.poista_tuote(kauramaito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    # step 14
    def test_jos_koriin_on_lisatty_tuote_ja_sama_tuote_poistetaan_on_kori_taman_jalkeen_tyhja(self):
        kauramaito = Tuote("Kauramaito", 4)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.poista_tuote(kauramaito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)
        self.assertEqual(self.kori.hinta(), 0)

    # step 15
    def test_tyhjenna_metodi_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        kauramaito = Tuote("Kauramaito", 4)
        kirja = Tuote("Kirja", 20)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kauramaito)
        self.kori.lisaa_tuote(kirja)
        self.assertEqual(self.kori.tavaroita_korissa(), 4)
        self.assertEqual(self.kori.hinta(), 31)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
