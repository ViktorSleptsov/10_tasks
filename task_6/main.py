from notes import add_note, read_notes, clear_notes


def show_notes():
    notes = read_notes()
    if not notes:
        print("Заметок нет.")
    else:
        for i, n in enumerate(notes, 1):
            print(f"{i}. {n}")


def main():
    while True:
        print("\n=== ЗАМЕТКИ ===")
        print("1. Добавить")
        print("2. Показать")
        print("3. Очистить")
        print("0. Выход")
        choice = input("Выбор: ").strip()

        if choice == "1":
            try:
                text = input("Текст заметки: ")
                add_note(text)
                print("Заметка добавлена.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            show_notes()
        elif choice == "3":
            clear_notes()
            print("Все заметки удалены.")
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()