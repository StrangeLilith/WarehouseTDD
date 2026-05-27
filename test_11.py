import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_get_all_products():
    w = Warehouse()
    w.add("A", 1)
    w.add("B", 2)
    assert w.get_all() == {"A": 1, "B": 2}
