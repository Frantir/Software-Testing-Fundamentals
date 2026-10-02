import unittest
from simple_addition import SimpleAddition


class TestSimpleAddition(unittest.TestCase):

    # --- Пример из условия ---
    def test_example_from_task(self):
        # K=4, A="1", B="3" -> "4"
        sa = SimpleAddition(4, "1", "3")
        self.assertEqual(sa.compute(), "4")

    # --- Простые случаи ---
    def test_simple(self):
        # K=9, A="12", B="34" -> 1+3=4, 2+4=6 -> "46"
        sa = SimpleAddition(9, "12", "34")
        self.assertEqual(sa.compute(), "46")

    # --- Сумма цифр больше 9 ---
    def test_sum_over_nine(self):
        # K=9, A="99", B="11" -> 9+1=10, 9+1=10 -> "1010"
        sa = SimpleAddition(9, "99", "11")
        self.assertEqual(sa.compute(), "1010")

    # --- Разная длина чисел ---
    def test_different_length(self):
        # K=9, A="1", B="100" -> выравниваем: "001" + "100" -> 0+1=1, 0+0=0, 1+0=1 -> "101"
        sa = SimpleAddition(9, "1", "100")
        self.assertEqual(sa.compute(), "101")

    # --- Ведущие нули ---
    def test_leading_zeros(self):
        # K=9, A="0012", B="0034" -> "46"
        sa = SimpleAddition(9, "0012", "0034")
        self.assertEqual(sa.compute(), "46")

    # --- Нулевой результат ---
    def test_zero_result(self):
        # K=9, A="0", B="0" -> "0"
        sa = SimpleAddition(9, "0", "0")
        self.assertEqual(sa.compute(), "0")

    # --- K = 0 (только нули) ---
    def test_k_zero(self):
        sa = SimpleAddition(0, "0", "0")
        self.assertEqual(sa.compute(), "0")

    # --- K = 1 ---
    def test_k_one(self):
        # K=1, A="1", B="0" -> "1"
        sa = SimpleAddition(1, "1", "0")
        self.assertEqual(sa.compute(), "1")

    # --- Большие числа (из ЛР1) ---
    def test_big_numbers(self):
        # K=9, A="135", B="77" -> 1+0=1, 3+7=10, 5+7=12 -> "11012"
        sa = SimpleAddition(9, "135", "77")
        self.assertEqual(sa.compute(), "11012")

    # --- Три девятки ---
    def test_triple_nines(self):
        # K=9, A="999", B="999" -> 18, 18, 18 -> "181818"
        sa = SimpleAddition(9, "999", "999")
        self.assertEqual(sa.compute(), "181818")

    # --- Валидация K ---
    def test_k_negative(self):
        with self.assertRaises(ValueError):
            SimpleAddition(-1, "0", "0")

    def test_k_too_big(self):
        with self.assertRaises(ValueError):
            SimpleAddition(10, "0", "0")

    def test_k_float(self):
        with self.assertRaises(TypeError):
            SimpleAddition(5.0, "0", "0")

    def test_k_bool(self):
        with self.assertRaises(TypeError):
            SimpleAddition(True, "0", "0")

    def test_k_none(self):
        with self.assertRaises(TypeError):
            SimpleAddition(None, "0", "0")

    # --- Валидация A и B ---
    def test_a_not_string(self):
        with self.assertRaises(TypeError):
            SimpleAddition(9, 123, "0")

    def test_b_not_string(self):
        with self.assertRaises(TypeError):
            SimpleAddition(9, "0", 123)

    def test_a_not_digits(self):
        with self.assertRaises(ValueError):
            SimpleAddition(9, "abc", "0")

    def test_b_not_digits(self):
        with self.assertRaises(ValueError):
            SimpleAddition(9, "0", "abc")

    def test_a_digit_exceeds_k(self):
        # K=5, A="6" -> 6 > 5 -> ValueError
        with self.assertRaises(ValueError):
            SimpleAddition(5, "6", "0")

    def test_b_digit_exceeds_k(self):
        # K=5, B="7" -> 7 > 5 -> ValueError
        with self.assertRaises(ValueError):
            SimpleAddition(5, "0", "7")

    # --- Коммутативность (A+B == B+A) ---
    def test_commutativity(self):
        sa1 = SimpleAddition(9, "123", "456")
        sa2 = SimpleAddition(9, "456", "123")
        self.assertEqual(sa1.compute(), sa2.compute())


if __name__ == "__main__":
    unittest.main(verbosity=2)