import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_key():
    key_path = os.path.expanduser("~/.secrets/secret.txt")
    salt_path = os.path.expanduser("~/.secrets/salt.txt")

    if not os.path.exists(key_path):
        raise FileNotFoundError(
            "Secret key file not found. Please create ~/.secrets/secret.txt"
        )
    if not os.path.exists(salt_path):
        raise FileNotFoundError(
            "Salt file not found. Please create ~/.secrets/salt.txt"
        )

    with open(key_path, "rb") as key_file:
        key_data = key_file.read()

    with open(salt_path, "rb") as salt_file:
        salt = salt_file.read()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(key_data))
    return key


def encrypt_data(data):
    fernet = Fernet(get_key())
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(encrypted_data):
    fernet = Fernet(get_key())
    return fernet.decrypt(encrypted_data.encode()).decode()
