import importlib.util
import pathlib

SCRIPT_PATH = (
    pathlib.Path(__file__).parent.parent
    / "examples"
    / "example_1_loop_error"
    / "fixed_script.py"
)

spec = importlib.util.spec_from_file_location("fixed_script", SCRIPT_PATH)
fixed_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixed_script)



def test_compute_order_total_basic():
    order = {
        "id": "A100",
        "items": [
            {"sku": "pen", "unit_price": 1.5, "quantity": 4},       # 6.0
            {"sku": "notebook", "unit_price": 3.0, "quantity": 2},  # 6.0
        ],
    }
    assert fixed_script.compute_order_total(order) == 12.0


def test_compute_batch_total_with_empty_order():
    orders = [
        {"id": "A100", "items": [{"sku": "pen", "unit_price": 2.0, "quantity": 3}]},  # 6.0
        {"id": "C300", "items": []},  # 0.0
    ]
    assert fixed_script.compute_batch_total(orders) == 6.0

