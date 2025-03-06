# create a list to store shopping items
shopping_list = []

while True:
    print("\nSHOPPING LIST")
    print("What would you like to do: \n")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View your shopping list\n")

    choice = int(input("Enter your choice(1/2/3): "))

    if choice == 1:
        new_item = input("What would you like to add: ")
        shopping_list.append(new_item)
        print(f"{new_item} has been added to your shopping list.")
        print(shopping_list)
    elif choice == 2:
        del_item = input("Which item would you like to remove: ").lower()

        if (len(shopping_list) == 0):
            print("Your shopping list is empty.")
        else:

            if del_item in shopping_list:
                shopping_list.remove(del_item)
                print(f"{del_item} has been removed to your shopping list.")
                print(shopping_list)
            else:
                print(f"{del_item} is not in your shopping list")
                print(shopping_list)

    elif choice == 3:

        if (len(shopping_list) == 0):
            print("No items in your shopping list")
        else:
            for item in shopping_list:
                print(item)

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")


    break




