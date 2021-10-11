class DatabaseEntry:
    def __init__(self, id : int, tool : str, borrowDate : str, borrower : str, returnDate : str = '') -> None:
        self.__id = id
        self.__tool = tool
        self.__borrowDate = borrowDate
        self.__borrower = borrower
        self.__returnDate = returnDate

    def getID(self) -> int:
        return self.__id

    def getTool(self) -> str:
        return self.__tool

    def getBorrowDate(self) -> str:
        return self.__borrowDate

    def getBorrower(self) -> str:
        return self.__borrower

    def getReturnDate(self) -> str:
        return self.__returnDate