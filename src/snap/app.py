"""
a snippet application
"""

import sys

from PySide6 import QtWidgets


class Snap(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("snap")
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Snap()
    sys.exit(app.exec())
