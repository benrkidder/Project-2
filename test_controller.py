from unittest import *
from controller import *


class TestController(TestCase):
    def test_shuffle_deck(self):
        self.assertEqual(len(shuffle_deck()), 52)
        self.assertEqual(type(shuffle_deck()), list)
        self.assertNotEqual(shuffle_deck(), shuffle_deck())

    def test_deal(self):
        self.assertEqual(len(deal(shuffle_deck())[0]), 48)

    # def test_draw(self):
    #     self.assertCountEqual()
