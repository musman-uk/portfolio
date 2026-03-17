"""
Example 1: Loop error fixed

Fix:
- Iterate directly over items instead of using an off-by-one index range.
"""

from typing import List, Dict, Any


def compute_order_total(order: Dict[str, Any]) -> float:
    """Compute total price for a single order."""
    items = order.get("items", [])
    total = 0.0

    # FIX: iterate directly over items to avoid off-by-one errors
    for line in items:
        total += line["unit_price"] * line["quantity"]
    return total


def compute_batch_total(orders: List[Dict[str, Any]]) -> float:
    """Compute total price for a batch of orders, with basic validation."""
    batch_total = 0.0
    for order in orders:
        if "items" not in order or not isinstance(order["items"], list):
            # Skip invalid orders
            continue
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
        {"id": "B200", "items": [{"sku": "stapler", "unit_price": 6.75, "quantity": 1}]},
        # Edge case: empty items list
        {"id": "C300", "items": []},
    ]
    # Expected total: (1.5*4 + 3.0*2) + (6.75*1) + 0.0 = 18.75
    print("Batch total:", compute_batch_total(orders))
