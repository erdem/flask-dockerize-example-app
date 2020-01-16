from flask_sqlalchemy import SQLAlchemy

from app.fixtures import create_initial_books

db = SQLAlchemy()


def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
        create_initial_books(db)
