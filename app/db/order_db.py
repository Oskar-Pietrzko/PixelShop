from sqlalchemy.orm import Mapped

from app.db.order_line_db import OrderLineDB
from app.db import db


class OrderDB(db.Model):
    __tablename__: str = "orders"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    client_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)

    order_lines: Mapped[list[OrderLineDB]] = db.relationship("OrderLineDB", backref="orders")

    def __repr__(self) -> str:
        return f"OrderDB(id={self.id}, client_id={self.client_id}, product_id={self.product_id}, purchase_price={self.purchase_price})"

    def to_json(self) -> dict[str, any]:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "product_id": self.product_id,
            "purchase_price": self.purchase_price
        }
