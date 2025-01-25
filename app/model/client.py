class Client:
    def __init__(self, client_id: int, first_name: str, last_name: str) -> None:
        self.id: int = client_id
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __repr__(self) -> str:
        return f"Client(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"
