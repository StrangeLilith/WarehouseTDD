import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_add_single_product():
    w = Warehouse()
    w.add("Socks", 10)
    assert w.check("Socks") == 10
