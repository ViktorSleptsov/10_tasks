from number_to_words import number_to_words


def main():
    print("=== ЧИСЛО ПРОПИСЬЮ ===")
    try:
        n = int(input("Введите число (1-1000): "))
        print(number_to_words(n))
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()