def add_items():
    item_list = input("Please enter items separated by comma: ")
    item_list = item_list.split(', ')
    unique_items = set()
    non_unique_items = {}

    for item in item_list:
        if item in non_unique_items:
            non_unique_items[item] += 1
        else:
            unique_items.add(item)
            non_unique_items[item] = 1

    non_unique_items = list(non_unique_items.items())
    print("Items are saved")
    print("Unique items:", unique_items)
    print("Not unique items:", tuple(non_unique_items))
while True:
    print("\nPlease chose the task you want to perform:")
    print("1. Enter items")
    print("2. Exit")
    user_choice = input("")
    if user_choice == '1':
        add_items()
    elif user_choice == '2':
        break
    else:
        print("Invalid input. Please try again.")