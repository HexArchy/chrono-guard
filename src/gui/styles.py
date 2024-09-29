MAIN_STYLE = """
    QMainWindow {
        background-color: #2C3E50;
    }
    QLabel {
        color: #ECF0F1;
        font-size: 14px;
    }
    QLineEdit {
        background-color: #34495E;
        color: #ECF0F1;
        border: 1px solid #7F8C8D;
        padding: 5px;
        border-radius: 3px;
    }
    QPushButton {
        background-color: #3498DB;
        color: #ECF0F1;
        border: none;
        padding: 8px 16px;
        border-radius: 3px;
    }
    QPushButton:hover {
        background-color: #2980B9;
    }
"""

INSTALLER_STYLE = """
    QWidget {
        background-color: #2C3E50;
        color: #ECF0F1;
    }
    QLabel {
        font-size: 14px;
    }
    QPushButton {
        background-color: #3498DB;
        color: #ECF0F1;
        border: none;
        padding: 8px 16px;
        border-radius: 3px;
    }
    QPushButton:hover {
        background-color: #2980B9;
    }
    QProgressBar {
        border: 2px solid #3498DB;
        border-radius: 5px;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: #3498DB;
    }
"""

UNINSTALLER_STYLE = """
    QWidget {
        background-color: #2C3E50;
        color: #ECF0F1;
    }
    QLabel {
        font-size: 14px;
    }
    QPushButton {
        background-color: #E74C3C;
        color: #ECF0F1;
        border: none;
        padding: 8px 16px;
        border-radius: 3px;
    }
    QPushButton:hover {
        background-color: #C0392B;
    }
    QProgressBar {
        border: 2px solid #E74C3C;
        border-radius: 5px;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: #E74C3C;
    }
"""
