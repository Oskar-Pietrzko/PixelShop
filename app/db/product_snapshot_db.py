from sqlalchemy.orm import Mapped

from app.db import db


class ProductSnapshotDB(db.Model):
    __tablename__: str = "product_snapshots"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(255), nullable=False)
    price: Mapped[float] = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"ProductSnapshotDB(id={self.id}, name={self.name}, price={self.price})"
