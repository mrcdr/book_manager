from flask_restful import Resource, reqparse
from models.book import BookModel


class Book(Resource):
    def is_non_empty_string(s):
        s = str(s)
        if not s.strip():
            raise ValueError("Must not be empty string")
        return s

    parser_post = reqparse.RequestParser()
    parser_post.add_argument("name",
                             type=is_non_empty_string,
                             required=True,
                             help="Book title")
    parser_post.add_argument("author",
                             type=is_non_empty_string,
                             required=True,
                             help="Author name(s)")

    def get(self, _id):
        book = BookModel.find_by_id(_id)
        if Book is not None:
            return book.json()

        return {"message": "Book not found"}, 404

    def put(self, _id):
        book = BookModel.find_by_id(_id)
        data = Book._parser_post.parse_args()

        if book is None:
            book = BookModel(**data)
        else:
            book.name = data["name"]
            book.author = data["author"]

        book.save_to_db()

        return book.json()

    def delete(self, _id):
        book = BookModel.find_by_id(_id)
        if book is None:
            return {"message": "Book not found"}, 404

        book.delete_from_db()

        return {"message": "Book deleted"}

    def patch(self, _id):
        parser = reqparse.RequestParser()
        parser.add_argument("to_borrow",
                            type=bool,
                            required=True,
                            help="Whether to borrow the book")
        parser.add_argument("borrower",
                            type=str,
                            help="Borrower's name")

        data = parser.parse_args()

        book = BookModel.find_by_id(_id)

        if book is None:
            return {"message": "Book not found"}, 404

        if data["to_borrow"]:
            book.borrow(data["borrower"])
        else:
            book.take_back()

        book.save_to_db()

        return book.json()


class BookList(Resource):
    def get(self):
        return {"books": list(map(lambda x: x.json(), BookModel.query.all()))}

    def post(self):
        data = Book.parser_post.parse_args()
        book = BookModel(**data)
        book.save_to_db()

        return book.json()
