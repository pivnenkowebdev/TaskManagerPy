import json
FILENAME = "tasks.json"

# === Работа с файлом ===
def load_tasks():
    """Загружает задачи из файла JSON, если файл есть."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Сохраняет список задач в JSON."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)