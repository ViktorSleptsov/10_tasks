import os
from datetime import datetime

NOTES_FILE = "notes.txt"


def add_note(text, filename=NOTES_FILE):
    """Добавляет заметку с датой в конец файла."""
    text = text.strip()
    if not text:
        raise ValueError("Заметка не может быть пустой")
    date = datetime.now().strftime("%d.%m.%Y %H:%M")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{date}] {text}\n")


def read_notes(filename=NOTES_FILE):
    """Возвращает список строк с заметками."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def clear_notes(filename=NOTES_FILE):
    """Удаляет все заметки (очищает файл)."""
    if os.path.exists(filename):
        os.remove(filename)