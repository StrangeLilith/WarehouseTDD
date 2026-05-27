import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from warehouse import Warehouse, NegativeQuantityError

def test_add_negative_raises_error():
    w = Warehouse()
    with pytest.raises(NegativeQuantityError):
        w.add("Socks", -5)
