## Books Mangaement
This repository contains a simple book database application that allows users to perform three main operations: reading all book details, adding a new book to the database, and updating existing book information. \
<b>Running versions of the app can be accessed by the given links</b> \
with frontend https://library-manager.streamlit.app/ \
only backend https://library-manager.azurewebsites.net/ \
frontend Repo https://github.com/namraha19/letsbloom_frontend.git

### Getting Started
#### Prerequisites
- Ensure you have Python installed on your system.
- You'll need a database system installed and configured. This project supports MySql, but you can easily modify it to use other databases.
#### Installation
1. Clone the repository:
  ```
git clone https://github.com/namraha19/Lets_bloom_assignment.git
cd Lets_bloom_assignment

```
2. Install dependencies:
 ```
pip install -r requirements.txt

```
3. Make ``` .env ``` and specify the following entries.
 ```
MYSQL_HOST = Your_host
MYSQL_USERNAME = Your_username
MYSQL_PASSWORD = Your_password
MYSQL_DATABASE = Your_database_name

```
4. Database Schema
```
bookID int AI PK 
title text 
authors text 
isbn13 bigint 
language_code text 
num_pages int 
publication_date text 
publisher text

```
5. Run app.py
```
python app.py

```
It will run server on localhost.

### USAGE 
1. Read All Book Details
  - To read all book details from the database, make a get request to the given api endpoint:
```
http://127.0.0.1:5000/api/books

```
<b>The running version can be accessed here</b>
```
https://library-manager.azurewebsites.net/api/books

```
This command will display a list of all books in the database.

2. Add a New Book
  - To add a new book to the database, make a post request to the given api endpoint :
```
http://127.0.0.1:5000/api/books

```
<b>The running version can be accessed here</b>
```
https://library-manager.azurewebsites.net/api/books

```

With the request body 
```
{"title":"TITLE OF THE BOOK","authors":"NAME OF THE AUTHOR","isbn13":ISBN,"language_code":"LANGUAGE CODE","num_pages":NUMBER OF PAGES,"publication_date":"PUBLISHING DATE","publisher":"PUBLISHER"}

```
Follow the prompts to enter the details of the new book.

3. Update Book Information
 - To update information for an existing book in the database, make a post request to the given api endpoint:
 ```
http://127.0.0.1:5000/api/books/bookId/

 ```
<b>The running version can be accessed here</b>
```
https://library-manager.azurewebsites.net/api/books/bookID/

```

With the request body 
```
{"title":"TITLE OF THE BOOK","authors":"NAME OF THE AUTHOR","isbn13":ISBN,"language_code":"LANGUAGE CODE","num_pages":NUMBER OF PAGES,"publication_date":"PUBLISHING DATE","publisher":"PUBLISHER"}

```

Follow the prompts to specify the book to update and provide the new information.



   
