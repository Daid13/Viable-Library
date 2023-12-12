import sqlite3
from sqlite3 import Error



create_books_table = """
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT NOT NULL
);"""

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL, 
last_name TEXT NOT NULL, 
email TEXT NOT NULL
);"""

create_copy_table = """
CREATE TABLE IF NOT EXISTS copy (
id INTEGER PRIMARY KEY AUTOINCREMENT,
available BOOLEAN,
borrower_id INTEGER,
due_date TEXT,
book_id INTEGER NOT NULL,
FOREIGN KEY (borrower_id) REFERENCES users(id),
FOREIGN KEY (book_id) REFERENCES books(id)
);"""


create_users = """
INSERT INTO users (first_name, last_name, email)
VALUES
('John', 'Smith', 'John@Smith.com'),
('Joe', 'Bloggs', 'Josephblogger@gmail.com');
"""
create_books = """
INSERT INTO books (title, description)
VALUES
('Return of the King', 'The epic finale in the genre defining work by J.R.R Tolkien'),
('Foundation', 'The Galactic Empire is doomed but the Encyclopedists of Terminus may shorten the turmoil');
"""
create_copy = """
INSERT INTO copy (available, borrower_id, due_date, book_id)
VALUES
(1, NULL, NULL, 1),
(1, NULL, NULL, 1),
(1, NULL, NULL, 2);
"""

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



def setup(path):
    connection = create_connection(path)
    execute_query(connection, create_users_table)
    execute_query(connection, create_books_table)
    execute_query(connection, create_copy_table)

    #put data in the tables here
    execute_query(connection, create_users)
    execute_query(connection, create_books)
    execute_query(connection, create_copy)
    return connection
