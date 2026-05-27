import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from warehouse import Warehouse, NegativeQuantityError

def test_remove_negative_raises_error():
    w = Warehouse()
    w.add("Socks", 10)
    with pytest.raises(NegativeQuantityError):
        w.remove("Socks", -2)
