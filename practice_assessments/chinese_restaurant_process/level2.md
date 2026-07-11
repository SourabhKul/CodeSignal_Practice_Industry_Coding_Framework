# Scenario

Implement an in-memory Chinese Restaurant Process simulator. All Level 1 behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **seat(ticket)**
- **customer_table(customer_number)**
- **table_size(table_number)**

## Level 2 - Data Structures & Data Processing

- **seat_many(tickets)**
  - Seat customers sequentially using the supplied tickets.
  - Return the table number assigned for each ticket.
  - If a ticket is invalid at its turn, append `None` for that ticket, leave state unchanged for it, and continue to the next ticket using the same customer count.
- **list_tables()**
  - Return `(table_number, size)` tuples ordered by size descending, then table number ascending.

### Example

```python
restaurant = ChineseRestaurant(2)
restaurant.seat_many([0, 2, 4, 1])  # [2, 1, 1, 3]
restaurant.list_tables()             # [(1, 3), (2, 1), (3, 1)]
```

