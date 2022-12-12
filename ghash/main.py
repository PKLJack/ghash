import sys

from PySide6.QtWidgets import QApplication

from .mainwindow import MainWindow


def main():
    app = QApplication()

    window = MainWindow(app)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
