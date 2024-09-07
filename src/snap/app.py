import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, \
    QLineEdit, QDialog
from snippet import Snippet



class Snap(QMainWindow):
    def __init__(self):
        super().__init__()

        # Central widget and layout
        self.snipNewInput = None
        self.newSnipDialog = None
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        #temporary name
        self.name: str = ""

        # Top horizontal layout for combo box and buttons
        self.TopHorizon = QWidget()
        self.TopHorizonLayout = QHBoxLayout()
        self.TopHorizon.setLayout(self.TopHorizonLayout)

        # Button to add snippet
        self.addItemButton = QPushButton("Add Snippet")
        self.addItemButton.clicked.connect(self.open_snippet_dialog)  # Pass method reference without parentheses

        # Combo box for selecting search method
        self.topCombo = QComboBox()
        self.topCombo.addItems(['Search by name', 'Search by category'])
        self.topCombo.currentTextChanged.connect(self.sort_method_change)

        # Add widgets to layout
        self.TopHorizonLayout.addWidget(self.addItemButton)
        self.TopHorizonLayout.addWidget(self.topCombo)

        # Set up the UI
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("snap")
        self.central_layout.addWidget(self.TopHorizon)
        self.show()

    @staticmethod
    def sort_method_change(s) -> str:
        print(s)
        return s

    def open_snippet_dialog(self):
        # Initialize the dialog only when needed
        self.newSnipDialog = QDialog(self)
        self.newSnipDialog.setWindowTitle("Create new Snippet")

        # Layout for the dialog
        newSnipDialogLayout = QVBoxLayout()
        self.snipNewInput = QLineEdit()  # Input field for snippet name

        # Connect text change to an update method
        self.snipNewInput.textChanged.connect(self.update_name)

        newSnipDialogLayout.addWidget(self.snipNewInput)

        # push buttons for ok and cancel
        dialogCancelButton = QPushButton("cancel")
        dialogCancelButton.clicked.connect(self.newSnipDialog.close)

        dialogOkButton = QPushButton("create")
        dialogOkButton.clicked.connect(self.create_snippet)

        dialogButtonLayout = QHBoxLayout()
        dialogButtonHost = QWidget()
        dialogButtonHost.setLayout(dialogButtonLayout)
        dialogButtonLayout.addWidget(dialogCancelButton)
        dialogButtonLayout.addWidget(dialogOkButton)

        newSnipDialogLayout.addWidget(dialogButtonHost)
        self.newSnipDialog.setLayout(newSnipDialogLayout)

        # Show the dialog
        self.newSnipDialog.exec()


    def create_snippet(self):
        # After closing the dialog, create the snippet
        new_snip = Snippet(name=self.name, category="string")
        self.newSnipDialog.close()
        print(new_snip)

    def update_name(self, text):
        self.name = text


# Main function
def main():
    app = QApplication(sys.argv)
    main_window = Snap()
    main_window.show()
    sys.exit(app.exec())

