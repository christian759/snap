"""
a snippet application
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class Snap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("snap")
        self.show()


def main():
    app = QApplication(sys.argv)
    main_window = Snap()
    main_window.show()
    sys.exit(app.exec())
