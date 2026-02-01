class Library:
    def __init__(self):
        self.books_file = "data/books.txt"
        self.issued_file = "data/issued_books.txt"

    def display_books(self):
        print("\nAvailable Books:")
        try:
            with open(self.books_file, "r") as f:
                books = f.readlines()
                if not books:
                    print("No books available")
                for book in books:
                    print("-", book.strip())
        except FileNotFoundError:
            print("Books file not found")

    def add_book(self, book):
        with open(self.books_file, "a") as f:
            f.write(book + "\n")
        print("Book added successfully")

    def issue_book(self, book, user):
        with open(self.books_file, "r") as f:
            books = f.readlines()

        if book + "\n" not in books:
            print("Book not available")
            return

        books.remove(book + "\n")
        with open(self.books_file, "w") as f:
            f.writelines(books)

        with open(self.issued_file, "a") as f:
            f.write(book + " issued to " + user + "\n")

        print("Book issued successfully")

    def return_book(self, book):
        with open(self.books_file, "a") as f:
            f.write(book + "\n")
        print("Book returned successfully")
