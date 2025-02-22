# To-Do List

def todo_add(todo):
    item = input("Enter your ToDo Task: ")
    todo.append(item)
    print(f"{item} Item added to To-Do")

def todo_remove(todo):
    view(todo)
    while True:
        try:
            task_index = int(input("enter task number to remove: "))
            if task_index >= 1 and task_index <= len(todo):
                removed_task = todo.pop(task_index-1)
                print(f"Task {removed_task} removed")
                break
            else:
                print("Invalid task number. Try again")

        except ValueError:
            print("Invalid. Enter vlaid Number")
    

def view(todo):
    if not todo:
        print("Empty To-Do List")
    else:
        print("Tasks : ")

        for index, task in enumerate(todo):
            print(f"Task {index+1} --> {task}\n")
        


def main():

    todo = []

    # input("************* Welcome to To-Do List **************")

    while True: 
        input("\n1. Add Task to To-Do List \n2. View Items in my To-Do List \n3. Remove Item from To-Do List  \n4. Break the Loop (Exit)\n")
        choice = input("Select the Task from above: ")

        if choice == '1':
            todo_add(todo)
        elif choice == '2':
            view(todo)
        elif choice == '3':
            todo_remove(todo)
        elif choice == '4':
            break
        else:
            print("Wrong Input given. Please Try Again--")

if __name__ == "__main__":
    main()
        



