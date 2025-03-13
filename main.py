# To-Do List Application

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    task = input("Enter the task to add: ")
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Invalid input. Task cannot be empty.")

def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks to view.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        try:
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                delete_task(tasks)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please select a valid menu item.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()