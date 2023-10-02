import unittest
from fizzbuzz import*

class testfizzbuzz(unittest.TestCase):

    def setUp(self):
        self.instance=fizzbuzz()


    def test_affiche_sans_param(self):
        self.assertEqual(self.instance.affiche(),"12Fizz4Buzz")



if __name__ == '__main__':
    unittest.main()
