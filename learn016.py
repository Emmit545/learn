class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed!")
        else:
            print(f"Task '{task}' not found!")

    def show_tasks(self):
        if self.tasks:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks in the list.")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo.remove_task(task)
        elif choice == '3':
            todo.show_tasks()
        elif choice == '4':
            print("Exiting To-Do List manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
