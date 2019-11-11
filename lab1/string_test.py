import unittest
from lab1.string_1 import *


class TestString(unittest.TestCase):

    def test_num_of_items_on_5(self):
        self.assertEqual('Number of: 5', num_of_items(5))

    def test_num_of_items_on_10(self):
        self.assertEqual('Number of: many', num_of_items(10))

    def test_num_of_items_on_minus_5(self):
        self.assertEqual('Number of: -5', num_of_items(-5))

    def test_start_end_symbols_on_welcome(self):
        self.assertEqual('weme', start_end_symbols('welcome'))

    def test_start_end_symbols_on_bye(self):
        self.assertEqual('byye', start_end_symbols('bye'))

    def test_start_end_symbols_on_hi(self):
        self.assertEqual('hihi', start_end_symbols('hi'))

    def test_start_end_symbols_on_i(self):
        self.assertEqual('ii', start_end_symbols('i'))

    def test_replace_char_on_bubble(self):
        self.assertEqual('bu**le', replace_char('bubble'))

    def test_replace_char_on_cuddle(self):
        self.assertEqual('cuddle', replace_char('cuddle'))

    def test_replace_char_on_шиншилла(self):
        self.assertEqual('шин*илла', replace_char('шиншилла'))

    def test_str_mix_on_bubble_cuddle(self):
        self.assertEqual('cubble buddle', str_mix('bubble', 'cuddle'))

    def test_str_mix_on_summer_rainbow(self):
        self.assertEqual('rammer suinbow', str_mix('summer', 'rainbow'))


