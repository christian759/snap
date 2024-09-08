import sys

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, \
    QLineEdit, QDialog, QScrollArea
from snippet import Snippet

# Main Application Window
class Snap(QMainWindow):
    def __init__(self):
        super().__init__()

        # QSettings setup
        self.settings = QSettings("MyCompany", "SnapApp")

        # List to store snippets
        self.listOfSnippet: list[Snippet] = self.load_snippets()
        self.snipNewInput = None
        self.newSnipDialog = None

        # Central widget and layout
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        # Temporary name for new snippets
        self.name: str = ""

        # Scroll Area for all snippets
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaLayout = QVBoxLayout(self.scrollAreaWidget)
        self.scrollAreaWidget.setLayout(self.scrollAreaLayout)
        self.scrollArea.setWidget(self.scrollAreaWidget)

        # Top horizontal layout for combo box and buttons
        self.TopHorizon = QWidget()
        self.TopHorizonLayout = QHBoxLayout()
        self.TopHorizon.setLayout(self.TopHorizonLayout)

        # Button to add snippet
        self.addItemButton = QPushButton("Add Snippet")
        self.addItemButton.clicked.connect(self.open_snippet_dialog)

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
        self.central_layout.addWidget(self.scrollArea)

        # Dynamically load saved snippets into the UI
        for snippet in self.listOfSnippet:
            self.scrollAreaLayout.addWidget(QPushButton(f"{snippet.name}"))

        self.show()

    def load_snippets(self):
        """Load the saved snippets from QSettings"""
        snippets_data = self.settings.value("snippets", [])
        print(type(snippets_data))
        return [Snippet.from_dict(data) for data in snippets_data]

    def save_snippets(self):
        """Save the current listOfSnippet to QSettings"""
        snippets_data = [snippet.to_dict() for snippet in self.listOfSnippet]
        self.settings.setValue("snippets", snippets_data)

    def create_snippet(self):
        """Create a new snippet, add to the list, and update the UI"""
        new_snip = Snippet(name=self.name, category="string")
        self.listOfSnippet.append(new_snip)
        self.scrollAreaLayout.addWidget(QPushButton(f"{new_snip.name}"))
        self.newSnipDialog.close()

        # Save the updated list of snippets
        self.save_snippets()

    def update_name(self, text):
        """Update snippet name from input"""
        self.name = text

    def open_snippet_dialog(self):
        """Open a dialog to create a new snippet"""
        self.newSnipDialog = QDialog(self)
        self.newSnipDialog.setWindowTitle("Create new Snippet")

        # Layout for the dialog
        newSnipDialogLayout = QVBoxLayout()
        self.snipNewInput = QLineEdit()  # Input field for snippet name

        # Connect text change to update_name method
        self.snipNewInput.textChanged.connect(self.update_name)

        newSnipDialogLayout.addWidget(self.snipNewInput)

        # Push buttons for cancel and create
        dialogCancelButton = QPushButton("Cancel")
        dialogCancelButton.clicked.connect(self.newSnipDialog.close)

        dialogOkButton = QPushButton("Create")
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

    @staticmethod
    def sort_method_change(s):
        """Handle changes in the sorting method"""
        print(s)
        return s


# Main function
def main():
    app = QApplication(sys.argv)
    main_window = Snap()
    main_window.show()
    sys.exit(app.exec())

