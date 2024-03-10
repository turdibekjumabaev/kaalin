import unittest

from kaalin.words.cyrillic import KaalinCyrillic


class TestKaalinCyrillic(unittest.TestCase):
    def setUp(self):
        self.kaalin_cyrillic = KaalinCyrillic()

    def test_get_uppercases(self):
        uppercases = self.kaalin_cyrillic.get_uppercases()
        self.assertEqual(len(uppercases), 34)

    def test_get_lowercases(self):
        lowercases = self.kaalin_cyrillic.get_lowercases()
        self.assertEqual(len(lowercases), 34)

    def test_is_upper(self):
        self.assertTrue(self.kaalin_cyrillic.is_upper('А'))
        self.assertTrue(self.kaalin_cyrillic.is_upper('Б'))
        self.assertFalse(self.kaalin_cyrillic.is_upper('а'))

    def test_is_lower(self):
        self.assertTrue(self.kaalin_cyrillic.is_lower('а'))
        self.assertTrue(self.kaalin_cyrillic.is_lower('б'))
        self.assertFalse(self.kaalin_cyrillic.is_lower('А'))

    def test_is_digit(self):
        self.assertTrue(self.kaalin_cyrillic.is_digit('5'))
        self.assertFalse(self.kaalin_cyrillic.is_digit('а'))

    def test_is_alpha(self):
        self.assertTrue(self.kaalin_cyrillic.is_alpha('А'))
        self.assertTrue(self.kaalin_cyrillic.is_alpha('а'))
        self.assertTrue(self.kaalin_cyrillic.is_alpha('5'))

    def test_swapcase(self):
        result = self.kaalin_cyrillic.swapcase('Привет, мир!')
        self.assertEqual(result, 'пРИВЕТ, МИР!')

    def test_to_upper(self):
        result = self.kaalin_cyrillic.to_upper('привет, мир!')
        self.assertEqual(result, 'ПРИВЕТ, МИР!')

    def test_to_lower(self):
        result = self.kaalin_cyrillic.to_lower('ПРИВЕТ, МИР!')
        self.assertEqual(result, 'привет, мир!')

if __name__ == '__main__':
    unittest.main()
