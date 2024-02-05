import csv
import os

class DB:
    def __init__(self):
        self.recordSize = 0
        self.numRecords = 0
        self.dataFileptr = None
    
    def open(self, fileName):
        csv_file = f"{fileName}.csv"
        data_file = f"{fileName}.data"
        try:
            with open(csv_file, "r") as csv_file:
                self.numRecords, self.recordSize = map(int, csv_file.readline().split())
            self.dataFileptr = open(data_file, "r+")
            return True
        except:
            print(f"Database {fileName} not found.")
            return False
    
    def close(self):
        if self.dataFileptr:
            self.dataFileptr.close()
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