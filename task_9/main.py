from shopping import load_items, add_item, remove_item, clear_items


def show_items():
    items = load_items()
    if not items:
        print("Список пуст.")
        return
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")


def main():
    while True:
        print("\n=== СПИСОК ПОКУПОК ===")
        print("1. Добавить товар")
        print("2. Показать список")
        print("3. Удалить товар")
        print("4. Очистить")
        print("0. Выход")
        choice = input("Выбор: ").strip()

        if choice == "1":
            try:
                add_item(input("Название товара: "))
                print("Добавлено.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            show_items()
        elif choice == "3":
            show_items()
            try:
                n = int(input("Номер для удаления: "))
                removed = remove_item(n - 1)
                print(f"Удалено: {removed}")
            except (ValueError, IndexError) as e:
                print(f"Ошибка: {e}")
        elif choice == "4":
            clear_items()
            print("Список очищен.")
        elif choice == "0":
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()