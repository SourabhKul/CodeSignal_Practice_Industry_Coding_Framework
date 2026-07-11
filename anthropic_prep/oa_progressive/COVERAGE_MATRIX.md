# OA Coverage Matrix

This matrix separates reported Anthropic OA families from drills that merely train transferable CodeSignal skills. Public reports are anecdotal; Anthropic and CodeSignal do not publish the live question bank.

## Confidence Key

- **Repeated report**: supported by multiple independent candidate reports or reports across multiple years.
- **Reported**: at least one concrete public report or question-bank reconstruction.
- **Transfer drill**: useful skill practice without reliable evidence that Anthropic used this exact scenario.

## Matrix

| Drill | Evidence | Level 1 | Level 2 | Level 3 | Level 4 |
| --- | --- | --- | --- | --- | --- |
| `in_memory_db` | Repeated report | record CRUD | scans/prefix | timestamp + TTL | backup/restore |
| `banking_system` | Repeated report | accounts/payments | top spenders | pending transfers | merge/history |
| `cloud_storage` | Repeated report | file CRUD | filtered search | users/capacity | backup/restore |
| `recipe_manager` | Reported, current in 2026 | recipe CRUD | ingredient search/sort | users/editors | history/rollback |
| `employee_system` | Reported | attendance | time ranking | promotion/payroll | double-pay periods |
| `task_manager` | Reported | task CRUD | priority search | quota + TTL | completion/overdue |
| `course_registration` | Reported | courses/registration | shared-course pairs | grading/GPA | department ranking |
| `time_versioned_kv` | Transfer drill | key-value CRUD | prefix queries | time versions | compaction/history |
| `inventory_orders` | Transfer drill | products/stock | aggregation | reservations | reporting |
| `package_manager` | Transfer drill | packages/install | dependency order | cycle handling | dependents/removal |
| `build_system` | Transfer drill | targets/build | dependency order | recursive build | invalidation |
| `text_editor` | Transfer drill | basic edits | cursor editing | undo/redo | snapshots |

## Format Coverage

All folders use four cumulative level files. Candidate `solution.py` files expose only Level 1 methods; later APIs must be added as each level is opened. Reported-family folders include maintained `reference_solution.py` answer keys for post-run review.
