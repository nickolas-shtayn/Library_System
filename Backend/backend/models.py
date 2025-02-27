import mysql.connector


def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="library_db"
    )
    return conn

# Book Model
class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def save(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, isbn, available_copies) VALUES (%s, %s, %s, %s)",
                       (self.title, self.author, self.isbn, self.available_copies))
        conn.commit()
        conn.close()

    @staticmethod
    def all_books():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def find_book(book_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id=%s", (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book

# Borrower Model
class Borrower:
    def __init__(self, name, borrower_id=None):
        self.name = name
        self.borrower_id = borrower_id

    def save(self):
        """Save the borrower to the database"""
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO borrowers (name) VALUES (%s)", (self.name,))
        conn.commit()
        conn.close()

    @staticmethod
    def find_borrower(borrower_id):
        """Find a borrower by ID and return a Borrower object"""
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM borrowers WHERE id=%s", (borrower_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return Borrower(result[1], result[0])
        else:
            return None
