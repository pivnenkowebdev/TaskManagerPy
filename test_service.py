from storage.json_storage import JsonStorage
from services.task_service import TaskService
import os

TEST_FILE = "test_tasks.json"

if os.path.exists(TEST_FILE):
    os.remove(TEST_FILE)

storage = JsonStorage(TEST_FILE)
service = TaskService(storage)

print("=== Добавляем задачи ===")

t1 = service.add_task("Task 1", "High", "2026-01-01")
t2 = service.add_task("Task 2", "Low", "2026-01-02")

print("ID первой:", t1.id)
print("ID второй:", t2.id)

print("=== Удаляем первую ===")
service.delete_task(t1.id)

print("=== Добавляем новую ===")
t3 = service.add_task("Task 3", "Medium", "2026-01-03")
print("ID новой:", t3.id)

print("=== Перезапуск сервиса ===")
service = TaskService(storage)
t4 = service.add_task("Task 4", "High", "2026-01-04")
print("ID после перезапуска:", t4.id)