from flask import Flask

from app.db import db

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object("config.Config")
    app.json.sort_keys = False

    db.init_app(app)

    with app.app_context():
        from app.route import init_routes

        init_routes(app)
        db.create_all()

    return app
