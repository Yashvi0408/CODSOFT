def main():
    tasks = []
    while True:
        print("\n===To-do List===")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            print()
            n_task = int(input("How many tasks do you want to add: "))
            for i in range(n_task):
                task_desc = input("Enter the task: ")
                tasks.append({"task": task_desc, "Done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks")
            if not tasks:
                print("No tasks to show.")
            for index, t in enumerate(tasks):
                status = "Done" if t["Done"] else "Not Done"
                print(f"{index + 1}. {t['task']} - {status}")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done.")
                continue
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["Done"] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()