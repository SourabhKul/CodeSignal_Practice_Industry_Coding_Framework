import importlib
import os
import unittest


CourseRegistration = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).CourseRegistration


class TestCourseRegistration(unittest.TestCase):
    def test_level_1_registration(self):
        system = CourseRegistration()
        self.assertTrue(system.add_course("cs1", "Intro", 3))
        self.assertFalse(system.add_course("cs1", "Duplicate", 4))
        self.assertFalse(system.register_student("a", "missing"))
        self.assertTrue(system.register_student("a", "cs1"))
        self.assertFalse(system.register_student("a", "cs1"))
        self.assertFalse(system.unregister_student("b", "cs1"))
        self.assertTrue(system.unregister_student("a", "cs1"))
        self.assertFalse(system.unregister_student("a", "cs1"))

    def test_level_2_pairs(self):
        system = CourseRegistration()
        for course_id in ["cs1", "cs2"]:
            system.add_course(course_id, course_id, 3)
        for student in ["a", "b", "c"]:
            system.register_student(student, "cs1")
        for student in ["a", "b"]:
            system.register_student(student, "cs2")
        self.assertEqual(system.shared_course_pairs(), ["a,b", "a,c", "b,c"])
        self.assertEqual(system.courses_for_student("a"), ["cs1", "cs2"])
        self.assertEqual(system.courses_for_student("missing"), [])

    def test_level_3_grades(self):
        system = CourseRegistration()
        system.add_course("cs", "CS", 3)
        system.add_course("seminar", "Seminar", 1)
        system.register_student("a", "cs")
        system.register_student("a", "seminar")
        self.assertFalse(system.configure_course("missing", "eng", "standard"))
        self.assertFalse(system.configure_course("cs", "eng", "invalid"))
        self.assertTrue(system.configure_course("cs", "eng", "standard"))
        self.assertTrue(system.configure_course("seminar", "eng", "pass_fail"))
        self.assertFalse(system.record_grade("missing", "cs", "A"))
        self.assertFalse(system.record_grade("a", "cs", "Pass"))
        self.assertTrue(system.record_grade("a", "cs", "B"))
        self.assertTrue(system.record_grade("a", "seminar", "Pass"))
        self.assertEqual(system.gpa("a"), 3.25)
        self.assertIsNone(system.gpa("missing"))

    def test_level_4_departments(self):
        system = CourseRegistration()
        system.add_course("cs", "CS", 3)
        system.add_course("math", "Math", 3)
        system.configure_course("cs", "engineering", "standard")
        system.configure_course("math", "science", "standard")
        for student in ["a", "b"]:
            system.register_student(student, "cs")
        system.register_student("a", "math")
        system.record_grade("a", "cs", "B")
        system.record_grade("b", "cs", "A")
        system.record_grade("a", "math", "A")
        self.assertEqual(system.top_students_by_department("engineering", 2), ["b(4.00)", "a(3.00)"])
        self.assertEqual(system.top_students_by_department("science", 5), ["a(4.00)"])
        self.assertEqual(system.top_students_by_department("missing", 2), [])


if __name__ == "__main__":
    unittest.main()
