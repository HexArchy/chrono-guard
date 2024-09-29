import unittest
import os
from src.utils.file_manager import FileManager


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_data")
        os.makedirs(self.test_dir, exist_ok=True)
        self.file_manager = FileManager()
        self.file_manager.names_file = os.path.join(self.test_dir, "test_names.dat")

    def tearDown(self):
        if os.path.exists(self.file_manager.names_file):
            os.remove(self.file_manager.names_file)
        os.rmdir(self.test_dir)

    def test_add_and_check_name(self):
        name = "John Doe"
        self.assertFalse(self.file_manager.name_exists(name))
        self.file_manager.add_name(name)
        self.assertTrue(self.file_manager.name_exists(name))

    def test_multiple_names(self):
        names = ["Alice", "Bob", "Charlie"]
        for name in names:
            self.file_manager.add_name(name)

        for name in names:
            self.assertTrue(self.file_manager.name_exists(name))

        self.assertFalse(self.file_manager.name_exists("David"))

    def test_case_sensitivity(self):
        self.file_manager.add_name("John Doe")
        self.assertTrue(self.file_manager.name_exists("John Doe"))
        self.assertFalse(self.file_manager.name_exists("john doe"))

    def test_file_creation(self):
        self.file_manager.add_name("Test User")
        self.assertTrue(os.path.exists(self.file_manager.names_file))


if __name__ == "__main__":
    unittest.main()
