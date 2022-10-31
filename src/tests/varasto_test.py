import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikalisays_varastoon(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_poisto_tyhjasta(self):
        self.varasto.ota_varastosta(3)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10.0)

    def test_liikapoisto(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(saatu, 5)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10.0)

    def test_to_string(self):
        self.varasto.lisaa_varastoon(3)

        self.assertEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")

    def test_init(self):
        var = Varasto(10, 0)
        self.assertAlmostEqual(var.paljonko_mahtuu(), 10.0)
        var = Varasto(10, 11)
        self.assertAlmostEqual(var.paljonko_mahtuu(), 0.0)
        var = Varasto(10, 5)
        self.assertAlmostEqual(var.paljonko_mahtuu(), 5.0)
        var = Varasto(-1, 5)
        self.assertAlmostEqual(var.tilavuus, 0.0)
        var = Varasto(10, -1)
        self.assertAlmostEqual(var.saldo, 0.0)

    def test_invalid_lisays(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_invalid_otto(self):
        self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
