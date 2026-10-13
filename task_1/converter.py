RATES = {
    "USD": 92.0,
    "EUR": 100.0,
    "CNY": 12.7,
}


def convert(amount_rub, currency):
    """Переводит рубли в указанную валюту по фиксированному курсу."""
    currency = currency.upper().strip()
    if currency not in RATES:
        raise ValueError(f"Неизвестная валюта: {currency}")
    if amount_rub < 0:
        raise ValueError("Сумма не может быть отрицательной")
    return amount_rub / RATES[currency]