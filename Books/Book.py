class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = "available"

    def check_out(self):
        if self.__status == "available":
            self.__status = "checked out"
            return f"The book '{self.__title}' has been checked out."
        else:
            return f"The book '{self.__title}' is not available."

    def return_book(self):
        if self.__status == "checked out":
            self.__status = "available"
            return f"The book '{self.__title}' has been returned."
        else:
            return f"The book '{self.__title}' is not checked out."

    def get_info(self):
        return f"Title: {self.__title}\nAuthor: {self.__author}\nYear: {self.__year}\nStatus: {self.__status}"