class ChineseRestaurant:
    def __init__(self, alpha):
        if not isinstance(alpha, int) or isinstance(alpha, bool) or alpha <= 0:
            raise ValueError("alpha must be a positive integer")
        self.alpha = alpha
        self.assignments = [1]
        self.sizes = [1]
        self.next_table = 2
        self.snapshots = {}

    def seat(self, ticket):
        customer_count = len(self.assignments)
        if (
            not isinstance(ticket, int)
            or isinstance(ticket, bool)
            or ticket < 0
            or ticket >= self.alpha + customer_count
        ):
            return None

        if ticket < self.alpha:
            table = self.next_table
            self.next_table += 1
            self.sizes.append(0)
        else:
            table = self.assignments[ticket - self.alpha]

        self.assignments.append(table)
        self.sizes[table - 1] += 1
        return table

    def customer_table(self, customer_number):
        if (
            not isinstance(customer_number, int)
            or isinstance(customer_number, bool)
            or customer_number < 1
            or customer_number > len(self.assignments)
        ):
            return None
        return self.assignments[customer_number - 1]

    def table_size(self, table_number):
        if (
            not isinstance(table_number, int)
            or isinstance(table_number, bool)
            or table_number < 1
            or table_number > len(self.sizes)
        ):
            return 0
        return self.sizes[table_number - 1]

    def seat_many(self, tickets):
        return [self.seat(ticket) for ticket in tickets]

    def list_tables(self):
        tables = enumerate(self.sizes, start=1)
        return sorted(tables, key=lambda item: (-item[1], item[0]))

    def _state_copy(self):
        return (list(self.assignments), list(self.sizes), self.next_table)

    def save(self, name):
        if name in self.snapshots:
            return False
        self.snapshots[name] = self._state_copy()
        return True

    def restore(self, name):
        state = self.snapshots.get(name)
        if state is None:
            return False
        assignments, sizes, next_table = state
        self.assignments = list(assignments)
        self.sizes = list(sizes)
        self.next_table = next_table
        return True

    def delete_snapshot(self, name):
        if name not in self.snapshots:
            return False
        del self.snapshots[name]
        return True

    def fork(self, name):
        state = self.snapshots.get(name)
        if state is None:
            return None
        forked = ChineseRestaurant(self.alpha)
        assignments, sizes, next_table = state
        forked.assignments = list(assignments)
        forked.sizes = list(sizes)
        forked.next_table = next_table
        return forked

    def compare_snapshots(self, first, second):
        first_state = self.snapshots.get(first)
        second_state = self.snapshots.get(second)
        if first_state is None or second_state is None:
            return None

        first_sizes = first_state[1]
        second_sizes = second_state[1]
        table_count = max(len(first_sizes), len(second_sizes))
        changes = []
        for index in range(table_count):
            before = first_sizes[index] if index < len(first_sizes) else 0
            after = second_sizes[index] if index < len(second_sizes) else 0
            if before != after:
                changes.append((index + 1, after - before))
        return changes

