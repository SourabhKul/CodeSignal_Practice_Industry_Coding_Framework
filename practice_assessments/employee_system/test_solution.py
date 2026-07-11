import importlib
import os
import unittest


EmployeeSystem = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).EmployeeSystem


class TestEmployeeSystem(unittest.TestCase):
    def test_level_1_time(self):
        system = EmployeeSystem()
        self.assertTrue(system.add_employee("a", "engineer", 10))
        self.assertFalse(system.add_employee("a", "manager", 20))
        self.assertFalse(system.clock_in(1, "missing"))
        self.assertTrue(system.clock_in(1, "a"))
        self.assertFalse(system.clock_in(2, "a"))
        self.assertTrue(system.clock_out(6, "a"))
        self.assertFalse(system.clock_out(7, "a"))
        self.assertEqual(system.get_total_time("a"), 5)
        system.clock_in(10, "a")
        system.clock_out(13, "a")
        self.assertEqual(system.get_total_time("a"), 8)
        self.assertIsNone(system.get_total_time("missing"))

    def test_level_2_ranking(self):
        system = EmployeeSystem()
        for employee_id in ["b", "a", "c"]:
            system.add_employee(employee_id, "engineer", 10)
        system.add_employee("m", "manager", 20)
        system.clock_in(1, "a")
        system.clock_out(6, "a")
        system.clock_in(10, "b")
        system.clock_out(15, "b")
        system.clock_in(20, "c")
        system.clock_out(22, "c")
        self.assertEqual(system.top_employees("engineer", 2), ["a(5)", "b(5)"])
        self.assertEqual(system.top_employees("manager", 5), ["m(0)"])
        self.assertEqual(system.top_employees("missing", 2), [])

    def test_level_3_promotions(self):
        system = EmployeeSystem()
        system.add_employee("a", "junior", 10)
        self.assertTrue(system.announce_promotion("a", "senior", 20, 10))
        self.assertFalse(system.announce_promotion("a", "staff", 30, 20))
        system.clock_in(5, "a")
        system.clock_out(8, "a")
        self.assertEqual(system.top_employees("junior", 1), ["a(3)"])
        system.clock_in(10, "a")
        system.clock_out(14, "a")
        self.assertEqual(system.top_employees("senior", 1), ["a(7)"])
        self.assertEqual(system.calculate_salary("a", 0, 20), 110)
        self.assertEqual(system.calculate_salary("a", 6, 12), 60)
        self.assertIsNone(system.calculate_salary("missing", 0, 20))

    def test_level_4_double_pay(self):
        system = EmployeeSystem()
        system.add_employee("a", "engineer", 10)
        system.clock_in(0, "a")
        system.clock_out(10, "a")
        self.assertFalse(system.define_double_pay_period(5, 5))
        self.assertTrue(system.define_double_pay_period(2, 6))
        self.assertEqual(system.calculate_salary("a", 0, 10), 140)
        self.assertTrue(system.define_double_pay_period(4, 8))
        self.assertEqual(system.calculate_salary("a", 0, 10), 160)
        self.assertEqual(system.calculate_salary("a", 5, 7), 40)


if __name__ == "__main__":
    unittest.main()
