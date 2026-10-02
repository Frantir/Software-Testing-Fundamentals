class Factorial:
    """
    Класс для вычисления факториала неотрицательного целого числа.
    """

    def __init__(self, n):
        # Проверка типа: bool — подкласс int, поэтому проверяем отдельно
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("n должно быть целым числом")
        if n < 0:
            raise ValueError("n не может быть отрицательным")
        self.n = n

    def compute(self):
        """Итеративное вычисление факториала."""
        result = 1
        for i in range(2, self.n + 1):
            result *= i
        return result

    def compute_recursive(self):
        """Рекурсивная реализация — для сравнения."""
        if self.n <= 1:
            return 1
        return self.n * Factorial(self.n - 1).compute_recursive()