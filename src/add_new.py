from .connection import mysql_connection
from .logger import logging
from .exceptions import CustomException
import sys

query = "INSERT INTO books (title,authors,isbn13,language_code,num_pages,publication_date,publisher) VALUES (%s,%s,%s,%s,%s,%s,%s)"

def add_new_book(title,authors,isbn13,language_code,num_pages,publication_date,publisher):
    try:
        logging.info("Adding New Book !!!!")
        values=(title,authors,isbn13,language_code,num_pages,publication_date,publisher)
        connection=mysql_connection()
        cursor=connection.cursor()
        cursor.execute(query,values)
        connection.commit()
        logging.info("New Book Added successfully !!!!")
        return 1
    except Exception as e:
        logging.info("ERROR !!!!")
        raise CustomException(sys,e)
    finally:
        if connection.is_connected():
            logging.info("Closing the Connection !!!!")
            connection.close()       
        
    
