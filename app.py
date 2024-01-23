user_input = "random"
data = []

def show_menu():
    print("Menu:")
    print("1. Add an item")
    print("2. Mark as Done")
    print("3. View items")
    print("4. Exit")

while user_input != '4':
    
    show_menu()
    user_input = input("Enter your choice: ")
    
    if user_input == '1':
        #print('Add an item')
        item = input("What is to be done? ")
        data.append(item)
        print("Added item", item)
    elif user_input == '2':
        #print('Mark as Done')
        item = input("What is to be marked as done? ")
        if item in data:
            data.remove(item)
            print("Removed item: ", item)
        else:
            print("Item not exist in the list")
    elif user_input== '3':
        print('List of todo items')
        for item in data:
            print(item)
    elif user_input == '4':
        print('Goodbye!')
    else:
        print('Please enter 1,2,3 or 4')

