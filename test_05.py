import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_add_increases_quantity():
    w = Warehouse()
    w.add("Socks", 10)
    w.add("Socks", 5)
    assert w.check("Socks") == 15
