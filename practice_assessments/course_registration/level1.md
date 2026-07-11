# Scenario

Implement an in-memory course-registration system.

## Level 1 - Initial Design & Basic Functions

- **add_course(course_id, name, credits)**
  - Add a course and return `True`; return `False` for a duplicate id.
- **register_student(student_id, course_id)**
  - Register a student and return `True`.
  - Return `False` for a missing course or duplicate registration.
- **unregister_student(student_id, course_id)**
  - Remove a registration and return `True`; otherwise return `False`.
