#To-do list app 

def main():
    task = []
    def show_menu():  
     while True:   
        print("\n===To-do List===")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            print()
            n_task = int(input("How many task you want to add: "))

            for i in range(n_task):
                task = input("Enter the task: ")
                task.append({"task": task, "Done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks")
            for index, task in enumerate(task):
                status = "Done" if task["Done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")
            
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(task):
                task[task_index] ["Done"] = True
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