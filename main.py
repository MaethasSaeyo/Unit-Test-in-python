import unittest
def add_numder(a,b):
    return a - b 



class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numder(1,2),3)
        self.assertEqual(add_numder(2,2),4)
        self.assertEqual(add_numder(1,4),5)
        self.assertEqual(add_numder(9,2),11)
        self.assertEqual(add_numder(8,2),10)


if __name__ == '__main__':
    unittest.main()
