import datetime
from db import db


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    author = db.Column(db.String(200))
    is_borrowed = db.Column(db.Boolean())
    borrower = db.Column(db.String(200))
    borrow_date = db.Column(db.Date())

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.is_borrowed = False
        self.borrower = None
        borrow_date = None

    def json(self):
        return {"id": self.id,
                "name": self.name,
                "author": self.author,
                "is_borrowed": self.is_borrowed,
                "borrower": self.borrower,
                "borrow_date": self.borrow_date}

    def borrow(self, borrower):
        self.is_borrowed = True
        self.borrower = borrower
        self.borrow_date = datetime.datetime.now().date()

    def take_back(self):
        self.is_borrowed = False
        self.borrower = None

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
