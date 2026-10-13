import random
import string


def generate_password(length, use_special=False):
    if not isinstance(length, int):
        raise ValueError("Длина должна быть целым числом")
    if length < 6 or length > 32:
        raise ValueError("Длина должна быть от 6 до 32")

    alphabet = string.ascii_letters + string.digits
    if use_special:
        alphabet += "!@#$%^&*()-_=+"

    return "".join(random.choice(alphabet) for _ in range(length))