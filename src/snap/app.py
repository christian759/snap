"""
author = CEO1
project name = "snap"
author_email = "christian4onos@gmail.com"
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, \
    QLineEdit, QDialog
from snippet import Snippet

name: str = " "

class Snap(QMainWindow):
    def __init__(self):
        """
        Initialize the main window with a central widget, top horizontal layout, and a combo box.

        The central widget is a QVBoxLayout containing the top horizontal layout. The top horizontal layout
        contains a QComboBox for selecting the sorting method. The combo box is populated with two options:
        'Search by name' and 'Search by category'. The current text change of the combo box triggers the
        'sort_method_change' method.

        Parameters:
        None

        Returns:
        None
        """
        super().__init__()
        # central widget
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        # top horizontal layout for combo box and other widgets
        self.TopHorizon = QWidget()
        self.TopHorizonLayout = QHBoxLayout()
        self.TopHorizon.setLayout(self.TopHorizonLayout)
        self.addItemButton = QPushButton("Add Snippet")
        self.addItemButton.clicked.connect(self.open_snippet_dialog())
        self.newSnipDialog = QDialog()
        self.newSnipDialog.setWindowTitle("Create new Snippet")
        self.snipNewInput = QLineEdit()
        self.topCombo = QComboBox()
        self.topCombo.addItems(['Search by name', 'Search by category'])
        self.topCombo.currentTextChanged.connect(self.sort_method_change)
        self.TopHorizonLayout.addWidget(self.addItemButton)
        self.TopHorizonLayout.addWidget(self.topCombo)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("snap")
        self.central_layout.addWidget(self.TopHorizon)
        self.show()

    # checking the category
    @staticmethod
    def sort_method_change(s) -> str:
        print(s)
        return s

    def init_snippets(self):
        newSnipDialogLayout = QVBoxLayout()
        self.newSnipDialog.setLayout(newSnipDialogLayout)
        newSnipDialogLayout.addWidget(self.snipNewInput)
        self.snipNewInput.textChanged.connect(name)
        new_snip = Snippet(name=name, category="string")
        print(new_snip)

    def open_snippet_dialog(self):
        self.newSnipDialog.exec()
        self.init_snippets()


#main function
def main():
    app = QApplication(sys.argv)
    main_window = Snap()
    main_window.show()
    sys.exit(app.exec())
