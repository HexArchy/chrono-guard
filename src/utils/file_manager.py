import os
from PyQt6.QtCore import QCryptographicHash


class FileManager:
    def __init__(self):
        self.names_file = os.path.expanduser(
            "~/Library/Application Support/ChronoGuard/names.dat"
        )

    def name_exists(self, name):
        name_hash = self._hash_name(name)
        if os.path.exists(self.names_file):
            with open(self.names_file, "r") as f:
                return name_hash in f.read()
        return False

    def add_name(self, name):
        name_hash = self._hash_name(name)
        os.makedirs(os.path.dirname(self.names_file), exist_ok=True)
        with open(self.names_file, "a") as f:
            f.write(name_hash + "\n")

    def _hash_name(self, name):
        hash_object = QCryptographicHash(QCryptographicHash.Algorithm.Sha256)
        hash_object.addData(name.encode())
        return hash_object.result().toHex().data().decode()
