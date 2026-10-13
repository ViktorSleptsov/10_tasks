import os
import tempfile
import unittest
from notes import add_note, read_notes, clear_notes


class TestNotes(unittest.TestCase):
    def setUp(self):
        # временный файл для тестов
        fd, self.path = tempfile.mkstemp()
        os.close(fd)
        os.remove(self.path)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add_and_read(self):
        add_note("Купить хлеб", self.path)
        notes = read_notes(self.path)
        self.assertEqual(len(notes), 1)
        self.assertIn("Купить хлеб", notes[0])

    def test_empty_note(self):
        with self.assertRaises(ValueError):
            add_note("   ", self.path)

    def test_clear(self):
        add_note("A", self.path)
        add_note("B", self.path)
        clear_notes(self.path)
        self.assertEqual(read_notes(self.path), [])

    def test_read_missing_file(self):
        self.assertEqual(read_notes("no_such_file.txt"), [])


if __name__ == "__main__":
    unittest.main()