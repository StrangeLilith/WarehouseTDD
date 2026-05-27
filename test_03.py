import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_add_multiple_products():
    w = Warehouse()
    w.add("Socks", 10)
    w.add("Shirts", 5)
    assert w.check("Socks") == 10
    assert w.check("Shirts") == 5
