USE library_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    available_copies INT NOT NULL
);

CREATE TABLE borrowers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    borrower_id INT,
    borrow_date DATETIME DEFAULT NOW(),
    return_date DATETIME,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
);