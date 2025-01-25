from flask import Response, request, make_response, jsonify

from app.decorator.validation import validate_json, validate_fields, validate_type
from app.db.client_db import ClientDB
from app import db


class ClientController:
    @staticmethod
    @validate_json
    @validate_fields(["first_name", "last_name"])
    @validate_type("first_name", str)
    @validate_type("last_name", str)
    def create() -> Response:
        data: dict[str, str] = request.json
        client: ClientDB = ClientDB(
            first_name=data["first_name"],
            last_name=data["last_name"]
        )

        db.session.add(client)
        db.session.commit()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": client.to_json()
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
