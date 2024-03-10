import unittest

from kaalin.words.latin import KaalinLatin

class TestKaalinLatin(unittest.TestCase):
    def setUp(self):
        self.kaalin_latin = KaalinLatin()

    def test_get_uppercases(self):
        uppercases = self.kaalin_latin.get_uppercases()
        self.assertEqual(len(uppercases), 34)

    def test_get_lowercases(self):
        lowercases = self.kaalin_latin.get_lowercases()
        self.assertEqual(len(lowercases), 34)

    def test_is_upper(self):
        self.assertTrue(self.kaalin_latin.is_upper('A'))
        self.assertTrue(self.kaalin_latin.is_upper('B'))
        self.assertTrue(self.kaalin_latin.is_upper('Á'))
        self.assertTrue(self.kaalin_latin.is_upper('Ǵ'))
        self.assertTrue(self.kaalin_latin.is_upper('Ú'))
        self.assertFalse(self.kaalin_latin.is_upper('a'))
        self.assertFalse(self.kaalin_latin.is_upper('b'))
        self.assertFalse(self.kaalin_latin.is_upper('c'))
        self.assertFalse(self.kaalin_latin.is_upper('f'))
        self.assertFalse(self.kaalin_latin.is_upper('g'))

    def test_is_lower(self):
        self.assertTrue(self.kaalin_latin.is_lower('a'))
        self.assertTrue(self.kaalin_latin.is_lower('b'))
        self.assertTrue(self.kaalin_latin.is_lower('f'))
        self.assertTrue(self.kaalin_latin.is_lower('l'))
        self.assertFalse(self.kaalin_latin.is_lower('A'))
        self.assertFalse(self.kaalin_latin.is_lower('Ǵ'))
        self.assertFalse(self.kaalin_latin.is_lower('J'))

    def test_is_digit(self):
        self.assertTrue(self.kaalin_latin.is_digit('5'))
        self.assertTrue(self.kaalin_latin.is_digit('12'))
        self.assertTrue(self.kaalin_latin.is_digit('312'))
        self.assertTrue(self.kaalin_latin.is_digit('9212'))
        self.assertFalse(self.kaalin_latin.is_digit('a'))
        self.assertFalse(self.kaalin_latin.is_digit('b'))
        self.assertFalse(self.kaalin_latin.is_digit('d'))
        self.assertFalse(self.kaalin_latin.is_digit('l'))

    def test_is_alpha(self):
        self.assertTrue(self.kaalin_latin.is_alpha('A'))
        self.assertTrue(self.kaalin_latin.is_alpha('a'))
        self.assertFalse(self.kaalin_latin.is_alpha('5'))

    def test_swapcase(self):
        result = self.kaalin_latin.swapcase('Hello World')
        self.assertEqual(result, 'hELLO wORLD')

    def test_to_upper(self):
        result = self.kaalin_latin.to_upper('hello world')
        self.assertEqual(result, 'HELLO WORLD')

    def test_to_lower(self):
        result = self.kaalin_latin.to_lower('HELLO WORLD')
        self.assertEqual(result, 'hello world')

if __name__ == '__main__':
    unittest.main()
