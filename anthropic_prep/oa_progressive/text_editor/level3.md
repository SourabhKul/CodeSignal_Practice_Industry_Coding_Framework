# Scenario

Your task is to implement a simplified version of a text editor.

## Level 1 - Initial Design & Basic Functions

- **append(text)**
- **delete(count)**
- **get_text()**

## Level 2 - Data Structures & Data Processing

- **move(position)**
- **insert(text)**
- **delete_left(count)**

## Level 3 - Refactoring & Encapsulation

The editor now supports undo and redo.

- **undo()**
  - Undo the most recent mutating operation.
  - Return the current document text.
  - If there is nothing to undo, return the current document text.
- **redo()**
  - Redo the most recently undone operation.
  - Return the current document text.
  - If there is nothing to redo, return the current document text.

Mutating operations are `append`, `delete`, `insert`, and `delete_left`. Cursor movement alone is not a mutating
operation.

