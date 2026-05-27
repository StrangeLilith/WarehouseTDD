import pytest
from warehouse import Warehouse, NotEnoughStockError, NegativeQuantityError


def test_create_warehouse():
    w = Warehouse()
    assert w is not None


def test_add_single_product():
    w = Warehouse()
    w.add("Socks", 10)
    assert w.check("Socks") == 10


def test_add_multiple_products():
    w = Warehouse()
    w.add("Socks", 10)
    w.add("Shirts", 5)
    assert w.check("Socks") == 10
    assert w.check("Shirts") == 5


def test_check_nonexistent_product():
    w = Warehouse()
    assert w.check("Umbrella") == 0


def test_add_increases_quantity():
    w = Warehouse()
    w.add("Socks", 10)
    w.add("Socks", 5)
    assert w.check("Socks") == 15


def test_remove_decreases_quantity():
    w = Warehouse()
    w.add("Socks", 10)
    w.remove("Socks", 3)
    assert w.check("Socks") == 7


def test_remove_exact_quantity_to_zero():
    w = Warehouse()
    w.add("Shirts", 5)
    w.remove("Shirts", 5)
    assert w.check("Shirts") == 0


def test_remove_too_much_raises_error():
    w = Warehouse()
    w.add("Socks", 10)
    with pytest.raises(NotEnoughStockError):
        w.remove("Socks", 20)


def test_add_negative_raises_error():
    w = Warehouse()
    with pytest.raises(NegativeQuantityError):
        w.add("Socks", -5)


def test_remove_negative_raises_error():
    w = Warehouse()
    w.add("Socks", 10)
    with pytest.raises(NegativeQuantityError):
        w.remove("Socks", -2)


def test_get_all_products():
    w = Warehouse()
    w.add("A", 1)
    w.add("B", 2)
    assert w.get_all() == {"A": 1, "B": 2}


def test_complex_operations():
    w = Warehouse()
    w.add("Socks", 100)
    w.add("Shirts", 50)
    w.remove("Socks", 20)
    w.add("Socks", 10)
    w.remove("Shirts", 50)
    assert w.check("Socks") == 90
    assert w.check("Shirts") == 0


def test_warehouse_empty_by_default():
    w = Warehouse()
    assert w.get_all() == {}


def test_remove_nonexistent_product_raises_error():
    w = Warehouse()
    with pytest.raises(NotEnoughStockError):
        w.remove("Chair", 1)


def test_warehouse_day_simulation():
    w = Warehouse()
    w.add("Boxes", 100)
    w.add("Tape", 50)
    w.remove("Boxes", 20)
    w.remove("Tape", 5)
    assert w.get_all() == {"Boxes": 80, "Tape": 45}