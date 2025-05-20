import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "completed": self.completed
        }

    def __str__(self):
        status = "✅" if self.completed else "❌"
        due = f" | Due: {self.due_date}" if self.due_date else ""
        return f"{status} {self.title}{due}"

class ToDoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(**task) for task in data]

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self):
        title = input("Enter task title: ")
        due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
        if due_date == "":
            due_date = None
        else:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Skipping due date.")
                due_date = None
        self.tasks.append(Task(title, due_date))
        self.save_tasks()
        print("✅ Task added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def mark_done(self):
        self.list_tasks()
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].completed = True
                self.save_tasks()
                print("✅ Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")

    def update_task(self):
        self.list_tasks()
        try:
            index = int(input("Enter task number to update: ")) - 1
            if 0 <= index < len(self.tasks):
                title = input("Enter new title: ")
                due_date = input("Enter new due date (YYYY-MM-DD): ")
                if due_date == "":
                    due_date = None
                else:
                    try:
                        datetime.strptime(due_date, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date. Skipping due date update.")
                        due_date = self.tasks[index].due_date
                self.tasks[index].title = title
                self.tasks[index].due_date = due_date
                self.save_tasks()
                print("✅ Task updated.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")

    def delete_task(self):
        self.list_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
                self.save_tasks()
                print("✅ Task deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")

    def show_pending_tasks(self):
        pending = [task for task in self.tasks if not task.completed]
        if not pending:
            print("All tasks completed!")
        else:
            print("\nPending Tasks:")
            for idx, task in enumerate(pending, 1):
                print(f"{idx}. {task}")

    def show_completed_tasks(self):
        done = [task for task in self.tasks if task.completed]
        if not done:
            print("No completed tasks yet.")
        else:
            print("\nCompleted Tasks:")
            for idx, task in enumerate(done, 1):
                print(f"{idx}. {task}")

    def sort_by_due_date(self):
        dated_tasks = [task for task in self.tasks if task.due_date]
        if not dated_tasks:
            print("No tasks with due dates.")
            return
        sorted_tasks = sorted(dated_tasks, key=lambda t: t.due_date)
        print("\nTasks sorted by due date:")
        for idx, task in enumerate(sorted_tasks, 1):
            print(f"{idx}. {task}")

    def clear_all(self):
        confirm = input("Are you sure you want to delete all tasks? (yes/no): ")
        if confirm.lower() == "yes":
            self.tasks.clear()
            self.save_tasks()
            print("🗑️ All tasks cleared.")
        else:
            print("Operation cancelled.")

def main_menu():
    app = ToDoApp()
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. View Pending Tasks")
        print("7. View Completed Tasks")
        print("8. Sort Tasks by Due Date")
        print("9. Clear All Tasks")
        print("10. Exit")
        choice = input("Select an option (1-10): ")

        if choice == '1':
            app.add_task()
        elif choice == '2':
            app.list_tasks()
        elif choice == '3':
            app.mark_done()
        elif choice == '4':
            app.update_task()
        elif choice == '5':
            app.delete_task()
        elif choice == '6':
            app.show_pending_tasks()
        elif choice == '7':
            app.show_completed_tasks()
        elif choice == '8':
            app.sort_by_due_date()
        elif choice == '9':
            app.clear_all()
        elif choice == '10':
            print("Exiting... ✅")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
