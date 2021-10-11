import sqlite3
from typing import List

from databaseEntry import DatabaseEntry


class Database:
    def __init__(self, filename : str) -> None:
        self.__isConnected = False
        self.__db = None
        self.__cur = None
        self.__filename = filename

    def createDatabase(self, filename : str) -> None:
        open(filename, 'a').close()
        self.__filename = filename
        self.connectToDatabase()
        if self.__isConnected:
            cmd = 'CREATE TABLE data (id INTEGER PRIMARY KEY, tool TEXT NOT NULL, borrowDate TEXT NOT NULL, borrower TEXT NOT NULL, returnDate TEXT)'
            self.__cur.execute(cmd)
            self.__db.commit()

    def connectToDatabase(self) -> None:
        if self.__db == None and self.__isConnected == False:
            self.__db = sqlite3.connect(self.__filename)
            self.__cur = self.__db.cursor()
            self.__isConnected = True

    def addBorrowedItem(self, tool : str, borrowDate : str, borrower : str):
        cmd = f'INSERT INTO data (tool, borrowDate, borrower) VALUES (\"{tool}\",\"{borrowDate}\",\"{borrower}\");'
        if self.__isConnected:
            self.__cur.execute(cmd)
            self.__db.commit()
        else:
            self.connectToDatabase()
            self.__cur.execute(cmd)
            self.__db.commit()

    def updateReturnDate(self, id : int, returnDate : str):
        cmd = f'UPDATE data SET returnDate = \"{returnDate}\" WHERE id = {id}'
        if self.__isConnected:
            self.__cur.execute(cmd)
            self.__db.commit()

    def getListOfBorrowesItems(self) -> List[DatabaseEntry]:
        cmd = 'SELECT id, tool, borrowDate, borrower FROM data WHERE returnDate IS NULL;'
        if self.__isConnected:
            self.__cur.row_factory = sqlite3.Row
            self.__cur.execute(cmd)
            l = self.__cur.fetchall()
        else:
            self.connectToDatabase()
            self.__cur.row_factory = sqlite3.Row
            self.__cur.execute(cmd)
            l = self.__cur.fetchall()
        tmpListOfBorrowedItems = [DatabaseEntry]
        for row in l:
            tmpItem = DatabaseEntry(row['id'], row['tool'], row['borrowDate'], row['borrower'])
            tmpListOfBorrowedItems.append(tmpItem)
        return tmpListOfBorrowedItems

    def getListOfAllItems(self) -> List[DatabaseEntry]:
        cmd = 'SELECT id, tool, borrowDate, borrower, returnDate FROM data;'
        if self.__isConnected:
            self.__cur.row_factory = sqlite3.Row
            self.__cur.execute(cmd)
            l = self.__cur.fetchall()
        else:
            self.connectToDatabase()
            self.__cur.row_factory = sqlite3.Row
            self.__cur.execute(cmd)
            l = self.__cur.fetchall()
        tmpListOfItems = [DatabaseEntry]
        for row in l:
            tmpItem = DatabaseEntry(row['id'], row['tool'], row['borrowDate'], row['borrower'], row['returnDate'])
            tmpListOfItems.append(tmpItem)
        return tmpListOfItems        

    def disconnect(self):
        if self.__isConnected:
            self.__db.commit()
            self.__db.close()
