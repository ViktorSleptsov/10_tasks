import json
import os

SHOPPING_FILE = "shopping.json"


def load_items(filename=SHOPPING_FILE):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_items(items, filename=SHOPPING_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def add_item(name, filename=SHOPPING_FILE):
    name = name.strip()
    if not name:
        raise ValueError("Название не может быть пустым")
    items = load_items(filename)
    items.append(name)
    save_items(items, filename)
    return items


def remove_item(index, filename=SHOPPING_FILE):
    items = load_items(filename)
    if index < 0 or index >= len(items):
        raise IndexError("Неверный номер товара")
    removed = items.pop(index)
    save_items(items, filename)
    return removed


def clear_items(filename=SHOPPING_FILE):
    save_items([], filename)