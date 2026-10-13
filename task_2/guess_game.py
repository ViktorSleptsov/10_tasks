import random


def make_secret(low=1, high=100):
    return random.randint(low, high)


def check_guess(secret, guess):
    """Возвращает 'more', 'less' или 'win'."""
    if guess < secret:
        return "more"
    elif guess > secret:
        return "less"
    return "win"


def play(secret, input_func=input, output_func=print):
    """Игровой цикл. Возвращает число попыток или None при выходе."""
    output_func("Я загадал число от 1 до 100. Угадай!")
    attempts = 0
    while True:
        raw = input_func("Твой вариант: ").strip()
        if raw.lower() == "exit":
            output_func("Выход.")
            return None
        try:
            guess = int(raw)
        except ValueError:
            output_func("Введи целое число или 'exit'.")
            continue

        attempts += 1
        result = check_guess(secret, guess)
        if result == "win":
            output_func(f"🎉 Угадал за {attempts} попытки!")
            return attempts
        elif result == "more":
            output_func("Больше!")
        else:
            output_func("Меньше!")