import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from warehouse import Warehouse

def test_warehouse_day_simulation():
    w = Warehouse()
    w.add("Boxes", 100)
    w.add("Tape", 50)
    w.remove("Boxes", 20)
    w.remove("Tape", 5)
    assert w.get_all() == {"Boxes": 80, "Tape": 45}
