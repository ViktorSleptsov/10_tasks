from bmi import calculate_bmi, bmi_category


def main():
    print("=== КАЛЬКУЛЯТОР ИМТ ===")
    try:
        w = float(input("Вес (кг): "))
        h = float(input("Рост (м): "))
        bmi = calculate_bmi(w, h)
        print(f"Ваш ИМТ: {bmi:.2f} — {bmi_category(bmi)}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()