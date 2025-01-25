from app.db.client_db import ClientDB
from app.model.client import Client
from app.db import db


class ClientService:
    @staticmethod
    def create_client(data: dict) -> Client:
        if not data.get("first_name") or not data.get("last_name"):
            raise ValueError("First name and last name are required")

        client: Client = Client(data["first_name"], data["last_name"])

        client_db: ClientDB = ClientDB(first_name=client.first_name, last_name=client.last_name)
        db.session.add(client_db)
        db.session.commit()

        return client

    @staticmethod
    def get_all_clients() -> list[Client]:
        clients: list[Client] = []
        client_dbs: list[ClientDB] = ClientDB.query.all()

        for client_db in client_dbs:
            clients.append(Client(client_db.id, client_db.first_name, client_db.last_name))

        return clients
