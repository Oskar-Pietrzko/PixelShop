from flask import Flask


def init_routes(app: Flask) -> None:
    from app.route.api import api_routes
    from app.route.web import web_routes

    app.register_blueprint(api_routes, url_prefix="/api")
    app.register_blueprint(web_routes, url_prefix="/")
