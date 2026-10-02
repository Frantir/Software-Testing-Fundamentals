class SimpleAddition:
    """
    Класс для реализации 'простого сложения' чисел A и B
    в системе счисления с ограничением K (0 <= K <= 9).
    Сложение выполняется поразрядно без переноса.
    """

    def __init__(self, K, A, B):
        # Проверка типа K
        if isinstance(K, bool) or not isinstance(K, int):
            raise TypeError("K должно быть целым числом")
        if K < 0 or K > 9:
            raise ValueError("K должно быть в диапазоне от 0 до 9")

        # Проверка типа A и B
        if not isinstance(A, str) or not isinstance(B, str):
            raise TypeError("A и B должны быть строками")

        # Проверка, что A и B состоят только из цифр
        if not A.isdigit() or not B.isdigit():
            raise ValueError("A и B должны состоять только из цифр")

        # Проверка, что все цифры A и B не превышают K
        for ch in A:
            if int(ch) > K:
                raise ValueError(f"Цифра {ch} в числе A превышает K={K}")
        for ch in B:
            if int(ch) > K:
                raise ValueError(f"Цифра {ch} в числе B превышает K={K}")

        self.K = K
        self.A = A
        self.B = B

    def compute(self):
        """
        Выполняет простое сложение.
        Возвращает строку — результат без ведущих нулей.
        """
        # Выравнивание длин
        max_len = max(len(self.A), len(self.B))
        a = self.A.zfill(max_len)
        b = self.B.zfill(max_len)

        result_digits = []
        for i in range(max_len):
            digit_a = int(a[i])
            digit_b = int(b[i])
            sum_digits = digit_a + digit_b
            result_digits.append(str(sum_digits))

        result_str = "".join(result_digits)
        final_result = result_str.lstrip('0')
        if not final_result:
            final_result = "0"
        return final_result