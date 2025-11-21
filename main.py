# ветка ООП после уроков ООП

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

# === Основные функции ===
def add_task(tasks):
    print("\nДобавление задачи")
    name = input("Название задачи: ")
    priority = input("Приоритет (низкий / средний / высокий): ")
    date = input("Дата выполнения (ГГГГ-ММ-ДД): ")

    task = {
        "name": name,
        "priority": priority,
        "date": date
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Задача добавлена!")

def remove_task(tasks):
    print("\nУдаление задачи")
    show_tasks(tasks)
    keyword = input("Введите номер задачи или слово из названия: ")

    if keyword.isdigit():
        index = int(keyword) - 1  # Нумерация с 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Удалена задача: {removed['name']}")
        else:
            print("Неверный номер задачи.")
    else:
        for task in tasks:
            if keyword.lower() in task["name"].lower():
                tasks.remove(task)
                print(f"Удалена задача: {task['name']}")
                save_tasks(tasks)
                return
        print("Задача не найдена.")
    save_tasks(tasks)

def edit_task(tasks):
    print("\nРедактирование задачи")
    show_tasks(tasks)
    try:
        number = int(input("Введите номер задачи для редактирования: "))
        index = number - 1
        task = tasks[index]
    except (ValueError, IndexError):
        print("Ошибка: неверный номер задачи.")
        return

    print(f"Редактируется задача: {task['name']}")
    new_name = input("Новое название (Enter — оставить без изменений): ")
    new_priority = input("Новый приоритет (Enter — оставить без изменений): ")
    new_date = input("Новая дата (Enter — оставить без изменений): ")

    if new_name:
        task["name"] = new_name
    if new_priority:
        task["priority"] = new_priority
    if new_date:
        task["date"] = new_date

    save_tasks(tasks)
    print("Задача обновлена!")

def show_tasks(tasks):
    print("\nСписок задач:")
    if not tasks:
        print("Нет задач.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} | Приоритет: {task['priority']} | Дата: {task['date']}")

def search_tasks(tasks):
    print("\nПоиск задачи")
    keyword = input("Введите слово для поиска: ").lower()
    found_tasks = []

    for task in tasks:
        if keyword in task["name"].lower():
            found_tasks.append(task)

    if found_tasks:
        print("\nНайдено:")
        for i, task in enumerate(found_tasks, start=1):
            print(f"{i}. {task['name']} | Приоритет: {task['priority']} | Дата: {task['date']}")
    else:
        print("Задачи не найдены.")

# === Главное меню ===
def main():
    tasks = load_tasks()

    while True:
        print("\nМеню:")
        print("1 — добавить задачу")
        print("2 — удалить задачу")
        print("3 — редактировать задачу")
        print("4 — показать все задачи")
        print("5 — поиск задачи")
        print("0 — выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            show_tasks(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
