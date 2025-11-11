from Book import Book

def main():
    books = []
    print("Welcome to the book collection manager!")
    print("This program lets you manage your book collection.")

    while True:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the year of publication: ")
        book = Book(title, author, year)
        books.append(book)

        while True:
            print("\nWhat would you like to do with this book?")
            print("1. Check out the book")
            print("2. Return the book")
            print("3. View book information")
            print("4. Add another book")
            choice = input("Choice: ")

            if choice == '1':
                print(book.check_out())
            elif choice == '2':
                print(book.return_book())
            elif choice == '3':
                print("\nBook Information:")
                print(book.get_info())
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

        repeat = input("\nWould you like to add another book? (y/n): ").lower()
        if repeat != 'y':
            break

    print("\nYour Book Collection:")
    for book in books:
        print("\n" + book.get_info())

if __name__ == "__main__":
    main()