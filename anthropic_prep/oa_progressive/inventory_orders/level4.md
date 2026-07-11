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

- **reserve_at(timestamp, product_id, quantity, ttl)**
- **complete_reservation_at(timestamp, reservation_id)**
- **purchase_at(timestamp, product_id, quantity)**

## Level 4 - Extending Design & Functionality

The system now supports product discontinuation and sales reporting.

- **discontinue(product_id)**
  - Mark a product as discontinued.
  - Return `True` if the product exists and was active.
  - Return `False` otherwise.
  - Discontinued products cannot be restocked, reserved, or purchased.
  - Existing alive reservations for the product should be canceled and their stock released.
- **sales_report(category)**
  - Return products in the category that have sold at least one unit.
  - Order by total revenue descending.
  - If revenue ties, order by product id ascending.
  - Return values in the format `["product_id(quantity_sold,revenue)", ...]`.

### Examples

```python
store = InventoryOrders()
store.add_product("book", "books", 25)
store.restock("book", 10)
store.purchase("book", 4)
store.sales_report("books")           # ["book(4,100)"]
store.discontinue("book")             # True
store.purchase("book", 1)             # None
```

