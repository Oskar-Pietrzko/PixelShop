from flask import Response, request, make_response, jsonify

from app.decorator.validation import validate_json, validate_fields, validate_type
from app.db.product_db import ProductDB
from app import db


class ProductController:
    @staticmethod
    @validate_json
    @validate_fields(["name", "price"])
    @validate_type("name", str)
    @validate_type("price", (int, float))
    def create() -> Response:
        data: dict[str, str | int | float] = request.json
        product: ProductDB = ProductDB(
            name=data["name"],
            price=data["price"]
        )

        db.session.add(product)
        db.session.commit()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": product.to_json()
                }
            ), 201
        )

    @staticmethod
    def get_all() -> Response:
        products: list[ProductDB] = ProductDB.query.all()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": [product.to_json() for product in products]
                }
            ), 200
        )

    @staticmethod
    def get(product_id: int) -> Response:
        product: ProductDB | None = ProductDB.query.get(product_id)

        if not product:
            return make_response(jsonify({"success": False, "error": "Product does not exist"}), 404)

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": product.to_json()
                }
            ), 200
        )

    @staticmethod
    @validate_json
    @validate_type("name", str)
    @validate_type("price", (int, float))
    def update(product_id: int) -> Response:
        product: ProductDB | None = ProductDB.query.get(product_id)

        if not product:
            return make_response(jsonify({"success": False, "error": "Product does not exist"}), 404)

        data: dict[str, str | int | float] = request.json

        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)

        db.session.commit()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": product.to_json()
                }
            ), 200
        )

    @staticmethod
    def delete(product_id: int) -> Response:
        product: ProductDB | None = ProductDB.query.get(product_id)

        if not product:
            return make_response(jsonify({"success": False, "error": "Product does not exist"}), 404)

        db.session.delete(product)
        db.session.commit()

        return make_response(
            jsonify(
                {
                    "success": True,
                    "data": {}
                }
            ), 200
        )
