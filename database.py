import csv
import os

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

    def createDatabase(self, filename):
        csv_filename = filename + ".csv"
        data_filename = filename + ".data"
        config_filename= filename + ".config"

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

            filestream.write("{:{width}.{width}}".format('__empty__',width=self.Id_size))
            filestream.write("{:{width}.{width}}".format('',width=self.fname_size))
            filestream.write("{:{width}.{width}}".format('',width=self.lname_size))
            filestream.write("{:{width}.{width}}".format('',width=self.age_size))
            filestream.write("{:{width}.{width}}".format('',width=self.ticketNum_size))
            filestream.write("{:{width}.{width}}".format('',width=self.fare_size))
            filestream.write("{:{width}.{width}}".format('',width=self.date_size))
            filestream.write("\n")

        with open(data_filename, "w") as outfile:
            for dict in data_list:
                writeDB(outfile, dict)

        recordSize = self.Id_size + self.fname_size + self.lname_size + self.age_size + self.ticketNum_size + self.fare_size + self.date_size + 1
    
        with open(config_filename, "w") as config_file:
            config_file.write(f"Number of records: {len(data_list)*2}\n")
            config_file.write(f"Record size: {recordSize}\n")

    def open(self, fileName):
        config_filename = f"{fileName}.config"
        data_filename = f"{fileName}.data"

        #open Config File
        try:
            with open(config_filename, "r") as config_file:
                for line in config_file:
                    if "Number of records:" in line:
                        self.numRecords = int(line.split(":")[1].strip())
                    elif "Record size:" in line:
                        self.recordSize = int(line.split(":")[1].strip())

        except FileNotFoundError:
            print(f"Config file {config_filename} not found.")
            return False
        
        except ValueError:
            print("Error reading the config file.")
            return False

        # Open the Data file
        try:
            if self.isOpen():
                print("Please close pervious Database beore opening a new one.")

                return False
                
            else:
                self.dataFileptr = open(data_filename, "r+")
                print(f"Database {fileName} is open")


        except FileNotFoundError:
            print(f"Data file {data_filename} not found.")
            return False

        return True
    
    def close(self):
        if self.dataFileptr:
            self.dataFileptr.close()
            print("Database Closed")
        self.recordSize = 0
        self.numRecords = 0
        self.dataFileptr = None
    
    def isOpen(self):
        return self.dataFileptr is not None
    
    def readRecord(self, recordNum):
        if not self.isOpen() or not (0 <= recordNum < self.numRecords):
            return -1
        self.dataFileptr.seek(recordNum * self.recordSize)
        record = self.dataFileptr.read(self.recordSize)
        if record.startswith("_empty_"):
            return 0
        
        #stuff to parse records

        return 1
    
    def writeRecord(self, recordNum, passengerID, fname, lname, age, ticketNum, fare, date):
        if not self.isOpen() or not (0 <= recordNum < self.numRecords):
            return -1
        self.dataFileptr.seek(recordNum * self.recordSize)
        
        #add write record stuff

        return 1 #add something to return 0 when overwritting an empty
    
    def binarySearch(self, passengerID):
        #implement binary search

        return False, -1 #if not found
    
    def updateRecord(self, passengerID, fname, lname, age, ticketNum, fare, date):
        found, recordNum = self.binarySearch(passengerID)

        if found:
            self.writeRecord(recordNum, passengerID, fname, lname, age, ticketNum, fare, date)
            return True
        return False
    
    def deleteRecord(self, passengerID):
        found, recordNum = self.binarySearch(passengerID)
        
        if found:
            self.writeRecord(recordNum, "_empty_", "", "", "", "", "","")
            return True
        return False
    
    def addRecord(self, passengerID, fname, lname, age, ticketNum, fare, date):
        if not self.isOpen():
            return False
        #add logic
        return True