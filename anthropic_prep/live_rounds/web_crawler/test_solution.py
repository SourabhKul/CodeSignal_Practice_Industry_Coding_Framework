import unittest
from solution import crawl, crawl_concurrent


GRAPH = {
    "https://example.com": ["https://example.com/a", "https://example.com/b", "https://other.com/x"],
    "https://example.com/a": ["https://example.com/c"],
    "https://example.com/b": ["https://example.com/c"],
    "https://example.com/c": [],
}


def fetch(url):
    return GRAPH.get(url, [])


class TestWebCrawler(unittest.TestCase):
    def test_crawl_same_domain(self):
        expected = ["https://example.com", "https://example.com/a", "https://example.com/b", "https://example.com/c"]
        self.assertEqual(crawl("https://example.com", fetch), expected)

    def test_crawl_concurrent_same_domain(self):
        expected = ["https://example.com", "https://example.com/a", "https://example.com/b", "https://example.com/c"]
        self.assertEqual(crawl_concurrent("https://example.com", fetch, max_workers=2), expected)


if __name__ == "__main__":
    unittest.main()

