from palindrome import is_palindrome


def main():
    print("=== ПАЛИНДРОМ ===")
    text = input("Введите текст: ")
    if is_palindrome(text):
        print("✔ Это палиндром!")
    else:
        print("✘ Это не палиндром.")


if __name__ == "__main__":
    main()