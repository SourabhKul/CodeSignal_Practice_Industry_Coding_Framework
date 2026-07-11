# Scenario

Your task is to implement a simplified version of a text editor.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Level 1 - Initial Design & Basic Functions

- **append(text)**
  - Append `text` to the end of the document.
  - Return the current document text.
- **delete(count)**
  - Delete up to `count` characters from the end of the document.
  - Return the current document text.
- **get_text()**
  - Return the current document text.

### Examples

```python
editor = TextEditor()
editor.append("abc")       # "abc"
editor.delete(1)           # "ab"
editor.delete(10)          # ""
```

