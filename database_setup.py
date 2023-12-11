import sqlite3
from sqlite3 import Error

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

connection = create_connection("C:\\Users\\danwh\\OneDrive\\Documents\\python\\Viable-Library\\library_database.db")
print("got here")
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
email TEXT NOT NULL, 
password TEXT NOT NULL
);"""

create_copy_table = """
CREATE TABLE IF NOT EXISTS copy (
id INTEGER PRIMARY KEY AUTOINCREMENT,
available BOOLEAN,
borrower_id INTEGER NOT NULL,
book_id INTEGER NOT NULL,
FOREIGN KEY (borrower_id) REFERENCES users(id),
FOREIGN KEY (book_id) REFERENCES books(id)
);"""

execute_query(connection, create_users_table)
execute_query(connection, create_books_table)
execute_query(connection, create_copy_table)

#put data in the tables here

