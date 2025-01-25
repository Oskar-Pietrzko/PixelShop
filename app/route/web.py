from flask import Blueprint

from app.controller.client_controller import ClientController

web_routes: Blueprint = Blueprint("web_routes", __name__)

web_routes.add_url_rule("/client/add", view_func=ClientController.add, methods=["GET", "POST"], endpoint="add_client")
web_routes.add_url_rule("/client", view_func=ClientController.get_all, methods=["GET"], endpoint="get_all_clients")
