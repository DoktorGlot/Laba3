import unittest

# Импортируем функции, которые мы хотим протестировать
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(7, 2), 14)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, 4), -12)

    def test_divide(self):
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(8, 0), "Деление на ноль невозможно")

if __name__ == '__main__':
    unittest.main()
