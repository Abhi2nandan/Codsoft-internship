# To-Do List Program

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['name']} [{status}]")

def add_task(tasks):
    task_name = input("\nEnter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added to the list.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['name']}' removed from the list.")
        except (ValueError, IndexError):
            print("Invalid task number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to mark as completed: "))
            tasks[task_num - 1]['completed'] = True
            print(f"Task '{tasks[task_num - 1]['name']}' marked as completed.")
        except (ValueError, IndexError):
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

