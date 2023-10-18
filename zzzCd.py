import os
import datetime


class Task:
    def __init__(self, id, description, priority, due_date=None, completed=False):
        self.id = id
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def is_done(self):
        return self.completed

    def __str__(self):
        status = "incomplete" if not self.is_done() else "complete"
        return f"{self.id}. {self.description}\t\t{status}\t\t{self.priority}\t\t{self.due_date}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority=None, due_date=None):
        # Adds a new task to the to-do list.

        # Args:
        #   task: The task description.
        #   priority: The task priority (high, medium, or low).
        #   due_date: The task due date (datetime object).

        if priority is not None:
            if priority not in ["high", "medium", "low"]:
                print("Error: Invalid task priority.")
                exit(1)

            task.priority = priority

        task.due_date = due_date
        if due_date is not None:
            task.due_date = due_date

        self.tasks.append(task)

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                break

    def mark_task_as_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                break

    def mark_task_as_incomplete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = False
                break

    def get_all_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.is_done()]

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.is_done()]

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    def display_task(self, task_id):
        task = self.get_task(task_id)
        if task is not None:
             print(f"{task.id}. {task.description}\t\t{task.due_date}\t\t{task.priority}\t\t{convert_bool_to_string(task.completed)}")
        else:
             print("Task not found.")
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    def list_all_tasks(self):
        for task in self.get_all_tasks():
            print(f"{task.id}. {task.description}\t\t{task.due_date}\t\t{task.priority}\t\t{convert_bool_to_string(task.completed)}")



def add_due_date_to_task(self, task_id):
    task = self.get_task(task_id)
    if task is not None:
        due_date_str = input("Enter task due date (yyyy-mm-dd): ")
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid due date format.")
            exit(1)

        task.due_date = due_date

def save_to_file(todo_list, filename):
    with open(filename, "w") as f:
        for task in todo_list.get_all_tasks():
            f.write(f"{task.id},{task.description},{task.priority},{task.completed}\n")


def load_from_file(filename):
    todo_list = TodoList()
    with open(filename, "r") as f:
        for line in f:
            task_values = line.strip().split(",")
            task_id = int(task_values[0])
            task_description = task_values[1]
            task_priority = task_values[2]
            #task_completed = (task_values[3] == "True")
            if len(task_values) >= 4:
                task_completed = (task_values[3] == "True")
            else:
                task_completed = False

            task = Task(task_id, task_description, task_priority, task_completed)
            todo_list.add_task(task)
    return todo_list


def convert_bool_to_string(bool_value):
    if bool_value:
        return "completed"
    else:
        return "incompleted"


def print_menu():
    print("To-Do List")
    print("----------")
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task as completed")
    print("4. List all tasks")
    print("5. List completed tasks")
    print("6. List incomplete tasks")
    print("7. List tasks by priority")
    print("8. Exit")
    print("9. Add due date to task")


def main():
    filename = "todo.txt"

    if not os.path.exists(filename):
        todo_list = TodoList()
    else:
        todo_list = load_from_file(filename)

    while True:
        print_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            task_priority = input("Enter task priority (high, medium, or low): ")
            todo_list.add_task(Task(len(todo_list.get_all_tasks()), task_description, task_priority))
        elif choice == "2":
            task_id = int(input("Enter task ID: "))
            todo_list.remove_task(task_id)
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            todo_list.mark_task_as_completed(task_id)
        elif choice == "4":
            for task in todo_list.get_all_tasks():
                print(f"{task.id}. {task.description}\t\t{convert_bool_to_string(task.completed)}\t\t{task.priority}")
        elif choice == "5":
            for task in todo_list.get_completed_tasks():
                print(f"{task.id}. {task.description}\t\t{convert_bool_to_string(task.completed)}\t\t{task.priority}")
        elif choice == "6":
            for task in todo_list.get_incomplete_tasks():
                print(f"{task.id}. {task.description}\t\t{convert_bool_to_string(task.completed)}\t\t{task.priority}")
        elif choice == "7":
            # List tasks by priority
            priority = input("Enter task priority (high, medium, or low): ")
            for task in todo_list.get_tasks_by_priority(priority):
                print(f"{task.id}. {task.description}\t\t{convert_bool_to_string(task.completed)}\t\t{task.priority}")
            break
        elif choice == "8":
            exit(0)
        elif choice == "9":
            task_id = int(input("Enter task ID: "))
            task = todo_list.get_task_by_id(task_id)

            due_date = input("Enter due date (YYYY-MM-DD): ")
            task.due_date = datetime.date.fromisoformat(due_date)
        else:
            print("Invalid choice.")

        save_to_file(todo_list, filename)







if __name__ == "__main__":
    main()

    
