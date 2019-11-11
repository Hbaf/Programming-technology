import unittest
from lab1.list import *


class TestList(unittest.TestCase):

    def test_me_1(self):
        self.assertEqual(2, me(['meem', 'weed', 'cool', 'tt', 'length', 'typo', 'pop']))

    def test_me_2(self):
        self.assertEqual(0, me('string'))

    def test_fx_1(self):
        self.assertEqual(['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix'], fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']))
        # self.assertEqual([''], fx(['sun', 'rainbow', 'cloud', 'xyz', 'tree', 'lake', 'xuan', 'Earth']))

    def test_fs_1(self):
        self.assertEqual([(2, 2), (1, 3), (3, 4, 5), (1, 7)], fs([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))
