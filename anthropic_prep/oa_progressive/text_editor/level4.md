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

- **undo()**
- **redo()**

## Level 4 - Extending Design & Functionality

The editor now supports named snapshots.

- **snapshot(name)**
  - Save the current document text and cursor position under `name`.
  - Return `True`.
  - If a snapshot with the same name already exists, overwrite it.
- **restore(name)**
  - Restore the document text and cursor position from the named snapshot.
  - Return the current document text.
  - If the snapshot does not exist, return `None`.
  - Restoring a snapshot is a mutating operation and should clear redo history.

