import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)

    def test_luodussa_kassassa_oikea_maara_raaha(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_luodussa_kassassa_oikea_maara_myytyja(self):
        self.assertEqual(self.kassa.edulliset + self.kassa.maukkaat, 0)


    # edullisen kateisosto
    def test_edullisen_kateisosto_kasvattaa_rahaa_oikein(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000+240)
    
    def test_edullisen_kateisosto_vaihtoraha_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)
    
    def test_edullisen_kateisosto_kasvattaa_maaraa_oikein(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullisen_kateisosto_alle_hinnan_ei_kasvata_rahaa(self):
        self.kassa.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_edullisen_kateisosto_alle_hinnan_palauttaa_koko_summan(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(150), 150)
    
    def test_edullisen_kateisosto_alle_hinnan_ei_kasvata_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassa.edulliset, 0)


    # maukkaan kateisosto
    def test_maukkaan_kateisosto_kasvattaa_rahaa_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000+400)
    
    def test_maukkaan_kateisosto_vaihtoraha_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
    
    def test_maukkaan_kateisosto_kasvattaa_maaraa_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maukkaan_kateisosto_alle_hinnan_ei_kasvata_rahaa(self):
        self.kassa.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_maukkaan_kateisosto_alle_hinnan_palauttaa_koko_summan(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(150), 150)
    
    def test_maukkaan_kateisosto_alle_hinnan_ei_kasvata_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassa.maukkaat, 0)

    # edullisen korttiosto
    def test_edullisen_korttiosto_rahaa_tarpeeksi_palautetaan_true(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_edullisen_korttiosto_rahaa_tarpeeksi_raha_vahenee_kortilta(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 1000-240)

    def test_edullisen_korttiosto_rahaa_tarpeeksi_kasvattaa_maaraa_oikein(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullisen_korttiosto_rahaa_tarpeeksi_rahan_maara_ei_muutu(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisen_korttiosto_rahaa_ei_tarpeeksi_palautetaan_false(self):
        self.kortti.saldo=1
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)

    def test_edullisen_korttiosto_rahaa_ei_tarpeeksi_ei_kasvata_maaraa(self):
        self.kortti.saldo=1
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_edullisen_korttiosto_rahaa_ei_tarpeeksi_rahan_maara_ei_muutu(self):
        self.kortti.saldo=1
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    
    # maukkaan korttiosto
    def test_maukkaan_korttiosto_rahaa_tarpeeksi_palautetaan_true(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)

    def test_maukkaan_korttiosto_rahaa_tarpeeksi_raha_vahenee_kortilta(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 1000-400)

    def test_maukkaan_korttiosto_rahaa_tarpeeksi_kasvattaa_maaraa_oikein(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maukkaan_korttiosto_rahaa_tarpeeksi_rahan_maara_ei_muutu(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukkaan_korttiosto_rahaa_ei_tarpeeksi_palautetaan_false(self):
        self.kortti.saldo=1
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)

    def test_maukkaan_korttiosto_rahaa_ei_tarpeeksi_ei_kasvata_maaraa(self):
        self.kortti.saldo=1
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_maukkaan_korttiosto_rahaa_ei_tarpeeksi_rahan_maara_ei_muutu(self):
        self.kortti.saldo=1
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    # kortin lataus 
    def test_kortin_lataus_kassan_raha_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_kortin_lataus_kortin_raha_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 1100)
    
    def test_kortin_lataus_negatiivinen_summa_palauttaa_none(self):
        self.assertEqual(self.kassa.lataa_rahaa_kortille(self.kortti, -100), None)
    
    