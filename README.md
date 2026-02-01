# Library Management System (Python + MySQL) 📚

A console-based Library Management System developed using Python and MySQL.

## Features
- Add new books
- Display available books
- Issue books to users
- Return issued books
- Persistent MySQL database storage

## Technologies Used
- Python
- MySQL
- mysql-connector-python
- Object-Oriented Programming

## Database Setup
```sql
CREATE DATABASE library_db;
USE library_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE issued_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(100),
    issued_to VARCHAR(100),
    issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
