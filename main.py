from database import DB

def main():
    db = DB()
    while True:
        display_menu()
        try:
            userInput = int(input("Please enter menu option: "))
            if userInput == 9:
                print("Quitting the program. Goodbye!")
                break  # Exit the loop and the program
            process_user_input(userInput, db)
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
    print("10 - Read Record Test")

def process_user_input(userInput, db):
    if userInput == 1:
        print("You have chosen to create a new database.")
        filename = input("please input the name of the csv file: ")
        db.createDatabase(filename)
        
    elif userInput == 2:
        print("You have chosen to open an existing database.")
        if not db.isOpen():
            filename = input("please input the name of the database you would like to open: ")
            db.open(filename)
        else:
            print("Database is already open. Please close the previous database before opening a new one.")
        
    elif userInput == 3:
        print("You have chosen to close the database.")
        db.close()
        
    elif userInput == 4:
        print("You have chosen to display a record.")
        recordNum = int(input("please input the record number you would like to view: "))
        db.binarySearch(recordNum)
        
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
        
    elif userInput == 10:
        print("Testing Read Record Function")
        recordNum = int(input("Please input the Id you would like to test: "))
        db.readRecord(recordNum)
    else:
        print("Invalid option. Please enter a number between 1 and 9.")



if __name__ == "__main__":
    main()
