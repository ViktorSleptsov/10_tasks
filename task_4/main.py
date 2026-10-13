from password_gen import generate_password


def main():
    print("=== ГЕНЕРАТОР ПАРОЛЕЙ ===")
    try:
        length = int(input("Длина пароля (6-32): "))
        ans = input("Использовать спецсимволы? (y/n): ").strip().lower()
        pwd = generate_password(length, use_special=(ans == "y"))
        print(f"Пароль: {pwd}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()