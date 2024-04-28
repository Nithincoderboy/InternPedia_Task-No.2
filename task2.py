# Task2 - TO DO LIST
import os

# Function to display the menu
def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Mark task as undone")
    print("5. Remove task")
    print("6. Exit")

# Function to load tasks from file
def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                task, status = line.strip().split(',')
                tasks.append((task, status))
    return tasks

# Function to save tasks to file
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task, status in tasks:
            file.write(f"{task},{status}\n")

# Function to view tasks
def view_tasks(tasks):
    if tasks:
        print("\n===== Your Tasks =====")
        for i, (task, status) in enumerate(tasks, start=1):
            print(f"{i}. [{status}] {task}")
    else:
        print("\nNo tasks found.")

# Function to add a new task
def add_task(tasks, task):
    tasks.append((task, "Incomplete"))

# Function to mark a task as done or undone
def mark_task(tasks, index, status):
    tasks[index] = (tasks[index][0], status)

# Function to remove a task
def remove_task(tasks, index):
    del tasks[index]

# Main function
def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':  # View tasks
            view_tasks(tasks)
        elif choice == '2':  # Add task
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
            print("Task added successfully.")
        elif choice == '3':  # Mark task as done
            view_tasks(tasks)
            index = int(input("Enter the index of the task to mark as done: ")) - 1
            mark_task(tasks, index, "Complete")
            print("Task marked as done.")
        elif choice == '4':  # Mark task as undone
            view_tasks(tasks)
            index = int(input("Enter the index of the task to mark as undone: ")) - 1
            mark_task(tasks, index, "Incomplete")
            print("Task marked as undone.")
        elif choice == '5':  # Remove task
            view_tasks(tasks)
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(tasks, index)
            print("Task removed successfully.")
        elif choice == '6':  # Exit
            save_tasks(tasks, filename)
            print("Thank you for using the to-do list. Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
