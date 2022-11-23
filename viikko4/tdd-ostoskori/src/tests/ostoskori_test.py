import unittest
from ostoskori import Ostoskori
from tuote import Tuote

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
        self.assertEqual(len(self.kori.ostokset), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
