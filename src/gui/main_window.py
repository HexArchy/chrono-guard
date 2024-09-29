import sys
import time
from datetime import datetime
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QApplication,
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont, QIcon
from src.utils.config_manager import ConfigManager
from src.utils.file_manager import FileManager
from src.gui.styles import MAIN_STYLE


class ChronoGuardMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config_manager = ConfigManager()
        self.file_manager = FileManager()
        self.init_ui()
        self.load_config()
        self.start_timer()

    def init_ui(self):
        self.setStyleSheet(MAIN_STYLE)
        self.setWindowIcon(QIcon("resources/icons/chronoguard_icon.png"))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        title_label = QLabel("ChronoGuard", self)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        layout.addWidget(title_label)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Введите ФИО")
        layout.addWidget(self.name_input)

        self.submit_button = QPushButton("Отправить", self)
        self.submit_button.clicked.connect(self.submit_name)
        layout.addWidget(self.submit_button)

        self.info_label = QLabel(self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)

        self.setWindowTitle("ChronoGuard")
        self.setGeometry(300, 300, 400, 300)

    def load_config(self):
        self.config_manager.load_config()
        self.update_info_label()

    def submit_name(self):
        name = self.name_input.text()
        if not name:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите ФИО")
            return

        if self.file_manager.name_exists(name):
            QMessageBox.information(
                self, "Информация", "Такое ФИО уже существует в файле"
            )
            return

        self.file_manager.add_name(name)
        QMessageBox.information(self, "Успех", "ФИО успешно добавлено")
        self.name_input.clear()

    def check_time_limit(self):
        if self.config_manager.update_time():
            self.show_limit_reached()
        else:
            self.update_info_label()

    def update_info_label(self):
        remaining_starts, remaining_time = self.config_manager.get_remaining_usage()
        self.info_label.setText(
            f"Осталось запусков: {remaining_starts}\n"
            f"Осталось времени: {remaining_time} сек"
        )

    def show_limit_reached(self):
        reply = QMessageBox.question(
            self,
            "Лимит достигнут",
            "Вы достигли лимита использования. Хотите приобрести полную версию?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(
                self, "Покупка", "Спасибо за покупку полной версии!"
            )
            self.reset_limits()
        else:
            self.close()

    def reset_limits(self):
        self.config_manager.reset_limits()
        self.update_info_label()
        QMessageBox.information(
            self, "ChronoGuard", "Все лимиты использования сброшены."
        )

    def closeEvent(self, event):
        self.config_manager.save_config()
        event.accept()

    def start_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time_limit)
        self.timer.start(100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ChronoGuardMainWindow()
    main_window.show()
    sys.exit(app.exec())
