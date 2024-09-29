import os
import shutil
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
from src.gui.styles import UNINSTALLER_STYLE


class Uninstaller(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet(UNINSTALLER_STYLE)
        layout = QVBoxLayout()

        self.info_label = QLabel("Деинсталлятор ChronoGuard", self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.uninstall_button = QPushButton("Удалить", self)
        self.uninstall_button.clicked.connect(self.uninstall)
        layout.addWidget(self.uninstall_button)

        self.setLayout(layout)
        self.setWindowTitle("Деинсталлятор ChronoGuard")
        self.setGeometry(300, 300, 400, 200)

    def uninstall(self):
        self.uninstall_button.setEnabled(False)
        self.progress_bar.setValue(0)

        QTimer.singleShot(100, self.perform_uninstallation)

    def perform_uninstallation(self):
        app_support_dir = os.path.expanduser(
            "~/Library/Application Support/ChronoGuard"
        )
        desktop_shortcut = os.path.expanduser("~/Desktop/ChronoGuard.command")

        try:
            if os.path.exists(app_support_dir):
                shutil.rmtree(app_support_dir)
            self.progress_bar.setValue(50)

            if os.path.exists(desktop_shortcut):
                os.remove(desktop_shortcut)
            self.progress_bar.setValue(100)

            QMessageBox.information(
                self, "Удаление завершено", "ChronoGuard успешно удален."
            )
        except Exception as e:
            QMessageBox.warning(
                self, "Ошибка", f"Произошла ошибка при удалении: {str(e)}"
            )

        self.close()


if __name__ == "__main__":
    app = QApplication([])
    uninstaller = Uninstaller()
    uninstaller.show()
    app.exec()
