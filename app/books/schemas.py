from marshmallow import Schema, fields, post_load
from sqlalchemy import func

from app.books.models import Book, RequestEmail
from app.database import db


class RequestEmailRetrieveSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(dump_only=True)
    title = fields.Method("get_title")
    timestamp = fields.Str(attribute='created_at', dump_only=True)

    def get_title(self, obj):
        return obj.book.title


class RequestEmailCreateSchema(Schema):
    title = fields.Str(load_only=True)
    email = fields.Email(load_only=True)

    @post_load
    def create_request_email(self, data, **kwargs):
        book_title = data.get('title')
        email = data.get('email')
        book = Book.query.filter(func.lower(Book.title) == book_title.lower()).one()
        request_email = RequestEmail(email=email)
        book.request_emails.append(request_email)
        db.session.add(book)
        db.session.add(request_email)
        db.session.commit()
        return RequestEmailRetrieveSchema().dump(request_email)
