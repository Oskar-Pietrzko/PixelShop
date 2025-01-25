from flask import request, make_response, jsonify, Response


def validate_json(func: callable) -> callable:
    def wrapper(*args: tuple, **kwargs: dict[str, any]) -> callable:
        if not request.json:
            return make_response({"success": False, "error": "Request must be JSON"}, 400)

        return func(*args, **kwargs)

    return wrapper

def validate_fields(required_fields: list[str]) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args: tuple, **kwargs: dict[str, any]) -> callable:
            data: dict[str, any] = request.json

            for field in required_fields:
                if not data.get(field):
                    return make_response(jsonify({"success": False, "error": f"Field {field} is required"}), 400)

            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_type(field: str, field_types: tuple | type) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args: tuple, **kwargs: dict[str, any]) -> callable:
            data: dict[str, any] = request.json

            if field in data and not isinstance(data[field], field_types):
                if isinstance(field_types, tuple):
                    field_type_names = " or ".join([field_type.__name__ for field_type in field_types])
                else:
                    field_type_names = field_types.__name__

                return make_response(jsonify({"success": False, "error": f"Field {field} should be of type {field_type_names}"}), 400)

            return func(*args, **kwargs)
        return wrapper
    return decorator
