import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from warehouse import Warehouse, NotEnoughStockError

def test_remove_nonexistent_product_raises_error():
    w = Warehouse()
    with pytest.raises(NotEnoughStockError):
        w.remove("Chair", 1)
