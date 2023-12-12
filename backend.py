import sqlite3
from sqlite3 import Error
from datetime import date
import database_setup
BORROW_LENGTH=21
PATH="C:\\Users\\danwh\\OneDrive\\Documents\\python\\Viable-Library\\library_database.db"
user_id=0
#taken from tutorial
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def borrow_book(copy):
    #validate user is logged in
    #validate copy is available
    borrow_update="""
    UPDATE copy
    SET borrower_id= %d
    due_date = %s 
    WHERE id = %d"""%(user_id,date.today()+BORROW_LENGTH,copy)
    
def return_book(copy):
    pass

def get_book_list(filter=None):
    
    query_book_list="""
    SELECT 
        books.title,
        books.description,
        copy.available,
        copy.id
    FROM 
        copy
        INNER JOIN books on books.id = copy.book_id
    """
    if filter=="available":
        query_book_list+=" WHERE copy.available = TRUE"
    elif filter=="today":
        query_book_list+= " WHERE copy.due_date = %s"%date.today()
    elif filter=="loan":
        query_book_list="""
        SELECT 
            books.title,
            books.description,
            copy.id,
            copy.due_date,
            user.first_name,
            user.last_name,
            user.email,
        FROM 
            copy
            INNER JOIN books on books.id = copy.book_id
            INNER JOIN users on user.id = copy.borrower_id
        """
    print(execute_read_query(con, query_book_list))

def register_user(first,last,email):
    #email_exists_query="""SELECT email FROM users WHERE email = '%s'"""% email
    #add validation of email format and if there already is an account.
    insert_user="""INSERT INTO users
    VALUES
    ('%s','%s','%s')"""%(first,last,email)
    database_setup.execute_query(con,insert_user)


def login(email):
    user_id=database_setup.execute_query(con,"SELECT id FROM users WHERE email = '%s"%email)
    #add error if email not in database



con=database_setup.setup(PATH)
get_book_list()



