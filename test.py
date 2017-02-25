import unittest
import main
import Division
import Multiplication

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):
        valueData = [8, 3, 0.52, 0.72, 0, 95, 0.5, 16, 6, 0.26, 331, 123.1, 0]
        main.TestCode(valueData)
    def test2(self):
        self.assertEqual(Multiplication.Multiply(2,3), 6)

        
if __name__ == '__main__':
    unittest.main()