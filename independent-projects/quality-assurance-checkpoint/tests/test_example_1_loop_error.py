import importlib.util
import pathlib

# Dynamically load the fixed script for Example 1 - Loop Error
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
    """
    Verify that compute_order_total correctly sums line items
    for a single order with multiple products.
    """
    order = {
        "id": "A100",
        "items": [
            {"sku": "pen", "unit_price": 1.5, "quantity": 4},
            {"sku": "notebook", "unit_price": 3.0, "quantity": 2},
        ],
    }
    # Expect total = 12.0; ensures the off-by-one bug is resolved
    assert fixed_script.compute_order_total(order) == 12.0


def test_compute_batch_total_with_empty_order():
    """
    Verify that compute_batch_total handles a mix of valid and empty orders.
    The empty order should contribute 0.0 to the batch total.
    """
    orders = [
        {"id": "A100", "items": [{"sku": "pen", "unit_price": 2.0, "quantity": 3}]},
        {"id": "C300", "items": []},  # Edge case: no items
    ]
    # Expect total = 6.0; confirms empty orders are safely included
    assert fixed_script.compute_batch_total(orders) == 6.0
