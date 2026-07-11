from itertools import combinations


class CourseRegistration:
    STANDARD_POINTS = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    PASS_FAIL_POINTS = {"Pass": 4, "Fail": 0}

    def __init__(self):
        self.courses = {}
        self.registrations = {}
        self.grades = {}

    def add_course(self, course_id, name, credits):
        if course_id in self.courses:
            return False
        self.courses[course_id] = {
            "name": name,
            "credits": credits,
            "department": None,
            "grading_type": None,
        }
        self.registrations[course_id] = set()
        return True

    def register_student(self, student_id, course_id):
        if course_id not in self.courses or student_id in self.registrations[course_id]:
            return False
        self.registrations[course_id].add(student_id)
        return True

    def unregister_student(self, student_id, course_id):
        if course_id not in self.courses or student_id not in self.registrations[course_id]:
            return False
        self.registrations[course_id].remove(student_id)
        self.grades.pop((student_id, course_id), None)
        return True

    def shared_course_pairs(self):
        pairs = set()
        for students in self.registrations.values():
            for first, second in combinations(sorted(students), 2):
                pairs.add((first, second))
        return [f"{first},{second}" for first, second in sorted(pairs)]

    def courses_for_student(self, student_id):
        return sorted(course_id for course_id, students in self.registrations.items() if student_id in students)

    def configure_course(self, course_id, department, grading_type):
        if course_id not in self.courses or grading_type not in {"standard", "pass_fail"}:
            return False
        self.courses[course_id]["department"] = department
        self.courses[course_id]["grading_type"] = grading_type
        return True

    def record_grade(self, student_id, course_id, grade):
        course = self.courses.get(course_id)
        if course is None or course["grading_type"] is None or student_id not in self.registrations[course_id]:
            return False
        points = self.STANDARD_POINTS if course["grading_type"] == "standard" else self.PASS_FAIL_POINTS
        if grade not in points:
            return False
        self.grades[(student_id, course_id)] = points[grade]
        return True

    def _gpa_for(self, student_id, department=None):
        weighted_points = 0
        credits = 0
        for (graded_student, course_id), points in self.grades.items():
            course = self.courses[course_id]
            if graded_student != student_id or (department is not None and course["department"] != department):
                continue
            weighted_points += points * course["credits"]
            credits += course["credits"]
        return None if credits == 0 else weighted_points / credits

    def gpa(self, student_id):
        return self._gpa_for(student_id)

    def top_students_by_department(self, department, n):
        students = {student_id for student_id, _ in self.grades}
        ranked = [
            (student_id, gpa)
            for student_id in students
            if (gpa := self._gpa_for(student_id, department)) is not None
        ]
        ranked.sort(key=lambda item: (-item[1], item[0]))
        return [f"{student_id}({gpa:.2f})" for student_id, gpa in ranked[:n]]
