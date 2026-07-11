# Scenario

Your task is to implement a simplified version of an inventory and order system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

The system stores products, prices, and available stock.

Example of inventory state:

```plaintext
[inventory]
    +- sku-1  category=book   price=25  stock=10
    +- sku-2  category=game   price=60  stock=3
```

## Level 1 - Initial Design & Basic Functions

- **add_product(product_id, category, price)**
  - Add a product with stock `0`.
  - Return `True` if the product was added.
  - If the product already exists, return `False`.
- **restock(product_id, quantity)**
  - Increase stock by `quantity`.
  - Return the new stock.
  - If the product does not exist, return `None`.
- **purchase(product_id, quantity)**
  - Buy `quantity` units of a product.
  - Return the remaining stock.
  - If the product does not exist or there is not enough stock, return `None`.

### Examples

```python
store = InventoryOrders()
store.add_product("book-1", "books", 25)     # True
store.add_product("book-1", "books", 30)     # False
store.restock("book-1", 10)                  # 10
store.purchase("book-1", 3)                  # 7
store.purchase("book-1", 100)                # None
```

