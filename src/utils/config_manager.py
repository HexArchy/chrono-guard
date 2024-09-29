import os
import json
import time
from src.utils.crypto import encrypt_data, decrypt_data


class ConfigManager:
    def __init__(self):
        self.config_path = os.path.expanduser(
            "~/Library/Application Support/ChronoGuard/config.dat"
        )
        self.usage_path = os.path.expanduser("~/.chronoguard_usage.dat")
        self.start_count = 0
        self.total_time = 0
        self.last_update_time = time.time()

    def load_config(self):
        self.load_usage_data()
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, "r") as f:
                    encrypted_content = f.read()
                decrypted_content = decrypt_data(encrypted_content)
                config = json.loads(decrypted_content)
                self.last_update_time = config.get("last_update_time", time.time())
            else:
                self.last_update_time = time.time()
            self.start_count += 1
            self.save_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            self.last_update_time = time.time()
        finally:
            self.save_usage_data()

    def save_config(self):
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        config = {"last_update_time": self.last_update_time}
        encrypted_data = encrypt_data(json.dumps(config))
        with open(self.config_path, "w") as f:
            f.write(encrypted_data)

    def load_usage_data(self):
        try:
            if os.path.exists(self.usage_path):
                with open(self.usage_path, "r") as f:
                    encrypted_content = f.read()
                decrypted_content = decrypt_data(encrypted_content)
                usage_data = json.loads(decrypted_content)
                self.start_count = usage_data.get("start_count", 0)
                self.total_time = usage_data.get("total_time", 0)
            else:
                self.start_count = 0
                self.total_time = 0
        except Exception as e:
            print(f"Error loading usage data: {e}")
            self.start_count = 0
            self.total_time = 0

    def save_usage_data(self):
        os.makedirs(os.path.dirname(self.usage_path), exist_ok=True)
        usage_data = {"start_count": self.start_count, "total_time": self.total_time}
        encrypted_data = encrypt_data(json.dumps(usage_data))
        with open(self.usage_path, "w") as f:
            f.write(encrypted_data)

    def update_time(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time
        self.total_time += elapsed_time
        self.last_update_time = current_time
        self.save_config()
        self.save_usage_data()
        return self.check_limits()

    def check_limits(self):
        return self.total_time >= 180 or self.start_count > 5

    def get_remaining_usage(self):
        remaining_starts = max(0, 5 - self.start_count)
        remaining_time = max(0, 180 - self.total_time)
        return remaining_starts, int(remaining_time)

    def reset_limits(self):
        self.start_count = 0
        self.total_time = 0
        self.last_update_time = time.time()
        self.save_config()
        self.save_usage_data()

    def get_total_time(self):
        return int(self.total_time)

    def get_start_count(self):
        return self.start_count
