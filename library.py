from db_config import get_connection

class Library:

    def display_books(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM books")
        books = cursor.fetchall()

        if not books:
            print("No books available")
        else:
            print("\nAvailable Books:")
            for book in books:
                print("-", book[0])

        conn.close()

    def add_book(self, book):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (name) VALUES (%s)", (book,))
        conn.commit()
        conn.close()
        print("Book added successfully")

    def issue_book(self, book, user):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books WHERE name=%s", (book,))
        result = cursor.fetchone()

        if not result:
            print("Book not available")
            conn.close()
            return

        cursor.execute("DELETE FROM books WHERE name=%s", (book,))
        cursor.execute(
            "INSERT INTO issued_books (book_name, issued_to) VALUES (%s, %s)",
            (book, user)
        )

        conn.commit()
        conn.close()
        print("Book issued successfully")

    def return_book(self, book):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO books (name) VALUES (%s)", (book,))
        cursor.execute("DELETE FROM issued_books WHERE book_name=%s", (book,))

        conn.commit()
        conn.close()
        print("Book returned successfully")
