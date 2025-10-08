"""
Example 1: Loop error (off-by-one)

Scenario:
- Aggregate order totals from a list of orders.
- Each order can have multiple line items.
- An off-by-one error is intentionally introduced when iterating items.
"""

from typing import List, Dict, Any


def compute_order_total(order: Dict[str, Any]) -> float:
    """Compute total price for a single order (contains intentional bug)."""
    items = order.get("items", [])
    total = 0.0

    # BUG: loop goes one past the end, causing IndexError
    for i in range(len(items) + 1):  # ❌ IndexError when i == len(items)
        line = items[i]
        total += line["unit_price"] * line["quantity"]
    return total


def compute_batch_total(orders: List[Dict[str, Any]]) -> float:
    """Compute total price for a batch of orders."""
    batch_total = 0.0
    for order in orders:
        batch_total += compute_order_total(order)
    return batch_total


if __name__ == "__main__":
    orders = [
        {
            "id": "A100",
            "items": [
                {"sku": "pen", "unit_price": 1.5, "quantity": 4},
                {"sku": "notebook", "unit_price": 3.0, "quantity": 2},
            ],
        },
        {
            "id": "B200",
            "items": [
                {"sku": "stapler", "unit_price": 6.75, "quantity": 1},
            ],
        },
    ]
    # Expected total (if correct): (1.5*4 + 3.0*2) + (6.75*1) = 18.75
    # Actual: IndexError due to off-by-one bug
    print("Batch total:", compute_batch_total(orders))
