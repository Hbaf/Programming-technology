import unittest
from lab2.list_2 import *


class TestList(unittest.TestCase):

    def test_rm_adj_1(self):
        self.assertEqual([0, 2, 3], rm_adj([0, 2, 2, 3]))

    def test_mrg_lsts_1(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7], mrg_lsts([0, 2, 5, 6], [1, 3, 4, 7]))