# Scenario

Implement an in-memory Indian Buffet Process simulator. Customers arrive one by one and choose any number of dishes (features).

In the standard IBP, after `n` customers have arrived, an existing dish with popularity `m` is selected by the next customer with probability `m / n`. The next customer also tries a Poisson-distributed number of new dishes with mean `alpha / (n + 1)`.

To make outcomes deterministic, `add_customer` receives one ticket per existing dish and a precomputed new-dish count. For each existing dish, its ticket must be an integer in `[0, n - 1]`; select that dish when `ticket < popularity`. A uniformly random ticket therefore selects a dish with probability `popularity / n`.

## Level 1 - Initial Design & Basic Functions

Construct `IndianBuffet(alpha)` with a positive integer concentration parameter.

- **add_customer(selection_tickets, new_dish_count)**
  - Add the next customer and return their dish numbers in ascending order.
  - `selection_tickets` must contain exactly one ticket per existing dish. The first customer therefore supplies `[]`.
  - `new_dish_count` is a non-negative integer representing a precomputed Poisson outcome.
  - Return `None` without changing state when any supplied value is invalid for the current state.
- **customer_dishes(customer_number)**
  - Return the customer's dish numbers in ascending order, or `None` when the positive one-based customer number does not exist.
- **dish_popularity(dish_number)**
  - Return the number of customers who selected the dish, or `0` when the positive one-based dish number does not exist.

Dishes are numbered consecutively in creation order. Aim for `O(K)` time for `add_customer`, where `K` is the current number of dishes.

