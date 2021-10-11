import os

from database import Database
from databaseEntry import DatabaseEntry


databaseName = 'database.db'
db = Database(databaseName)

def checkDatabaseExistenz() -> bool:
    print(f'Checking the existenz of {databaseName}...')
    if os.path.exists(databaseName):
        print(f'{databaseName} exists...')
        return True
    else:
        print(f'{databaseName} does not exists...')
        print('Do you want to create it? [y/n]')
        if input() == ('y' or 'yes'):
            db.createDatabase(databaseName)
        else:
            return False
        return True


if __name__ == '__main__':
    print('EasyBorrowedToolManager')
    print('https://github.com/BBMBB/EasyBorrowedToolManager\n\n')

    if not checkDatabaseExistenz():
        exit()

    while True:
        print("[1]\tList of not returned borrowed items")
        print("[2]\tAdd new borrowed item")
        print("[3]\tUpdate a borrowed item")
        print("[4]\tList all borrowed items")
        print("[5]\tExit")
        choice = input()
        if choice == '1':
            tmpList = db.getListOfBorrowesItems()
            print("ID\t\tTool\t\tBorrowDate\t\tBorrower")
            for i in range(1, len(tmpList)):
                print(f'{tmpList[i].getID()}\t\t{tmpList[i].getTool()}\t\t{tmpList[i].getBorrowDate()}\t\t{tmpList[i].getBorrower()}\t\t')
        elif choice == '2':
            print("Tool:")
            tool = input()
            print("Borrow Date:")
            borrowDate = input()
            print("Borrower:")
            borrower = input()
            db.addBorrowedItem(tool, borrowDate, borrower)
        elif choice == '3':
            tmpList = db.getListOfBorrowesItems()
            print("ID\t\tTool\t\tBorrowDate\t\tBorrower")
            ids = [int]
            for i in range(1, len(tmpList)):
                ids.append(tmpList[i].getID())
                print(f'{tmpList[i].getID()}\t\t{tmpList[i].getTool()}\t\t{tmpList[i].getBorrowDate()}\t\t{tmpList[i].getBorrower()}\t\t')
            print("Which ID?:")
            id = int(input())
            if not id in ids:
                print("Can't find ID in database")
            else:
                print("Return Date:")
                returnDate = input()
                db.updateReturnDate(id, returnDate)
        elif choice == '4':
            tmpList = db.getListOfAllItems()
            print("ID\t\tTool\t\tBorrowDate\t\tBorrower\t\tReturnDate")
            for i in range(1, len(tmpList)):
                print(f'{tmpList[i].getID()}\t\t{tmpList[i].getTool()}\t\t{tmpList[i].getBorrowDate()}\t\t{tmpList[i].getBorrower()}\t\t\t{tmpList[i].getReturnDate()}')
        elif choice == '5':
            db.disconnect()
            exit()
        else:
            print("Invalid Input")