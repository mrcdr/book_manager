from flask import Flask
from flask_restful import Api

from resources.book import Book, BookList
from resources.user import UserList

import initialize_db

from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Book, "/api/book/<int:_id>")
api.add_resource(BookList, "/api/books")
api.add_resource(UserList, "/api/users")

if __name__ == "__main__":
    app.run(debug=True)
