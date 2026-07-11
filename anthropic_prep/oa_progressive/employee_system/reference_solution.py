class EmployeeSystem:
    def __init__(self):
        self.employees = {}
        self.double_pay_periods = []

    def add_employee(self, employee_id, position, pay_rate):
        if employee_id in self.employees:
            return False
        self.employees[employee_id] = {
            "position": position,
            "rate": pay_rate,
            "clock_in": None,
            "clock_rate": None,
            "sessions": [],
            "pending": None,
        }
        return True

    def clock_in(self, timestamp, employee_id):
        employee = self.employees.get(employee_id)
        if employee is None or employee["clock_in"] is not None:
            return False
        pending = employee["pending"]
        if pending is not None and timestamp >= pending["effective_from"]:
            employee["position"] = pending["position"]
            employee["rate"] = pending["rate"]
            employee["pending"] = None
        employee["clock_in"] = timestamp
        employee["clock_rate"] = employee["rate"]
        return True

    def clock_out(self, timestamp, employee_id):
        employee = self.employees.get(employee_id)
        if employee is None or employee["clock_in"] is None or timestamp < employee["clock_in"]:
            return False
        employee["sessions"].append((employee["clock_in"], timestamp, employee["clock_rate"]))
        employee["clock_in"] = None
        employee["clock_rate"] = None
        return True

    def get_total_time(self, employee_id):
        employee = self.employees.get(employee_id)
        if employee is None:
            return None
        return sum(end - start for start, end, _ in employee["sessions"])

    def top_employees(self, position, n):
        ranked = [
            (employee_id, self.get_total_time(employee_id))
            for employee_id, employee in self.employees.items()
            if employee["position"] == position
        ]
        ranked.sort(key=lambda item: (-item[1], item[0]))
        return [f"{employee_id}({total})" for employee_id, total in ranked[:n]]

    def announce_promotion(self, employee_id, new_position, new_pay_rate, effective_from):
        employee = self.employees.get(employee_id)
        if employee is None or employee["pending"] is not None:
            return False
        employee["pending"] = {
            "position": new_position,
            "rate": new_pay_rate,
            "effective_from": effective_from,
        }
        return True

    def define_double_pay_period(self, start_timestamp, end_timestamp):
        if start_timestamp >= end_timestamp:
            return False
        self.double_pay_periods.append((start_timestamp, end_timestamp))
        return True

    def _double_overlap(self, start, end):
        intervals = []
        for period_start, period_end in self.double_pay_periods:
            left = max(start, period_start)
            right = min(end, period_end)
            if left < right:
                intervals.append((left, right))
        intervals.sort()
        merged = []
        for left, right in intervals:
            if not merged or left > merged[-1][1]:
                merged.append([left, right])
            else:
                merged[-1][1] = max(merged[-1][1], right)
        return sum(right - left for left, right in merged)

    def calculate_salary(self, employee_id, start_timestamp, end_timestamp):
        employee = self.employees.get(employee_id)
        if employee is None:
            return None
        salary = 0
        for session_start, session_end, rate in employee["sessions"]:
            left = max(session_start, start_timestamp)
            right = min(session_end, end_timestamp)
            if left >= right:
                continue
            duration = right - left
            salary += duration * rate
            salary += self._double_overlap(left, right) * rate
        return salary
