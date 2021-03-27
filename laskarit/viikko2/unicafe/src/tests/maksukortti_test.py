import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo,10)

    def test_saldon_kasvatus(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 15)

    def test_otto_palauttaa_true(self):
        self.assertEqual(True, self.maksukortti.ota_rahaa(5))

    def test_otto_palauttaa_false_jos_saldo_menisi_negatiiviseksi(self):
        self.assertEqual(False, self.maksukortti.ota_rahaa(50))
    
    def test_ottoo_jattaa_oikean_summan(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo,5)

    def test_otto_pitaa_saman_summan_jos_saldo_menisi_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(self.maksukortti.saldo,10)
    
    def test_merkkijonoesitys_oikein(self):
        self.assertEqual(str(self.maksukortti), f"saldo: 0.1")