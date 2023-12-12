from .connection import mysql_connection
from .logger import logging
from .exceptions import CustomException
import sys

def read_all_books():
    try:
        connection=mysql_connection()
        logging.info("Fetching all books !!!!")
        cursor=connection.cursor()
        query="SELECT* from books"
        cursor.execute(query)
        logging.info("Books fetched successfully !!!!")
        rows=cursor.fetchall()
        books=[]
        for row in rows:
            books.append(row)
        return books
    except Exception as e:
        logging.info("Connection error !!!!")
        raise CustomException(sys,e)
    finally:
        if connection.is_connected():
            logging.info("Closing the Connection !!!!")
            connection.close()
                    
          