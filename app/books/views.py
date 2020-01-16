from http import HTTPStatus

from flask import Blueprint, jsonify
from flask import request
from marshmallow import ValidationError
from sqlalchemy import func

from app.books.models import RequestEmail, Book
from app.books.schemas import RequestEmailRetrieveSchema, RequestEmailCreateSchema
from app.database import db


books_api = Blueprint('books_api', __name__)


@books_api.route('request/<int:request_id>/', methods=["GET"])
def retrieve_request(request_id):
    request_email = RequestEmail.query.filter_by(id=request_id).first_or_404()
    response_data = RequestEmailRetrieveSchema().dump(request_email)
    return jsonify(response_data), HTTPStatus.OK


@books_api.route('request/', methods=["POST"])
def create_request():
    data = request.get_json()
    schema = RequestEmailCreateSchema()

    book_title = data.get('title', '')
    email = data.get('email')
    book = Book.query.filter(func.lower(Book.title) == book_title.lower()).first()
    if not bool(book):
        return {'errors': {
                        'title': [f'"{book_title}" could not foound']
                    }
               }, HTTPStatus.BAD_REQUEST

    if bool(RequestEmail.query.filter_by(book_id=book.id, email=email).first()):
        return {'errors': {
            'email': [f'"{book_title}" already requested for "{email}"']
        }}, HTTPStatus.BAD_REQUEST

    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        errors = err.messages
        return jsonify({'errors': errors}), HTTPStatus.BAD_REQUEST

    return jsonify(validated_data), HTTPStatus.CREATED


@books_api.route('request/<int:request_id>/', methods=["DELETE"])
def delete_request(request_id):
    request_email = RequestEmail.query.filter_by(id=request_id).first_or_404()
    db.session.delete(request_email)
    db.session.commit()
    return '', HTTPStatus.NO_CONTENT
