import unittest
from cryptage import *

class Cryptage_Test(unittest.TestCase):

    def test_crypt(self):
        self.assertEqual(crypt("Yo"), "Rp")
        self.assertEqual(crypt("Salut ca va "), "Tbmvuadbawba")

if __name__ == '__main__':
    unittest.main()