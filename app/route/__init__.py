from flask import Flask


def init_routes(app: Flask) -> None:
    from app.route.web import web_routes

    app.register_blueprint(web_routes, url_prefix="/")
