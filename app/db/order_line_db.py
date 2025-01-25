from sqlalchemy.orm import Mapped

from app.db.product_snapshot_db import ProductSnapshotDB
from app.db import db


class OrderLineDB(db.Model):
    __tablename__: str = "order_lines"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    order_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("product_snapshots.id"), nullable=False)

    product: Mapped[ProductSnapshotDB] = db.relationship("ProductSnapshotDB", backref="clients")

    def __repr__(self) -> str:
        return f"OrderDB(id={self.id}, client_id={self.client_id}, product_id={self.product_id}, purchase_price={self.purchase_price})"

    def to_json(self) -> dict[str, any]:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "product_id": self.product_id,
            "purchase_price": self.purchase_price
        }
