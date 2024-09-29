import unittest
import os
from src.utils.crypto import encrypt_data, decrypt_data, get_key


class TestCrypto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create temporary secret and salt files for testing
        cls.secret_path = "test_secret.txt"
        cls.salt_path = "test_salt.txt"

        with open(cls.secret_path, "w") as f:
            f.write("test_secret_key")

        with open(cls.salt_path, "w") as f:
            f.write("test_salt_value")

        # Temporarily replace the paths in the crypto module
        cls.original_secret_path = os.environ.get("CHRONOGUARD_SECRET_PATH")
        cls.original_salt_path = os.environ.get("CHRONOGUARD_SALT_PATH")
        os.environ["CHRONOGUARD_SECRET_PATH"] = cls.secret_path
        os.environ["CHRONOGUARD_SALT_PATH"] = cls.salt_path

    @classmethod
    def tearDownClass(cls):
        # Remove temporary files and restore original paths
        os.remove(cls.secret_path)
        os.remove(cls.salt_path)

        if cls.original_secret_path:
            os.environ["CHRONOGUARD_SECRET_PATH"] = cls.original_secret_path
        else:
            del os.environ["CHRONOGUARD_SECRET_PATH"]

        if cls.original_salt_path:
            os.environ["CHRONOGUARD_SALT_PATH"] = cls.original_salt_path
        else:
            del os.environ["CHRONOGUARD_SALT_PATH"]

    def test_encrypt_decrypt(self):
        original_data = "This is a test string"
        encrypted = encrypt_data(original_data)
        decrypted = decrypt_data(encrypted)
        self.assertEqual(original_data, decrypted)

    def test_different_encryptions(self):
        data1 = "First string"
        data2 = "Second string"
        encrypted1 = encrypt_data(data1)
        encrypted2 = encrypt_data(data2)
        self.assertNotEqual(encrypted1, encrypted2)

    def test_key_generation(self):
        key1 = get_key()
        key2 = get_key()
        self.assertEqual(
            key1, key2
        )  # Keys should be the same for the same secret and salt


if __name__ == "__main__":
    unittest.main()
