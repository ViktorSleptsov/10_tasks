def parse_numbers(text):
    """Преобразует строку '5 2 9' в список чисел."""
    if not text.strip():
        raise ValueError("Список пуст")
    parts = text.split()
    try:
        return [float(p) for p in parts]
    except ValueError:
        raise ValueError("Все элементы должны быть числами")


def sort_asc(numbers):
    return sorted(numbers)


def sort_desc(numbers):
    return sorted(numbers, reverse=True)


def stats(numbers):
    if not numbers:
        raise ValueError("Список пуст")
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
    }