import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_remove_decreases_quantity():
    w = Warehouse()
    w.add("Socks", 10)
    w.remove("Socks", 3)
    assert w.check("Socks") == 7
