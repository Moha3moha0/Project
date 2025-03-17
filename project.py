class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def __str__(self):
        return f"Task: {self.name} - Status: {'Completed' if self.completed else 'Pending'}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(Task(task_name))

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return
        print(f"Task '{task_name}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def linear_search(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    def bubble_sort(self):
        n = len(self.tasks)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.tasks[j].name > self.tasks[j+1].name:
                    self.tasks[j], self.tasks[j+1] = self.tasks[j+1], self.tasks[j]


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. Mark Task as Completed\n3. Display All Tasks\n4. Search Task by Name\n5. Sort Tasks\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)

        elif choice == "2":
            task_name = input("Enter task name to mark as completed: ")
            todo_list.mark_completed(task_name)

        elif choice == "3":
            todo_list.display_tasks()

        elif choice == "4":
            task_name = input("Enter task name to search for: ")
            task = todo_list.linear_search(task_name)
            if task:
                print(f"Task found: {task}")
            else:
                print(f"Task '{task_name}' not found.")

        elif choice == "5":
            todo_list.bubble_sort()
            print("Tasks sorted.")

        elif choice == "6":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()