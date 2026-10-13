from converter import convert


def main():
    print("=== КОНВЕРТЕР ВАЛЮТ ===")
    try:
        amount = float(input("Сумма в рублях: "))
        currency = input("Валюта (USD/EUR/CNY): ")
        result = convert(amount, currency)
        print(f"Результат: {result:.2f} {currency.upper()}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()