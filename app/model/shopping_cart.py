from app.model.order import Order
from app.model.product import Product


class ShoppingCart:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def __repr__(self) -> str:
        return f"ShoppingCart(products={self.products})"

    def add(self, product: Product) -> None:
        if product in self.products:
            raise ValueError(f"Product '{product.name}' is already in the cart.")

        self.products.append(product)

    def remove(self, product: Product) -> None:
        if product not in self.products:
            raise ValueError(f"Product '{product.name}' is not in the cart.")

        self.products.remove(product)

    def clear(self) -> None:
        self.products.clear()

    def finalize(self) -> Order:
        if not self.products:
            raise ValueError("Cannot finalize an empty shopping cart.")

        order = Order(self.products)
        self.clear()

        return order
