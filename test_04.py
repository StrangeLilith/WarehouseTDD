import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_check_nonexistent_product():
    w = Warehouse()
    assert w.check("Umbrella") == 0
