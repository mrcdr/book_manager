from flask_restful import Resource, reqparse
from models.book import BookModel


class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("to_borrow",
                        type=bool,
                        required=True,
                        help="Whether to borrow the book")
    parser.add_argument("borrower",
                        type=str,
                        help="Borrower's name")

    def get(self, _id):
        book = BookModel.find_by_id(_id)
        if book:
            return book.json()
        return {"message": "Book not found"}, 404

    def patch(self, _id):
        data = Book.parser.parse_args()

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
