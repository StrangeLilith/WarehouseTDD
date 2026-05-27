import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_complex_operations():
    w = Warehouse()
    w.add("Socks", 100)
    w.add("Shirts", 50)
    w.remove("Socks", 20)
    w.add("Socks", 10)
    w.remove("Shirts", 50)
    assert w.check("Socks") == 90
    assert w.check("Shirts") == 0
