# Practice Coverage Matrix

| Drill | Level 1 | Level 2 | Level 3 | Level 4 |
| --- | --- | --- | --- | --- |
| `in_memory_db` | record CRUD | scans/prefix | timestamp + TTL | backup/restore |
| `banking_system` | accounts/payments | top spenders | pending transfers | merge/history |
| `cloud_storage` | file CRUD | filtered search | users/capacity | backup/restore |
| `recipe_manager` | recipe CRUD | ingredient search/sort | users/editors | history/rollback |
| `employee_system` | attendance | time ranking | promotion/payroll | double-pay periods |
| `task_manager` | task CRUD | priority search | quota + TTL | completion/overdue |
| `course_registration` | courses/registration | shared-course pairs | grading/GPA | department ranking |
| `time_versioned_kv` | key-value CRUD | prefix queries | time versions | compaction/history |
| `inventory_orders` | products/stock | aggregation | reservations | reporting |
| `package_manager` | packages/install | dependency order | cycle handling | dependents/removal |
| `build_system` | targets/build | dependency order | recursive build | invalidation |
| `text_editor` | basic edits | cursor editing | undo/redo | snapshots |
| `chinese_restaurant_process` | deterministic seating | bulk/ranking | snapshots | forks/comparison |
| `indian_buffet_process` | deterministic feature sampling | matrix/popularity | tags/recommendations | snapshots |
