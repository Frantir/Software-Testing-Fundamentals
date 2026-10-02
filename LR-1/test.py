import subprocess
import sys

def run_test(input_data):
    # Запускаем main.py как отдельный процесс, передавая данные на вход
    process = subprocess.Popen(
        [sys.executable, 'main.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_data)
    return stdout.strip()

def main():
    print("=== Тестирование задачи 'Простое сложение' ===")
    
    # Корректные тесты
    test_cases = [
        (4, "1", "3", "4"),
        (9, "12", "34", "46"),
        (9, "99", "11", "1010"),
        (0, "0", "0", "0"),
        (9, "123", "456", "579"),
        (1, "1", "0", "1"),
        (9, "0012", "0034", "46"),
        (9, "999", "999", "181818"),
        (9, "135", "77", "11012"),
    ]

    for K, A, B, expected in test_cases:
        input_str = f"{K}\n{A}\n{B}\n"
        result = run_test(input_str)
        status = "OK" if result == expected else f"FAIL (ожидалось {expected}, получено {result})"
        print(f"Тест K={K}, A={A}, B={B}: {status}")

if __name__ == "__main__":
    main()