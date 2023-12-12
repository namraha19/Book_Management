from .connection import mysql_connection
from .logger import logging
from .exceptions import CustomException
import sys



def update_book(bookID,title,authors,isbn13,language_code,num_pages,publication_date,publisher):
    try:
        query = "UPDATE books SET "
        logging.info("Updating Book !!!!")
        values=(title,authors,isbn13,language_code,num_pages,publication_date,publisher)
        fields=("title","authors","isbn13","language_code","num_pages","publication_date","publisher")
        not_null=[]
        for i in range(len(fields)):
            if values[i]!=None:
                query = query + fields[i] + "=" + "%s" +","
                not_null.append(values[i])
        query = query[:-1]  
        query=query+ " WHERE bookID =" + "%s"    
        not_null.append(bookID)
        connection=mysql_connection()
        cursor=connection.cursor()
        cursor.execute(query,not_null)
        connection.commit()
        logging.info("Book updated successfully !!!!")
        return 1
    except Exception as e:
        logging.info("ERROR !!!!")
        raise CustomException(sys,e)
    finally:
        if connection.is_connected():
            logging.info("Closing the Connection !!!!")
            connection.close()       
        
    