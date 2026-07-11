# Scenario

Your task is to implement a simplified version of an inventory and order system.

## Level 1 - Initial Design & Basic Functions

- **add_product(product_id, category, price)**
- **restock(product_id, quantity)**
- **purchase(product_id, quantity)**

## Level 2 - Data Structures & Data Processing

- **top_products(category, n)**
  - Return up to `n` products in `category`.
  - Order by stock descending.
  - If stock ties, order by product id ascending.
  - Return values in the format `["product_id(stock)", ...]`.
  - Return `[]` if no products match.
- **inventory_value(category)**
  - Return the total value of available inventory in the category: `sum(price * stock)`.
  - Return `0` if no products match.

### Examples

```python
store = InventoryOrders()
store.add_product("a", "books", 10)
store.add_product("b", "books", 20)
store.restock("a", 5)
store.restock("b", 5)
store.top_products("books", 2)       # ["a(5)", "b(5)"]
store.inventory_value("books")       # 150
```

