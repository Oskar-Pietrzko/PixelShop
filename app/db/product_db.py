from sqlalchemy.orm import Mapped

from app.db import db


class ProductDB(db.Model):
    __tablename__: str = "products"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(255), nullable=False)
    price: Mapped[float] = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"ProductDB(id={self.id}, name={self.name}, price={self.price:.2f})"

    def to_json(self) -> dict[str, any]:
        return {
            "id": self.id,
            "name": self.name,
            "price": f"{self.price:.2f}"
        }
