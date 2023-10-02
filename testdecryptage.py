import unittest
from decryptage import *

class decryptage_Test(unittest.TestCase):

    def test_decryptage(self):
        self.assertEqual(decryptage("Yo"), "Rp")
        self.assertEqual(decryptage("Salut ca va "), "Tbmvuadbawba")


if __name__ == '__main__':
    unittest.main()