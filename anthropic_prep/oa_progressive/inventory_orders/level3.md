# Scenario

Your task is to implement a simplified version of an inventory and order system.

## Level 1 - Initial Design & Basic Functions

- **add_product(product_id, category, price)**
- **restock(product_id, quantity)**
- **purchase(product_id, quantity)**

## Level 2 - Data Structures & Data Processing

- **top_products(category, n)**
- **inventory_value(category)**

## Level 3 - Refactoring & Encapsulation

The system now supports timestamped reservations. Reserved stock is not available for purchase until the
reservation is either completed or expired.

- **reserve_at(timestamp, product_id, quantity, ttl)**
  - Reserve `quantity` units for `ttl` seconds.
  - Return a unique reservation id in the format `"reservation1"`, `"reservation2"`, etc.
  - If the product does not exist or there is not enough available stock, return `None`.
  - A reservation is alive for timestamps `created_timestamp <= t < created_timestamp + ttl`.
- **complete_reservation_at(timestamp, reservation_id)**
  - Complete an alive reservation and convert it into a purchase.
  - Return `True` if completed, otherwise `False`.
- **purchase_at(timestamp, product_id, quantity)**
  - Buy from currently available stock.
  - Expired reservations should no longer reduce available stock.
  - Return the remaining available stock for the product, or `None`.

### Examples

```python
store = InventoryOrders()
store.add_product("game", "games", 60)
store.restock("game", 5)
rid = store.reserve_at(10, "game", 3, 5)       # "reservation1"
store.purchase_at(11, "game", 3)               # None
store.complete_reservation_at(12, rid)         # True
store.purchase_at(13, "game", 2)               # 0
```

