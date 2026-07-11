# Live Drill: Duplicate File Finder

Implement `find_duplicate_files(root)`.

Requirements:

- Traverse a directory recursively.
- Group files with identical content.
- Return only duplicate groups.
- Avoid loading entire large files into memory.
- Return groups as sorted path lists, and sort the list of groups by first path for deterministic tests.

Optimization path:

1. Group by file size.
2. Hash candidates in chunks.
3. Only compare full bytes if asked.

