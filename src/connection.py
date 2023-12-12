import mysql.connector
import os,sys
from dotenv import load_dotenv

from .logger import logging
from .exceptions import CustomException
load_dotenv()

host = os.environ.get("MYSQL_HOST")
user = os.environ.get("MYSQL_USERNAME")
password = os.environ.get("MYSQL_PASSWORD")
database = os.environ.get("MYSQL_DATABASE")

def mysql_connection():

    try:
        logging.info("Connecting to MySQL database !!!!")
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info("MySQL database connected successfully !!!!")
        return connection

        if connection.is_connected():
            logging.info("Connected to MySQL database !!!!")
        else:
            logging.info("Connection error !!!!")

    except mysql.connector.Error as e:
        logging.info(f"Error: {e}")
        raise CustomException(sys,e)

        
    