from database import DB

def main():
    dbObject = DB()
    while True:
        display_menu()
        try:
            userInput = int(input("Please enter menu option: "))
            if userInput == 9:
                print("Quitting the program. Goodbye!")
                break  # Exit the loop and the program
            process_user_input(userInput, dbObject)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def display_menu():
    print("\nWelcome to the Database Management System!")
    print("Here is what is on the menu:")
    print("1 - Create a New Database")
    print("2 - Open an Existing Database")
    print("3 - Close the Database")
    print("4 - Display a Record")
    print("5 - Update a Record")
    print("6 - Create a report")
    print("7 - Add a Record")
    print("8 - Delete a Record")
    print("9 - Quit the Program")

def process_user_input(userInput, dbObject):
    if userInput == 1:
        print("You have chosen to create a new database.")
        # Call a function to create a new database
    elif userInput == 2:
        print("You have chosen to open an existing database.")
        # Call a function to open an existing database
    elif userInput == 3:
        print("You have chosen to close the database.")
        # Call a function to close the database
    elif userInput == 4:
        print("You have chosen to display a record.")
        # Call a function to display a record
    elif userInput == 5:
        print("You have chosen to update a record in the database.")
        # Call a function to update a record
    elif userInput == 6:
        print("You have chosen to create a report for the database.")
        # Call a function to create a report
    elif userInput == 7:
        print("You have chosen to add a record to the database.")
        # Call a function to add a record
    elif userInput == 8:
        print("You have chosen to delete a record from the database.")
        # Call a function to delete a record
    else:
        print("Invalid option. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
