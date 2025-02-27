from models import Book, Borrower, connect_db


def print_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. View Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    return input("Enter your choice: ")


def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    available_copies = int(input("Enter the number of available copies: "))
    book = Book(title, author, isbn, available_copies)
    book.save()
    print(f"Book '{title}' added successfully!")


def remove_book():
    book_id = int(input("Enter the book ID to remove: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()
    conn.close()
    print(f"Book with ID {book_id} removed successfully!")


def view_books():
    books = Book.all_books()
    print("\nBooks in the Library:")
    for book in books:
        print(
            f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Available Copies: {book[4]}")


def borrow_book():
    borrower_id = int(input("Enter your borrower ID: "))

    # Check borrower's existence
    borrower = Borrower.find_borrower(borrower_id)

    if not borrower:
        name = input("Borrower not found. Enter your name: ")
        borrower = Borrower(name)
        borrower.save()  # Save the new borrower to the database

        borrower_id = borrower.borrower_id
        print(f"New borrower added: {borrower.name}")

    book_id = int(input("Enter the book ID to borrow: "))
    book = Book.find_book(book_id)

    if book:
        if book[4] > 0:
            # Insert the transaction record
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO transactions (book_id, borrower_id) VALUES (%s, %s)", (book_id, borrower_id))

            cursor.execute(
                "UPDATE books SET available_copies = available_copies - 1 WHERE id=%s", (book_id,))

            conn.commit()
            conn.close()

            print(f"Book '{book[1]}' borrowed by {borrower.name}.")
        else:
            print("Sorry, this book is not available.")
    else:
        print("Invalid book ID.")


def return_book():
    borrower_id = int(input("Enter borrower ID: "))
    book_id = int(input("Enter the book ID to return: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE transactions SET return_date = CURRENT_TIMESTAMP WHERE borrower_id = %s AND book_id = %s AND return_date IS NULL",
                   (borrower_id, book_id))
    cursor.execute(
        "UPDATE books SET available_copies = available_copies + 1 WHERE id=%s", (book_id,))
    conn.commit()
    conn.close()
    print("Book returned successfully!")
