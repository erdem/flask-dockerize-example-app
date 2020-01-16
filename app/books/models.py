from datetime import datetime

from app.database import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=80), unique=True, index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, index=True)

    request_emails = db.relationship(
        "RequestEmail",
        back_populates="book",
        cascade="all, delete-orphan"
    )

    __mapper_args__ = {
        "order_by": created_at
    }

    __tablename__ = 'book'

    def __repr__(self):
        return (
            '<{class_name}('
            'book_id={self.id}, '
            'title="{self.title}")>'.format(
                class_name=self.__class__.__name__,
                self=self
            )
        )


class RequestEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship("Book")
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, index=True)

    __mapper_args__ = {
        "order_by": created_at
    }

    __tablename__ = 'request_email'

    def __repr__(self):
        return (
            '<{class_name}('
            'request_email_id={self.id}, '
            'book_id="{self.book_id}")'
            'email="{self.email}">'.format(
                class_name=self.__class__.__name__,
                self=self
            )
        )
