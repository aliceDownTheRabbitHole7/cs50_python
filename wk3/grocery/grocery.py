# Init an empty grocery list

grocery_list = {}

while True:

    # Get user input and add to grocery list

    try:
        item = input('Grocery Item: ').upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    # Exit the program and print the list to the console

    except KeyboardInterrupt:
        print()
        print('Grocery List: ')
        for key in sorted(grocery_list.keys()):
            print(grocery_list[key], key)
        break
