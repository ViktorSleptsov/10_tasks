def calculate_bmi(weight, height):
    if weight <= 0:
        raise ValueError("Вес должен быть положительным")
    if height <= 0:
        raise ValueError("Рост должен быть положительным")
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Недостаток"
    elif bmi < 25:
        return "Норма"
    elif bmi < 30:
        return "Избыток"
    return "Ожирение"