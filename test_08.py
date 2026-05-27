import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from warehouse import Warehouse, NotEnoughStockError

def test_remove_too_much_raises_error():
    w = Warehouse()
    w.add("Socks", 10)
    with pytest.raises(NotEnoughStockError):
        w.remove("Socks", 20)
