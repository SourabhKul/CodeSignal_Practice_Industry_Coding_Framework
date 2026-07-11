# Live Drill: Web Crawler

Implement a crawler that returns all URLs reachable from `start_url` within the same domain.

Start single-threaded with BFS. Then make it concurrent.

Requirements tested:

- Do not crawl outside the starting domain.
- Do not visit the same URL twice.
- Return a sorted list for deterministic tests.
- `crawl_concurrent` should use `ThreadPoolExecutor` or equivalent synchronization.

