import os
import shutil
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QMessageBox,
    QProgressBar,
)
from PyQt6.QtCore import Qt, QTimer
from src.gui.styles import INSTALLER_STYLE


class Installer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet(INSTALLER_STYLE)
        layout = QVBoxLayout()

        self.info_label = QLabel("Установщик ChronoGuard", self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.install_button = QPushButton("Установить", self)
        self.install_button.clicked.connect(self.install)
        layout.addWidget(self.install_button)

        self.setLayout(layout)
        self.setWindowTitle("Установщик ChronoGuard")
        self.setGeometry(300, 300, 400, 200)

    def install(self):
        self.install_button.setEnabled(False)
        self.progress_bar.setValue(0)

        QTimer.singleShot(100, self.perform_installation)

    def perform_installation(self):
        app_support_dir = os.path.expanduser(
            "~/Library/Application Support/ChronoGuard"
        )
        os.makedirs(app_support_dir, exist_ok=True)

        # Получаем абсолютный путь к директории src
        src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # Копируем всю директорию src в директорию поддержки приложения
        shutil.copytree(
            src_dir, os.path.join(app_support_dir, "src"), dirs_exist_ok=True
        )
        self.progress_bar.setValue(50)

        # Создаем простой скрипт запуска
        with open(os.path.expanduser("~/Desktop/ChronoGuard.command"), "w") as f:
            f.write("#!/bin/bash\n")
            f.write(f'cd "{app_support_dir}"\n')
            f.write("python3 -m src.main\n")
        os.chmod(os.path.expanduser("~/Desktop/ChronoGuard.command"), 0o755)
        self.progress_bar.setValue(100)

        QMessageBox.information(
            self,
            "Установка завершена",
            "ChronoGuard успешно установлен. Ярлык создан на рабочем столе.",
        )
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    installer = Installer()
    installer.show()
    sys.exit(app.exec())
