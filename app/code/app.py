from flask import Flask
from flask_restful import Api

from resources.book import Book, BookList
from resources.user import UserList

from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////app_data/data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Book, "/api/books/<int:_id>")
api.add_resource(BookList, "/api/books")

if __name__ == "__main__":
    app.run(debug=True)
