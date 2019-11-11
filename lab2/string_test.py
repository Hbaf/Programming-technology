import unittest
from lab2.string_2 import *


class TestList(unittest.TestCase):

    def test_v_1(self):
        self.assertEqual('missingly', v('missing'))

    def test_v_2(self):
        self.assertEqual('missing', v('miss'))

    def test_nb_1(self):
        self.assertEqual('good', nb('notnotnotnotnotnotbad'))

    def test_nb_2(self):
        self.assertEqual('good for me', nb('not fricking bad for me'))
