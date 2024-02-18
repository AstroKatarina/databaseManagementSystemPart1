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
            userInput = 0
            
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
            print("\nDatabase is already open. Please close the previous database before opening a new one.")
        
    elif userInput == 3:
        if not db.isOpen():
            print("\nNo database Open, Please open a database")
        else:    
            print("You have chosen to close the database.")
            db.close()
        
    elif userInput == 4:
        print("You have chosen to display a record.")
        if not db.isOpen():
            print("\nPlease open the database before searching for a record")
        else:
            recordNum = int(input("please input the Id of the passenger you would like to view: "))
            db.binarySearch(recordNum)
        
    elif userInput == 5:
        print("You have chosen to update a record in the database.")
        if not db.isOpen():
            print("\nPlease open a database before updating")
        else:
<<<<<<< HEAD
            ID = int(input("please input the passenger Id to update: "))
            # Search for the record number corresponding to the given ID
            recordNum = db.binarySearch(ID)
            if recordNum is not None:
                fname = input("please input the updated passenger's first name: ")
                lname = input("please input the updated passenger's last name: ")
                age = input("please input the updated passenger's age: ")
                ticketNum = input("please input the updated passenger's ticket number: ")
                fare = input("please input the updated passenger's fare: ")
                date = input("please input the date of purchase for the updated passenger: ")
                # Call writeRecord with the found recordNum
                db.writeRecord(recordNum, ID, fname, lname, age, ticketNum, fare, date)
            else:
                print("Passenger ID not found.") 
        return
    
=======
            ID = input("\nplease input the passenger Id to update: ")
            fname = input("please input the updated passengers first name: ")
            lname = input("please input the updated passengers last name: ")
            age = input("please input the updated passengers age: ")
            ticketNum = input("please input the updated passengers ticket number: ")
            fare = input("please input the updated passengers fare: ")
            date = input("please input the date of purchase for the updated passenger: ")
            db.updateRecord(ID, fname, lname, age, ticketNum, fare, date)
        
>>>>>>> e3137e9108408ed3215774830e3ccc26dae682af
    elif userInput == 6:
        print("You have chosen to create a report for the database.")
        # Call a function to create a report
        db.createRecord()
        
    elif userInput == 7:
        print("You have chosen to add a record to the database.")
        if not db.isOpen():
            print("\nPlease open a database before adding a record")
        else:
            ID = input("\nplease input the passenger Id to add: ")
            fname = input("please input the new passengers first name: ")
            lname = input("please input the new passengers last name: ")
            age = input("please input the new passengers age: ")
            ticketNum = input("please input the new passengers ticket number: ")
            fare = input("please input the new passengers fare: ")
            date = input("please input the date of purchase for the new passenger: ")
            db.addRecord(ID, fname, lname, age, ticketNum, fare, date)
        
    elif userInput == 8:
        print("You have chosen to delte a record from the database.")
        if not db.isOpen():
            print("\nPlease open a database before deleting a record")
        else:
            ID = input("Please input the record that you would like to delete: ")
            db.deleteRecord(ID)

    else:
        print("Invalid option. Please enter a number between 1 and 9.")



if __name__ == "__main__":
    main()
