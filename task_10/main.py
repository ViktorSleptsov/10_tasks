from season import parse_date, get_season, get_weekday, days_to_end_of_year


def main():
    print("=== ВРЕМЯ ГОДА ===")
    try:
        d = parse_date(input("Введите дату (ДД.ММ.ГГГГ): "))
        print(f"Время года: {get_season(d)}")
        print(f"День недели: {get_weekday(d)}")
        print(f"До конца года: {days_to_end_of_year(d)} дней")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()