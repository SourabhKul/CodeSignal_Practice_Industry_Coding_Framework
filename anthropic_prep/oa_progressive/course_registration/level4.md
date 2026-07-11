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
- **record_grade(student_id, course_id, grade)**
- **gpa(student_id)**

## Level 4 - Extending Design & Functionality

- **top_students_by_department(department, n)**
  - Rank students using credit-weighted GPA from graded courses in the department only.
  - Sort by GPA descending, then student id ascending.
  - Format as `student_id(gpa)` with GPA rounded to two decimal places.
  - Exclude students with no graded course in the department.
