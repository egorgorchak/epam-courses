import unittest
from src.task001 import Task001


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        answer = Task001.addition(3, 5)
        self.assertEqual(answer, 8)

    def test_subtraction(self):
        answer = Task001.subtraction(3, 5)
        self.assertEqual(answer, -2)

    def test_multiplication(self):
        answer = Task001.multiplication(3, 5)
        self.assertEqual(answer, 15)

    def test_division(self):
        answer = Task001.division(15, 5)
        self.assertEqual(answer, 3)


if __name__ == '__main__':
    unittest.main()
