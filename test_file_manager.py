import unittest
from file_manager import FileManager
import os


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager()
        self.test_file = "test_file.txt"
        self.test_content = "This is a test."

        with open(self.test_file, "w", encoding="utf-8") as file:
            file.write(self.test_content)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_file(self):
        content = self.file_manager.read_file(self.test_file)
        self.assertEqual(content, self.test_content)

    def test_write_file(self):
        new_content = "New content."
        self.file_manager.write_file(self.test_file, new_content)
        content = self.file_manager.read_file(self.test_file)
        self.assertEqual(content, new_content)

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.file_manager.read_file("nonexistent.txt")


if __name__ == "__main__":
    unittest.main()
