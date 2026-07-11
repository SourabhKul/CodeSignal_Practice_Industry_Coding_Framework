# Scenario

Your task is to implement a simplified version of a text editor.

## Level 1 - Initial Design & Basic Functions

- **append(text)**
- **delete(count)**
- **get_text()**

## Level 2 - Data Structures & Data Processing

The editor now has a cursor.

- **move(position)**
  - Move the cursor to `position`.
  - Positions are clamped between `0` and the document length.
  - Return the cursor position.
- **insert(text)**
  - Insert `text` at the cursor position and move the cursor after the inserted text.
  - Return the current document text.
- **delete_left(count)**
  - Delete up to `count` characters immediately left of the cursor.
  - Move the cursor to the start of the deleted range.
  - Return the current document text.

### Examples

```python
editor = TextEditor()
editor.append("ac")        # "ac"
editor.move(1)             # 1
editor.insert("b")         # "abc"
editor.delete_left(2)      # "c"
```

