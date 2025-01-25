from flask import Response, request, make_response, render_template

from app.service.client_service import ClientService


class ClientController:
    @staticmethod
    def add() -> Response:
        if request.method == "POST":
            data = request.form.to_dict()

            try:
                ClientService.create_client(data)

                return make_response("Client added successfully!", 201)
            except ValueError as error:
                return make_response(str(error), 400)
            except Exception as error:
                return make_response(f"An error occurred: {str(error)}", 500)

        return make_response(render_template("client/add.html"), 200)

    @staticmethod
    def get_all() -> Response:
        return make_response(render_template("client/get_all.html", clients=ClientService.get_all_clients()), 200)
