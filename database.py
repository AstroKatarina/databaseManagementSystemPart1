import csv
import os.path

class DB:
    def __init__(self):
        self.recordSize = 0
        self.numRecords = 0
        self.dataFileptr = None
        self.Id_size = 10
        self.fname_size = 25
        self.lname_size = 25
        self.age_size = 4
        self.ticketNum_size = 25
        self.fare_size = 8
        self.date_size = 15
        self.record = dict()
        self.data_filename = None

    def createDatabase(self, filename):
        csv_filename = filename + ".csv"
<<<<<<< HEAD
        text_filename = filename + ".data"
        config_filename = filename + ".config"
=======
        data_filename = filename + ".data"
        config_filename= filename + ".config"
>>>>>>> 47b1f4ca87e8b9fc18e8a8abc1b1feccfa758449

<<<<<<< HEAD
        #each line has size ->
        charLengthPerLine = (self.Id_size + self.firstName_size + self.lastName_size + self.age_size + self.ticketNum_size + self.fare_size + self.dateOfPurchase_size)

        # Read the CSV file and write into data files
=======
>>>>>>> 47b1f4ca87e8b9fc18e8a8abc1b1feccfa758449
        with open(csv_filename, "r") as csv_file:
            data_list = list(csv.DictReader(csv_file, fieldnames = ('passengerID', 'fname', 'lname', 'age', 'ticketNum', 'fare', 'date')))

        def writeDB(filestream, dict):
            filestream.write("{:{width}.{width}}".format(dict["passengerID"],width=self.Id_size))
            filestream.write("{:{width}.{width}}".format(dict["fname"],width=self.fname_size))
            filestream.write("{:{width}.{width}}".format(dict["lname"],width=self.lname_size))
            filestream.write("{:{width}.{width}}".format(dict["age"],width=self.age_size))
            filestream.write("{:{width}.{width}}".format(dict["ticketNum"],width=self.ticketNum_size))
            filestream.write("{:{width}.{width}}".format(dict["fare"],width=self.fare_size))
            filestream.write("{:{width}.{width}}".format(dict["date"],width=self.date_size))
            filestream.write("\n")

            filestream.write("{:{width}.{width}}".format('_empty_',width=self.Id_size))
            filestream.write("{:{width}.{width}}".format('',width=self.fname_size))
            filestream.write("{:{width}.{width}}".format('',width=self.lname_size))
            filestream.write("{:{width}.{width}}".format('',width=self.age_size))
            filestream.write("{:{width}.{width}}".format('',width=self.ticketNum_size))
            filestream.write("{:{width}.{width}}".format('',width=self.fare_size))
            filestream.write("{:{width}.{width}}".format('',width=self.date_size))
            filestream.write("\n")

        def writeConfig(filestream):
            filestream.write("There are " + self.num_record + " records.")
        with open(data_filename, "w") as outfile:
            for dict in data_list:
                writeDB(outfile, dict)

        with open(text_filename,"w") as outfile:
            for dict in data_list:
                writeDB(outfile,dict)
                self.num_record += 1
        recordSize = self.Id_size + self.fname_size + self.lname_size + self.age_size + self.ticketNum_size + self.fare_size + self.date_size + 1
    
        with open(config_filename, "w") as config_file:
            config_file.write(f"Number of records: {len(data_list)*2}\n")
            config_file.write(f"Record size: {recordSize}\n")

    def open(self, fileName):
        config_filename = f"{fileName}.config"
        self.dataFileptr = f"{fileName}.data"

        #open Config File
        try:
            with open(config_filename, "r") as config_file:
                for line in config_file:
                    if "Number of records:" in line:
                        self.numRecords = int(line.split(":")[1].strip())
                    elif "Record size:" in line:
                        self.recordSize = int(line.split(":")[1].strip())
                

<<<<<<< HEAD
        with open(config_filename, "w") as outfile:
            writeConfig(outfile)

    #read the database
    def readDB(self, filename, DBsize, rec_size):
        self.filestream = filename + ".data"
        self.record_size = DBsize
        self.rec_size = rec_size
=======
        except FileNotFoundError:
            print(f"\nConfig file {config_filename} not found.")
            self.dataFileptr = None
            return False
>>>>>>> 47b1f4ca87e8b9fc18e8a8abc1b1feccfa758449
        
        except ValueError:
            print("\nError reading the config file.")
            self.dataFileptr = None
            return False
        
        config_file.close()

        # Open the Data file
        try:
            self.data_filename = open(self.dataFileptr, "r+")
            print(f"\nDatabase {fileName} is open")


        except FileNotFoundError:
            print(f"\nData file {self.dataFileptr} not found.")
            return False

        return True
    
    def isOpen(self):
        return self.dataFileptr is not None
    
    def close(self):
        if self.data_filename:
            self.data_filename.close()
            print("\nDatabase Closed")
        self.recordSize = 0
        self.numRecords = 0
        self.dataFileptr = None
    
    
    def readRecord(self, recordNum):
        self.flag = False
        passengerID = fname = lname = age = ticketNum = fare = date = "None"
        self.index = recordNum
        if not self.isOpen() or not (0 <= recordNum < self.numRecords):
            print("\nDatabase not opened, or invalid input")
            return -1
        
        if recordNum >= 0 and recordNum < self.recordSize:
            self.data_filename.seek(0,0)
            self.data_filename.seek(recordNum * self.recordSize)
            line = self.data_filename.readline().rstrip()
            self.flag = True

            if line.startswith("_empty_"):
                self.record = dict({"passengerID": "_empty_"})
                return 0
        
        if self.flag:
            passengerID = line[0:10]
            fname = line[10:35]
            lname = line[35:60]
            age = line[60:64]
            ticketNum = line[64:89]
            fare = line[89:97]
            date = line[97:113]
            self.record = dict({"passengerID":passengerID,"fname":fname,"lname":lname,"age":age,"ticketNum":ticketNum,"fare":fare,"date":date})
            
            return 1
    
    def writeRecord(self, recordNum, passengerID, fname, lname, age, ticketNum, fare, date):
        if not self.isOpen() or not (0 <= recordNum < self.numRecords):
            return -1
        
<<<<<<< HEAD
        self.data_filename.seek(0, 0)
        self.data_filename.seek(recordNum * self.recordSize)
        line = self.data_filename.readline().rstrip()
=======
        if recordNum >= 0 and recordNum < self.recordSize:
            self.data_filename.seek(0,0)
            self.data_filename.seek(recordNum * self.recordSize)
            line = self.data_filename.readline().rstrip()
            self.data_filename.seek(0,0)
            self.data_filename.seek(recordNum * self.recordSize)
>>>>>>> e3137e9108408ed3215774830e3ccc26dae682af

        if not line.startswith("_empty_"):
            self.data_filename.write("{:{width}.{width}}".format(passengerID, width=self.Id_size))
            self.data_filename.write("{:{width}.{width}}".format(fname, width=self.fname_size))
            self.data_filename.write("{:{width}.{width}}".format(lname, width=self.lname_size))
            self.data_filename.write("{:{width}.{width}}".format(age, width=self.age_size))
            self.data_filename.write("{:{width}.{width}}".format(ticketNum, width=self.ticketNum_size))
            self.data_filename.write("{:{width}.{width}}".format(fare, width=self.fare_size))
            self.data_filename.write("{:{width}.{width}}".format(date, width=self.date_size))
            return 1

        else:
            self.data_filename.write("{:{width}.{width}}".format(passengerID, width=self.Id_size))
            self.data_filename.write("{:{width}.{width}}".format(fname, width=self.fname_size))
            self.data_filename.write("{:{width}.{width}}".format(lname, width=self.lname_size))
            self.data_filename.write("{:{width}.{width}}".format(age, width=self.age_size))
            self.data_filename.write("{:{width}.{width}}".format(ticketNum, width=self))
    
    def binarySearch(self, input_ID):
        low = 0
        high = self.numRecords - 1
        found = False
        self.recordNum = None  # Initialize the insertion point

        while not found and high >= low:
            self.middle = (low + high) // 2
            self.readRecord(self.middle)
            mid_id = self.record["passengerID"]

            if mid_id.strip() == "_empty_":
                non_empty_record = self.findNearestNonEmpty(self.middle, low, high)
                if non_empty_record == -1:
                    # If no non-empty record found, set recordNum for potential insertion
                    self.recordNum = high
                    print(f"\nCould not find record with ID {input_ID}")
                    return False, self.recordNum

                self.middle = non_empty_record
                self.readRecord(self.middle)
                mid_id = self.record["passengerID"]
                if int(mid_id) > int(input_ID):
                    index = self.middle - 1
                else:
                    index = self.middle + 1

            if mid_id != "_empty_":
                try:
                    if int(mid_id) == int(input_ID):
                        found = True
                        self.recordNum = self.middle
                    elif int(mid_id) > int(input_ID):
                        high = self.middle - 1
                    elif int(mid_id) < int(input_ID):
                        low = self.middle + 1
                except ValueError:
                    # Handle non-integer IDs
                    high = self.middle - 1

        if not found and self.recordNum is None:
            # Set recordNum to high + 1 if no suitable spot is found
            index = high + 1
            print(f"\nCould not find record with ID {input_ID}")
            return False, None

        print("\nEntry Found")
        print(f"Passenger ID: {self.record['passengerID'].strip()}, First Name: {self.record['fname'].strip()}, Last name: {self.record['lname'].strip()}, Age: {self.record['age'].strip()}, Ticket Number: {self.record['ticketNum'].strip()}, Fare: {self.record['fare'].strip()}, Date: {self.record['date'].strip()}")
        
        return found, self.recordNum

    
    def findNearestNonEmpty(self, start, low_limit, high_limit):
        step = 1  # Initialize step size

        while True:
            # Check backward
            if start - step >= low_limit:
                self.readRecord(start - step)
                if self.record["passengerID"].strip() != "_empty_":
                    #print(self.record)
                    return start - step

            # Check forward
            if start + step <= high_limit:
                self.readRecord(start + step)
                if self.record["passengerID"].strip() != "_empty_":
                    #print(self.record)
                    return start + step

            # Increase step size and repeat
            step += 1

            # Terminate if beyond the search range
            if start - step < low_limit and start + step > high_limit:
                break

        return -1  # No non-empty record found
    
    
<<<<<<< HEAD
=======
    def updateRecord(self, passengerID, fname, lname, age, ticketNum, fare, date):
        found, index = self.binarySearch(passengerID)
        
        if found:
            self.writeRecord(index, passengerID, fname, lname, age, ticketNum, fare, date)
            print("Entry Updated")
            return True
        return False
    
>>>>>>> e3137e9108408ed3215774830e3ccc26dae682af
    def deleteRecord(self, passengerID):
        found, index = self.binarySearch(passengerID)
        
        if found:
            self.writeRecord(index, "_empty_", "", "", "", "", "","")
            print("Entry Deleted")
            return True
        return False
    
    def addRecord(self, passengerID, fname, lname, age, ticketNum, fare, date):
        if not self.isOpen():
            return False
        print(self.recordNum)
        return True
    
    def createReport(self):
        if not self.isOpen():
            print("Database is not open.")
            return

        records = []
        for i in range(self.numRecords):
            if self.readRecord(i) == 1:
                records.append(self.record)

        sorted_records = sorted(records, key=lambda x: int(x['passengerID']))
        print("First ten records sorted by passengerID:")
        print("{:<12} {:<25} {:<25} {:<6} {:<25} {:<8} {:<15}".format('PassengerID', 'First Name', 'Last Name', 'Age', 'Ticket Number', 'Fare', 'Date'))
        for record in sorted_records[:10]:
            print("{:<12} {:<25} {:<25} {:<6} {:<25} {:<8} {:<15}".format(record['passengerID'], record['fname'], record['lname'], record['age'], record['ticketNum'], record['fare'], record['date']))