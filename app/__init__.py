from flask import Flask

from app.books.views import books_api
from app.database import init_db
from app.utils import get_config


def create_app(config_name=None, **kwargs):

    app = Flask(__name__, **kwargs)

    try:
        app.config.from_object(get_config(config_name))
    except ImportError:
        raise Exception('Invalid Config')

    app.register_blueprint(books_api, url_prefix='/')

    init_db(app)
    return app
