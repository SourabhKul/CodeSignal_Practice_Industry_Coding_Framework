import unittest
from solution import TextEditor


class TestTextEditor(unittest.TestCase):
    def test_level_1_basic_editing(self):
        editor = TextEditor()
        self.assertEqual(editor.append("abc"), "abc")
        self.assertEqual(editor.delete(1), "ab")
        self.assertEqual(editor.delete(10), "")
        self.assertEqual(editor.get_text(), "")

    def test_level_2_cursor_editing(self):
        editor = TextEditor()
        editor.append("ac")
        self.assertEqual(editor.move(1), 1)
        self.assertEqual(editor.insert("b"), "abc")
        self.assertEqual(editor.delete_left(2), "c")

    def test_level_3_undo_redo(self):
        editor = TextEditor()
        editor.append("a")
        editor.append("b")
        self.assertEqual(editor.undo(), "a")
        self.assertEqual(editor.redo(), "ab")
        editor.delete(1)
        self.assertEqual(editor.redo(), "a")

    def test_level_4_snapshots(self):
        editor = TextEditor()
        editor.append("hello")
        self.assertTrue(editor.snapshot("base"))
        editor.append(" world")
        self.assertEqual(editor.restore("base"), "hello")
        self.assertIsNone(editor.restore("missing"))


if __name__ == "__main__":
    unittest.main()

