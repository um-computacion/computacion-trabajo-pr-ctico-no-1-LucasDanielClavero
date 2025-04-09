import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

    def test_triple_repeticion(self):
        self.assertEqual(decimal_to_roman(3), "III")
        self.assertEqual(decimal_to_roman(30), "XXX")
        self.assertEqual(decimal_to_roman(300), "CCC")
        self.assertEqual(decimal_to_roman(3000), "MMM")

    def test_triple_capicua(self):
        self.assertEqual(decimal_to_roman(101), "CI")
        self.assertEqual(decimal_to_roman(202), "CCII")
        self.assertEqual(decimal_to_roman(303), "CCCIII")
    
    def test_triple_pares(self):
        self.assertEqual(decimal_to_roman(2), "II")
        self.assertEqual(decimal_to_roman(6), "VI")
        self.assertEqual(decimal_to_roman(12), "XII")

    

if __name__ == '__main__':
    unittest.main()

