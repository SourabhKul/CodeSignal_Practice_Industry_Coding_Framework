# Scenario

Implement an in-memory course-registration and grading system. All previous behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_course(course_id, name, credits)**
- **register_student(student_id, course_id)**
- **unregister_student(student_id, course_id)**

## Level 2 - Data Structures & Data Processing

- **shared_course_pairs()**
- **courses_for_student(student_id)**

## Level 3 - Refactoring & Encapsulation

- **configure_course(course_id, department, grading_type)**
  - Set a department and a grading type of either `standard` or `pass_fail`.
  - Return `False` for a missing course or invalid type.
- **record_grade(student_id, course_id, grade)**
  - Record a grade only for a registered student and a configured course.
  - Standard grades: `A`, `B`, `C`, `D`, `F`. Pass/fail grades: `Pass`, `Fail`.
- **gpa(student_id)**
  - Return the credit-weighted GPA across graded courses, or `None` when no grade exists.
  - Points are A/Pass=4, B=3, C=2, D=1, F/Fail=0.
