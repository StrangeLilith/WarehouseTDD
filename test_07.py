import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_remove_exact_quantity_to_zero():
    w = Warehouse()
    w.add("Shirts", 5)
    w.remove("Shirts", 5)
    assert w.check("Shirts") == 0
