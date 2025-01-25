from app.model.product import Product


class Order:
    def __init__(self, products: list[Product]) -> None:
        self.products: list[Product] = products
        self.total_price: float = sum(product.price for product in self.products)

    def __repr__(self) -> str:
        return f"Order(total_price: {self.total_price}, products: {self.products})"
