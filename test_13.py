import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_warehouse_empty_by_default():
    w = Warehouse()
    assert w.get_all() == {}
