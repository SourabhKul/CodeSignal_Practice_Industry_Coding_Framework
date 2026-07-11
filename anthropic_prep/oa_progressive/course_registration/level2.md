# Scenario

Implement an in-memory course-registration system. All Level 1 behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_course(course_id, name, credits)**
- **register_student(student_id, course_id)**
- **unregister_student(student_id, course_id)**

## Level 2 - Data Structures & Data Processing

- **shared_course_pairs()**
  - Return every unique student pair sharing at least one course.
  - Format pairs as `student_a,student_b` with ids ordered inside each pair.
  - Return pairs lexicographically and do not duplicate a pair that shares multiple courses.
- **courses_for_student(student_id)**
  - Return registered course ids lexicographically.
