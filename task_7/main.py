from sorter import parse_numbers, sort_asc, sort_desc, stats


def main():
    print("=== СОРТИРОВКА СПИСКА ===")
    try:
        text = input("Введите числа: ")
        nums = parse_numbers(text)
        print(f"По возрастанию: {sort_asc(nums)}")
        print(f"По убыванию:   {sort_desc(nums)}")
        s = stats(nums)
        print(f"Минимум: {s['min']}, Максимум: {s['max']}, "
              f"Сумма: {s['sum']}, Среднее: {s['avg']:.1f}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()