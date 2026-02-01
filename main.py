from library import Library

library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        book = input("Enter book name: ")
        library.add_book(book)
    elif choice == "3":
        book = input("Enter book name to issue: ")
        user = input("Enter user name: ")
        library.issue_book(book, user)
    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)
    elif choice == "5":
        print("Thank you for using Library Management System")
        break
    else:
        print("Invalid choice!")
