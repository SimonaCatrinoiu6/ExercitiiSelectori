import unittest
import HtmlTestRunner

from Sesiunea_11_UnitTest import TestLogin
from Sesiunea_12_Alerte import alerte


class Test_Suit(unittest.TestCase):
    def test_suit(self):
        suita=unittest.TestSuite()
        suita.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
                        unittest.defaultTestLoader.loadTestsFromTestCase(alerte)])