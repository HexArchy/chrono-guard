import sys
import os

# Добавляем корневую директорию проекта в sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from PyQt6.QtWidgets import QApplication
from src.gui.main_window import ChronoGuardMainWindow


def main():
    app = QApplication(sys.argv)
    ex = ChronoGuardMainWindow()

    # Backdoor: If launched with a specific argument, reset the usage limits
    if len(sys.argv) > 1 and sys.argv[1] == "reset_chrono_9876":
        ex.reset_limits()
        print("Limits have been reset.")
        sys.exit()

    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
