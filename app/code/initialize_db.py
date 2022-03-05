from models.book import BookModel
from app import app, db

with app.app_context():
    db.create_all()
    BookModel("磁性I", "久保健").save_to_db()
    BookModel("量子系のエンタングルメントと幾何学", "松枝宏明").save_to_db()
