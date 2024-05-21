def main():
    todo_list = []

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.append({"task": task, "completed": False})
            print("Task added successfully!")

        elif choice == "2":
            print("\n===== To-Do List =====")
            for idx, item in enumerate(todo_list, start=1):
                status = "Completed" if item["completed"] else "Pending"
                print(f"{idx}. [{status}] {item['task']}")
            if not todo_list:
                print("No tasks in the list.")

        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_number < len(todo_list):
                todo_list[task_number]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
