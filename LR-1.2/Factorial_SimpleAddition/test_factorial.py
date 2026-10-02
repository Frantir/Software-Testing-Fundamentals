import unittest
from factorial import Factorial


class TestFactorial(unittest.TestCase):

    # --- Базовые значения ---
    def test_zero(self):
        # 0! = 1 по определению
        self.assertEqual(Factorial(0).compute(), 1)

    def test_one(self):
        self.assertEqual(Factorial(1).compute(), 1)

    def test_two(self):
        self.assertEqual(Factorial(2).compute(), 2)

    # --- Типовые значения ---
    def test_five(self):
        # 5! = 120
        self.assertEqual(Factorial(5).compute(), 120)

    def test_ten(self):
        # 10! = 3 628 800
        self.assertEqual(Factorial(10).compute(), 3_628_800)

    def test_twenty(self):
        # 20! = 2 432 902 008 176 640 000
        self.assertEqual(Factorial(20).compute(), 2_432_902_008_176_640_000)

    # --- Рекурсивная реализация (совпадает с итеративной) ---
    def test_recursive_matches_iterative(self):
        for n in range(0, 15):
            f = Factorial(n)
            self.assertEqual(
                f.compute(),
                f.compute_recursive(),
                msg=f"Расхождение на n={n}"
            )

    # --- Валидация ввода ---
    def test_negative(self):
        with self.assertRaises(ValueError):
            Factorial(-1)

    def test_negative_large(self):
        with self.assertRaises(ValueError):
            Factorial(-100)

    def test_float(self):
        with self.assertRaises(TypeError):
            Factorial(5.0)

    def test_string(self):
        with self.assertRaises(TypeError):
            Factorial("5")

    def test_bool(self):
        with self.assertRaises(TypeError):
            Factorial(True)

    def test_none(self):
        with self.assertRaises(TypeError):
            Factorial(None)

    # --- Математические свойства ---
    def test_recurrence_relation(self):
        # n! = n · (n-1)! для всех n ≥ 1
        for n in range(1, 15):
            self.assertEqual(
                Factorial(n).compute(),
                n * Factorial(n - 1).compute(),
                msg=f"n! ≠ n·(n-1)! на n={n}"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)