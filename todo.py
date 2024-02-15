import json
from datetime import datetime

def load_todo_list():
    try:
        with open('todo_list.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todo_list(todo_list):
    with open('todo_list.json', 'w') as file:                                               
        json.dump(todo_list, file)

def add_task(todo_list):
    task = input("Enter the task: ")
    due_date_str = input("Enter the due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Task will be added without a due date.")
        due_date = None

    todo_list.append({'task': task, 'due_date': due_date, 'completed': False})
    print("Task added successfully.")

def mark_complete(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the index of the task to mark as complete: "))

    if 0 <= index < len(todo_list):
        todo_list[index]['completed'] = True
        print("Task marked as complete.")
    else:
        print("Invalid index.")

def view_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
        return

    print("To-Do List:")
    for i, task in enumerate(todo_list, start=1):
        status = "[ ]" if not task['completed'] else "[X]"
        due_date = f" (Due: {task['due_date']})" if task['due_date'] else ""
        print(f"{i}. {status} {task['task']}{due_date}")

def delete_task(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the index of the task to delete: "))

    if 0 <= index < len(todo_list):
        del todo_list[index]
        print("Task deleted.")
    else:
        print("Invalid index.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View To-Do List")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice-----------(1-5): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            mark_complete(todo_list)
        elif choice == '3':
            view_todo_list(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            save_todo_list(todo_list)
            print("Exiting the To-Do List application.")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
     