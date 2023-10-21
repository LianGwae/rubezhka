to_do_list = []
completed_tasks = []
while True:
    print("\nPlease chose the task you want to perform:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View All Completed Tasks")
    print("5. Exit")
    user_choice = input("")
    if user_choice == '1':
        task_name = input("Enter the task: ")
        to_do_list.append(task_name)
        print("The task “{}” was added to the todo list".format(task_name))
    elif user_choice == '2':
        print("\nTo-Do List:")
        for i, task in enumerate(to_do_list):
            print(f"{i+1}. {task}")
    elif user_choice == '3':
        task_name = input("Enter the name of the task: ")
        for task in to_do_list:
            if task == task_name:
                to_do_list.remove(task)
                completed_tasks.append(task)
                print("The task {} is marked as completed".format(task_name))
                break
        else:
            print("The task {} is not in the todo list".format(task_name))
    elif user_choice == '4':
        print("\nCompleted Tasks:")
        for i, task in enumerate(completed_tasks):
            print(f"{i+1}. {task}")
    elif user_choice == '5':
        break
    else:
        print("Invalid input. Please try again.")