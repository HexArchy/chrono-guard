import sys
import os

# Получаем абсолютный путь к корневой директории проекта
project_root = os.path.abspath(os.path.dirname(__file__))

# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, project_root)

from src.installer.installer import Installer
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    installer = Installer()
    installer.show()
    sys.exit(app.exec())
