import unittest
from FileManager import FileManager
import os

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager()
        self.test_file = "test_file.txt"
        self.test_content = "This is a test."

        # Create a test file
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write(self.test_content)

    def tearDown(self):
        # Remove the test file
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

    def test_read_as_paragraphs(self):
        multi_para_content = "Paragraph one.\n\nParagraph two.\n\nParagraph three."
        self.file_manager.write_file(self.test_file, multi_para_content)
        paragraphs = self.file_manager.read_as_paragraphs(self.test_file)
        self.assertEqual(len(paragraphs), 3)
        self.assertEqual(paragraphs[0], "Paragraph one.")
        self.assertEqual(paragraphs[1], "Paragraph two.")
        self.assertEqual(paragraphs[2], "Paragraph three.")

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.file_manager.read_file("nonexistent.txt")
    

if __name__ == "__main__":
    unittest.main()
