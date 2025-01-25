from flask import Response, request, make_response, jsonify

from app.db.client_db import ClientDB
from app.db.product_db import ProductDB
from app.decorator.validation import validate_json, validate_fields, validate_type
from app.db.order_db import OrderDB
from app import db


class OrderController:
    @staticmethod
    @validate_json
    @validate_fields(["product_id"])
    @validate_type("product_id", int)
    def create(client_id: int) -> Response:
        if not ClientDB.query.get(client_id):
            return make_response(jsonify({"success": False, "error": "Client does not exist"}), 404)

        data: dict[str, int] = request.json
        product: ProductDB | None = ProductDB.query.get(data["product_id"])

        if not product:
            return make_response(jsonify({"success": False, "error": "Product does not exist"}), 400)

        order: OrderDB = OrderDB(
            client_id=client_id,
            product_id=product.product_id,
            purchase_price=product.price,
        )

        db.session.add(order)
        db.session.commit()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": order.to_json()
                }
            ), 201
        )

    @staticmethod
    def get_all() -> Response:
        clients: list[ClientDB] = ClientDB.query.all()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": [client.to_json() for client in clients]
                }
            ), 200
        )

    @staticmethod
    def get(client_id: int) -> Response:
        client: ClientDB | None = ClientDB.query.get(client_id)

        if not client:
            return make_response(jsonify({"success": False, "error": "Client does not exist"}), 404)

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": client.to_json()
                }
            ), 200
        )

    @staticmethod
    @validate_json
    @validate_type("first_name", str)
    @validate_type("last_name", str)
    def update(client_id: int) -> Response:
        client: ClientDB | None = ClientDB.query.get(client_id)

        if not client:
            return make_response(jsonify({"success": False, "error": "Client does not exist"}), 404)

        data: dict[str, str] = request.json

        client.name = data.get("name", client.name)
        client.price = data.get("price", client.price)

        db.session.commit()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": client.to_json()
                }
            ), 200
        )

    @staticmethod
    def delete(client_id: int) -> Response:
        client: ClientDB | None = ClientDB.query.get(client_id)

        if not client:
            return make_response(jsonify({"success": False, "error": "Client does not exist"}), 404)

        db.session.delete(client)
        db.session.commit()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": {}
                }
            ), 200
        )
