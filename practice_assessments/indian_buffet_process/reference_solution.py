from fractions import Fraction


class IndianBuffet:
    def __init__(self, alpha):
        if not isinstance(alpha, int) or isinstance(alpha, bool) or alpha <= 0:
            raise ValueError("alpha must be a positive integer")
        self.alpha = alpha
        self.customers = []
        self.popularity = []
        self.tags = {}
        self.snapshots = {}

    @staticmethod
    def _positive_integer(value):
        return isinstance(value, int) and not isinstance(value, bool) and value > 0

    def add_customer(self, selection_tickets, new_dish_count):
        customer_count = len(self.customers)
        if (
            not isinstance(selection_tickets, list)
            or len(selection_tickets) != len(self.popularity)
            or not isinstance(new_dish_count, int)
            or isinstance(new_dish_count, bool)
            or new_dish_count < 0
        ):
            return None
        if any(
            not isinstance(ticket, int)
            or isinstance(ticket, bool)
            or ticket < 0
            or ticket >= customer_count
            for ticket in selection_tickets
        ):
            return None

        selected = {
            dish_number
            for dish_number, ticket in enumerate(selection_tickets, start=1)
            if ticket < self.popularity[dish_number - 1]
        }
        for dish_number in selected:
            self.popularity[dish_number - 1] += 1

        first_new_dish = len(self.popularity) + 1
        for dish_number in range(first_new_dish, first_new_dish + new_dish_count):
            selected.add(dish_number)
            self.popularity.append(1)

        self.customers.append(selected)
        return sorted(selected)

    def customer_dishes(self, customer_number):
        if not self._positive_integer(customer_number) or customer_number > len(self.customers):
            return None
        return sorted(self.customers[customer_number - 1])

    def dish_popularity(self, dish_number):
        if not self._positive_integer(dish_number) or dish_number > len(self.popularity):
            return 0
        return self.popularity[dish_number - 1]

    def feature_matrix(self):
        return [
            [int(dish_number in customer) for dish_number in range(1, len(self.popularity) + 1)]
            for customer in self.customers
        ]

    def popular_dishes(self, min_popularity):
        if not self._positive_integer(min_popularity):
            return []
        dishes = [
            (dish_number, count)
            for dish_number, count in enumerate(self.popularity, start=1)
            if count >= min_popularity
        ]
        return sorted(dishes, key=lambda item: (-item[1], item[0]))

    def expected_new_dishes(self):
        return Fraction(self.alpha, len(self.customers) + 1)

    def add_tag(self, customer_number, tag):
        if not self._positive_integer(customer_number) or customer_number > len(self.customers):
            return False
        if not isinstance(tag, str):
            return False
        tags = self.tags.setdefault(customer_number, set())
        if tag in tags:
            return False
        tags.add(tag)
        return True

    def customers_with_tag(self, tag):
        if not isinstance(tag, str):
            return []
        return sorted(customer for customer, tags in self.tags.items() if tag in tags)

    def recommend_dishes(self, customer_number, limit):
        if not self._positive_integer(customer_number) or customer_number > len(self.customers):
            return None
        if not self._positive_integer(limit):
            return []
        selected = self.customers[customer_number - 1]
        candidates = [
            (dish_number, popularity)
            for dish_number, popularity in enumerate(self.popularity, start=1)
            if dish_number not in selected
        ]
        candidates.sort(key=lambda item: (-item[1], item[0]))
        return [dish_number for dish_number, _ in candidates[:limit]]

    def _state_copy(self):
        return {
            "customers": [set(customer) for customer in self.customers],
            "popularity": list(self.popularity),
            "tags": {customer: set(tags) for customer, tags in self.tags.items()},
        }

    def save(self, name):
        if name in self.snapshots:
            return False
        self.snapshots[name] = self._state_copy()
        return True

    def restore(self, name):
        state = self.snapshots.get(name)
        if state is None:
            return False
        self.customers = [set(customer) for customer in state["customers"]]
        self.popularity = list(state["popularity"])
        self.tags = {customer: set(tags) for customer, tags in state["tags"].items()}
        return True

