from flask import Response, make_response, request, render_template

from app.model.client import Client

import requests

class AuthController:
    @staticmethod
    def register() -> Response:
        response = requests.post(request.url_root.strip("/") + "/api/client", json=request.form.to_dict()).json()

        if response["success"]:
            client: Client =  Client(response["data"]["first_name"], response["data"]["last_name"])
            print(client)

            return make_response(render_template("register.html", error=f"Client: {client.first_name}, {client.last_name}"), 200)
        else:
            return make_response(render_template("register.html", error=response["error"]), 400)

    @staticmethod
    def register_view() -> Response:
        return make_response(render_template("register.html"), 200)
