import sys
import os

# Получаем абсолютный путь к корневой директории проекта
project_root = os.path.abspath(os.path.dirname(__file__))

# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, project_root)

from src.installer.uninstaller import Uninstaller
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    uninstaller = Uninstaller()
    uninstaller.show()
    sys.exit(app.exec())
