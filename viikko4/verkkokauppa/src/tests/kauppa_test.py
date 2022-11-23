import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipa", 10)
            if tuote_id == 3:
                return Tuote(3, "kala", 15)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilimaksun_jalkeen_kutsutaan_metodia_tilisiirto_oikealla_asiakkaalla_tilinumerolla_ja_summalla(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("testi", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("testi", 42, "12345", ANY, 5)

    def test_lisataan_koriin_kaksi_samaa_tuotetta_ja_kutsutaan_tilisiirtoa_oikealla_asiakkaalla_tilinumerolla_ja_summalla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("testi", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("testi", 42, "12345", ANY, 10)

    def test_lisataan_koriin_kaksi_eri_tuotetta_ja_kutsutaan_tilisiirtoa_oikealla_asiakkaalla_tilinumerolla_ja_summalla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("testi", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("testi", 42, "12345", ANY, 15)

    def test_lisataan_koriin_kaksi_eri_tuotetta_joista_toinen_on_loppu(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("testi", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("testi", 42, "12345", ANY, 5)   