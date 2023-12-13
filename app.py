from src.read import read_all_books
from src.add_new import add_new_book
from src.update import update_book

from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return "hello"

@app.route("/api/books",methods=["GET","POST"])
def fetch_books():
    if request.method == "POST":
        content = request.get_json()
        title=content.get("title")
        authors=content.get("authors")
        isbn13=content.get("isbn13")
        language_code=content.get("language_code")
        num_pages=content.get("num_pages")
        publication_date=content.get("publication_date")
        publisher=content.get("publisher")
        result=add_new_book(title,authors,isbn13,language_code,num_pages,publication_date,publisher)
        if result:
            return jsonify({"result":"success"})
        else:
            return jsonify({"result":"failure"})
    books=read_all_books()
    return jsonify({"books":books})

@app.route("/api/books/<int:id>/",methods=["GET","POST"])
def update_book_(id):
    if request.method == "POST":
        content = request.get_json()
        title=content.get("title")
        authors=content.get("authors")
        isbn13=content.get("isbn13")
        language_code=content.get("language_code")
        num_pages=content.get("num_pages")
        publication_date=content.get("publication_date")
        publisher=content.get("publisher")
        result=update_book(id,title,authors,isbn13,language_code,num_pages,publication_date,publisher)
        if result:
            return jsonify({"result":"success"})
        else:
            return jsonify({"result":"failure"})
   
    return "hello"
   
   
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)



