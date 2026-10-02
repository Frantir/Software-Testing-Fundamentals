def solve():
    # Чтение данных по одной строке
    K = int(input("Введите K: "))
    A = input("Введите A: ").strip()
    B = input("Введите B: ").strip()

    # Выравнивание длин строк (дополняем нулями слева)
    max_len = max(len(A), len(B))
    A = A.zfill(max_len)
    B = B.zfill(max_len)

    result_digits = []
    
    # Поразрядное сложение
    for i in range(max_len):
        digit_a = int(A[i])
        digit_b = int(B[i])
        sum_digits = digit_a + digit_b
        result_digits.append(str(sum_digits))

    # Сборка результата
    result_str = "".join(result_digits)

    # Удаление ведущих нулей
    final_result = result_str.lstrip('0')
    if not final_result:
        final_result = "0"

    print(f"Результат: {final_result}")

if __name__ == "__main__":
    solve()