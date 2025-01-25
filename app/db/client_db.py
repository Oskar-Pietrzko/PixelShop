from sqlalchemy.orm import Mapped

from app.db.order_db import OrderDB
from app.db import db


class ClientDB(db.Model):
    __tablename__: str = "clients"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    first_name: Mapped[str] = db.Column(db.String(100), nullable=False)
    last_name: Mapped[str] = db.Column(db.String(100), nullable=False)

    orders: Mapped[list[OrderDB]] = db.relationship("OrderDB", backref="clients")

    def __repr__(self) -> str:
        return f"ClientDB(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"

    def to_json(self) -> dict[str, any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
