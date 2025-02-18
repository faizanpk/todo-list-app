# simple To-Do list app

lst = []

def add_task():
    ask_user = input("Enter a task: ")
    lst.append(ask_user)
    print(f"Task added: {ask_user}")

def remove_task():
    show_task()
    if not lst:
        return 
    
    try:
        ask_user = int(input("Enter a index of the task to remove: "))
        if 0 <= ask_user <= len(lst):
            task_removed = lst.pop(ask_user)
            print(f"Task removed: {task_removed}")
        else:
            print("Invalid index! Please enter a valid number.")
    
    except ValueError:
        print("Please enter a valid number.")

def show_task():
    if not lst:
        print("No tasks found!")
    else:
        print("Your To-Do list:")
        for i, task in enumerate(lst):
            print(f"{i}. {task}")
        
def main():
    while True:
        print("Options: [1] View tasks [2] Add task [3] Remove task [4] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
        else:
            print("Invalid choice. Please select again")

if __name__ == "__main__":
    main()