"""
a snippet application
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox


class Snap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        self.TopHorizon = QWidget()
        self.TopHorizonLayout = QHBoxLayout()
        self.TopHorizon.setLayout(self.TopHorizonLayout)
        self.topCombo = QComboBox()
        self.topCombo.addItems(['Search by name','Search by category'])
        self.topCombo.currentTextChanged.connect(self.sort_method_change)
        self.TopHorizonLayout.addWidget(self.topCombo)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("snap")
        self.central_layout.addWidget(self.TopHorizon)
        self.show()

    def sort_method_change(self, s):
        print(s)


def main():
    app = QApplication(sys.argv)
    main_window = Snap()
    main_window.show()
    sys.exit(app.exec())
