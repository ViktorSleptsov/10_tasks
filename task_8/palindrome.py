import re


def normalize(text):
    """Оставляет только буквы и цифры, приводит к нижнему регистру."""
    return re.sub(r"[^\w]", "", text.lower(), flags=re.UNICODE)


def is_palindrome(text):
    cleaned = normalize(text)
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]