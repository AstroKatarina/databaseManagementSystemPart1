from database import DB
dbObject = DB()

#Display Menu Options
print ("Welcome to Katarina's Database Management System!\n")
print ("Here is what is on the menu\n")
print ("Press 1 to Create a New Database.\nPress 2 to Open an Existing Database.")
print ("Press 3 to Close the Database.\nPress 4 to Display a Record.")
print ("Press 5 to Update a Record.\nPress 6 to Create a Record.")
print ("Press 7 to Add a Record.\nPress 8 to Delete a Record.\nPress 9 to Quit the Program.\n")

#Take User Menu Input
while True:
	try:
		userInput = int(input("Please enter menu option now: "))
		break  # exit the loop if conversion to integer is successful
	except ValueError:
		print("Invalid input. Please enter a number.")

#Create Menu
while userInput != 9:
	if userInput == 1:
		print ("You have chosen to create a new database. ")
		fileNameInput = input("Please enter the name of the csv file that will be used:  ")
		dbObject.createDB(fileNameInput)
		break
	elif userInput == 2:
		print ("You have chosen to open an exsisting database.")
		break
	elif userInput == 3:
		print ("You have chosen to close the database.")
		break
	elif userInput == 4:
		print ("You have chosen to display a record.")
		break
	elif userInput == 5:
		print ("You have chosen to update a record in the database.")
		break
	elif userInput == 6:
		print ("You have chosen to create a new record for the database.")
		#which database?
		break
	elif userInput == 7:
		print ("You have chosen to add a record to the database.")
		break
	elif userInput == 8:
		print ("You have chosen to delete a record from the database.")
		break
	else:
		userInput = int(input("Please enter number from 1 to 9:  "))

