import unittest
import os
import json
import time
from src.utils.config_manager import ConfigManager
from src.utils.crypto import encrypt_data, decrypt_data


class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_data")
        os.makedirs(self.test_dir, exist_ok=True)
        self.config_manager = ConfigManager()
        self.config_manager.config_path = os.path.join(self.test_dir, "test_config.dat")
        self.config_manager.usage_path = os.path.join(self.test_dir, "test_usage.dat")

    def tearDown(self):
        if os.path.exists(self.config_manager.config_path):
            os.remove(self.config_manager.config_path)
        if os.path.exists(self.config_manager.usage_path):
            os.remove(self.config_manager.usage_path)
        os.rmdir(self.test_dir)

    def test_load_and_save_config(self):
        # Set initial values
        self.config_manager.start_count = 3
        self.config_manager.total_time = 100
        self.config_manager.last_update_time = time.time()

        # Save config
        self.config_manager.save_config()
        self.config_manager.save_usage_data()

        # Create a new instance and load config
        new_config_manager = ConfigManager()
        new_config_manager.config_path = self.config_manager.config_path
        new_config_manager.usage_path = self.config_manager.usage_path
        new_config_manager.load_config()

        # Check if values are loaded correctly
        self.assertEqual(
            new_config_manager.start_count, 4
        )  # 3 + 1 because load_config increments start_count
        self.assertEqual(new_config_manager.total_time, 100)

    def test_update_time(self):
        self.config_manager.total_time = 100
        self.config_manager.last_update_time = time.time() - 10  # 10 seconds ago

        self.config_manager.update_time()

        self.assertGreater(self.config_manager.total_time, 100)
        self.assertLess(
            self.config_manager.total_time, 111
        )  # Allow for small discrepancies

    def test_check_limits(self):
        self.config_manager.start_count = 5
        self.config_manager.total_time = 179
        self.assertFalse(self.config_manager.check_limits())

        self.config_manager.start_count = 6
        self.assertTrue(self.config_manager.check_limits())

        self.config_manager.start_count = 5
        self.config_manager.total_time = 180
        self.assertTrue(self.config_manager.check_limits())

    def test_get_remaining_usage(self):
        self.config_manager.start_count = 3
        self.config_manager.total_time = 100
        remaining_starts, remaining_time = self.config_manager.get_remaining_usage()
        self.assertEqual(remaining_starts, 2)
        self.assertEqual(remaining_time, 80)

    def test_reset_limits(self):
        self.config_manager.start_count = 3
        self.config_manager.total_time = 100
        self.config_manager.reset_limits()
        self.assertEqual(self.config_manager.start_count, 0)
        self.assertEqual(self.config_manager.total_time, 0)


if __name__ == "__main__":
    unittest.main()
