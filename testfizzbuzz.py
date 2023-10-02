import unittest
from fizzbuzz import*

class testfizzbuzz(unittest.TestCase):

    def setUp(self):
        self.instance=fizzbuzz()


    def test_affiche_sans_param(self):
        with self.subTest(self):
            self.assertEqual(self.instance.affiche(100), "12Fizz4BuzzFizz78F")
        with self.subTest(self):
            self.assertEqual(self.instance.affiche(5),"12Fizz4Buzz")
        with self.subTest(self):
            self.assertEqual(self.instance.affiche(3),"12Fizz")


if __name__ == '__main__':
    unittest.main()
