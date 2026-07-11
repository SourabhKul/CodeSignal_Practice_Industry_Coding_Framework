import unittest
from solution import Tokenizer


class TestTokenizerReview(unittest.TestCase):
    def test_longest_match_for_overlapping_tokens(self):
        tokenizer = Tokenizer(["a", "ab", "abc", " "])
        self.assertEqual(tokenizer.tokenize("abc ab"), ["abc", " ", "ab"])

    def test_unknown_round_trip_marker_collision(self):
        tokenizer = Tokenizer(["hello", "UNK", " "])
        tokens = tokenizer.tokenize("hello UNK ?")
        self.assertEqual(tokenizer.detokenize(tokens), "hello UNK ?")

    def test_empty_input(self):
        tokenizer = Tokenizer(["a"])
        self.assertEqual(tokenizer.tokenize(""), [])
        self.assertEqual(tokenizer.detokenize([]), "")


if __name__ == "__main__":
    unittest.main()

