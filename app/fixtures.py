INITIAL_BOOKS = [
    {
        'title': 'Witcher'
    },
    {
        'title': 'Doppler'
    },
    {
        'title': 'Time out of Joint'
    }
]


def create_initial_books(db):
    from app.books.models import Book

    for book_data in INITIAL_BOOKS:
        if not bool(Book.query.filter_by(title=book_data.get('title')).first()):
            book = Book(**book_data)
            db.session.add(book)
            db.session.commit()
