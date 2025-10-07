"""
Example 1: Loop error fixed

Fix:
- Iterate exactly over item indices or, better, iterate over items directly.
"""

from typing import List, Dict, Any


def compute_order_total(order: Dict[str, Any]) -> float:
    """Compute total price for a single order."""
    items = order.get("items", [])
    total = 0.0

    # FIX: iterate directly over items (pythonic), or use range(len(items))
    for line in items:  # ✅ No off-by-one
        total += line["unit_price"] * line["quantity"]
    return total


def compute_batch_total(orders: List[Dict[str, Any]]) -> float:
    """Compute total price for a batch of orders, with simple validation."""
    batch_total = 0.0
    for order in orders:
        if "items" not in order or not isinstance(order["items"], list):
            # Defensive programming: treat invalid orders as empty
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
    print("Batch total:", compute_batch_total(orders))  # Expected: 6.0 + 6.75 + 0.0 = 12.75

