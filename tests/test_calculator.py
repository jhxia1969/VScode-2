import unittest

from src.core.calculator import calculate


class TestCalculator(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(calculate("add", 2, 3), 5)

    def test_sub(self) -> None:
        self.assertEqual(calculate("sub", 10, 4), 6)

    def test_mul(self) -> None:
        self.assertEqual(calculate("mul", 3, 5), 15)

    def test_div(self) -> None:
        self.assertEqual(calculate("div", 8, 2), 4)

    def test_div_zero(self) -> None:
        with self.assertRaises(ValueError):
            calculate("div", 1, 0)


if __name__ == "__main__":
    unittest.main()
