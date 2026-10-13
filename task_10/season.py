from datetime import datetime, date


def parse_date(text):
    """Принимает строку ДД.ММ.ГГГГ, возвращает date."""
    try:
        return datetime.strptime(text.strip(), "%d.%m.%Y").date()
    except ValueError:
        raise ValueError("Неверный формат даты. Ожидается ДД.ММ.ГГГГ")


def get_season(d):
    month = d.month
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    return "Осень"


WEEKDAYS_RU = ["Понедельник", "Вторник", "Среда",
               "Четверг", "Пятница", "Суббота", "Воскресенье"]


def get_weekday(d):
    return WEEKDAYS_RU[d.weekday()]


def days_to_end_of_year(d):
    end = date(d.year, 12, 31)
    return (end - d).days