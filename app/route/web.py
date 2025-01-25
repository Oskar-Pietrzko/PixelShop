from flask import Blueprint

from app.controller.web.auth_controller import AuthController

web_routes: Blueprint = Blueprint("web_routes", __name__)

web_routes.add_url_rule("/register", view_func=AuthController.register_view, methods=["GET"], endpoint="register_view")
web_routes.add_url_rule("/register", view_func=AuthController.register, methods=["POST"], endpoint="register")
