from flask import Blueprint

from app.controller.api.client_controller import ClientController
from app.controller.api.product_controller import ProductController

api_routes: Blueprint = Blueprint("api_routes", __name__)

api_routes.add_url_rule("/product", view_func=ProductController.create, methods=["POST"], endpoint="create_product")
api_routes.add_url_rule("/product", view_func=ProductController.get_all, methods=["GET"], endpoint="get_all_products")
api_routes.add_url_rule("/product/<int:product_id>", view_func=ProductController.get, methods=["GET"], endpoint="get_product")
api_routes.add_url_rule("/product/<int:product_id>", view_func=ProductController.update, methods=["PUT"], endpoint="update_product")
api_routes.add_url_rule("/product/<int:product_id>", view_func=ProductController.delete, methods=["DELETE"], endpoint="delete_product")

api_routes.add_url_rule("/client", view_func=ClientController.create, methods=["POST"], endpoint="create_client")
api_routes.add_url_rule("/client", view_func=ClientController.get_all, methods=["GET"], endpoint="get_all_clients")
api_routes.add_url_rule("/client/<int:client_id>", view_func=ClientController.get, methods=["GET"], endpoint="get_client")
api_routes.add_url_rule("/client/<int:client_id>", view_func=ClientController.update, methods=["PUT"], endpoint="update_client")
api_routes.add_url_rule("/client/<int:client_id>", view_func=ClientController.delete, methods=["DELETE"], endpoint="delete_client")

client_routes: Blueprint = Blueprint("client_routes", __name__)

api_routes.register_blueprint(client_routes, url_prefix="/client/<int:client_id>")
