import unittest
from kaalin import KaalinNumber

class TestKaalinNumber(unittest.TestCase):
    def setUp(self):
        self.kn = KaalinNumber()

    def test_to_word(self):
        self.assertEqual(self.kn.to_word(5), "bes")
        self.assertEqual(self.kn.to_word(27), "jigirma jeti")
        self.assertEqual(self.kn.to_word(1000), "mıń")

    def test_base2to8(self):
        self.assertEqual(self.kn.base2to8('101'), '5')
        self.assertEqual(self.kn.base2to8('1101'), '15')
        self.assertEqual(self.kn.base2to8('11010'), '32')

    def test_base2to10(self):
        self.assertEqual(self.kn.base2to10('101'), 5)
        self.assertEqual(self.kn.base2to10('1101'), 13)
        self.assertEqual(self.kn.base2to10('111010'), 58)

    def test_base8to2(self):
        self.assertEqual(self.kn.base8to2('5'), '101')
        self.assertEqual(self.kn.base8to2('15'), '1101')
        self.assertEqual(self.kn.base8to2('32'), '11010')

    def test_base8to10(self):
        self.assertEqual(self.kn.base8to10('5'), 5)
        self.assertEqual(self.kn.base8to10('15'), 13)
        self.assertEqual(self.kn.base8to10('32'), 26)

    def test_base8to16(self):
        self.assertEqual(self.kn.base8to16('5'), '5')
        self.assertEqual(self.kn.base8to16('15'), 'd')
        self.assertEqual(self.kn.base8to16('32'), '1a')

    def test_base2to16(self):
        self.assertEqual(self.kn.base2to16('101'), '5')
        self.assertEqual(self.kn.base2to16('1101'), 'd')
        self.assertEqual(self.kn.base2to16('111010'), '3a')

    def test_base10to2(self):
        self.assertEqual(self.kn.base10to2(5), '101')
        self.assertEqual(self.kn.base10to2(13), '1101')
        self.assertEqual(self.kn.base10to2(58), '111010')

    def test_base10to8(self):
        self.assertEqual(self.kn.base10to8(5), '5')
        self.assertEqual(self.kn.base10to8(13), '15')
        self.assertEqual(self.kn.base10to8(58), '72')

    def test_base10to16(self):
        self.assertEqual(self.kn.base10to16(5), '5')
        self.assertEqual(self.kn.base10to16(13), 'd')
        self.assertEqual(self.kn.base10to16(58), '3a')

if __name__ == '__main__':
    unittest.main()
