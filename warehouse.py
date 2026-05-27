class NotEnoughStockError(Exception):
    """Raised when there is not enough stock to remove."""
    pass


class NegativeQuantityError(Exception):
    """Raised when quantity is negative."""
    pass


class Warehouse:
    def __init__(self):
        self._stock = {}

    def add(self, name: str, qty: int):
        """Add product to warehouse or increase existing stock."""
        if qty < 0:
            raise NegativeQuantityError("Quantity cannot be negative")
        if name in self._stock:
            self._stock[name] += qty
        else:
            self._stock[name] = qty

    def remove(self, name: str, qty: int):
        """Remove product from warehouse."""
        if qty < 0:
            raise NegativeQuantityError("Remove quantity cannot be negative")
        if name not in self._stock:
            raise NotEnoughStockError(f"Product '{name}' not in warehouse")
        if self._stock[name] < qty:
            raise NotEnoughStockError(
                f"Not enough '{name}': requested {qty}, available {self._stock[name]}"
            )
        self._stock[name] -= qty
        if self._stock[name] == 0:
            del self._stock[name]

    def check(self, name: str) -> int:
        """Return quantity of product in warehouse."""
        return self._stock.get(name, 0)

    def get_all(self) -> dict:
        """Return copy of all warehouse stock."""
        return dict(self._stock)