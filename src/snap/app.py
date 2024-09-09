import sys
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QLineEdit, QDialog, QScrollArea, QLabel
from snippet import Snippet

# Main Application Window
class Snap(QMainWindow):
    def __init__(self):
        super().__init__()

        # QSettings setup
        self.settings = QSettings("MyCompany", "SnapApp")

        # List to store snippets
        self.listOfSnippet: list[Snippet] = self.load_snippets()

        # Initialize some components that will be used later
        self.snipCateInput = None
        self.snipNameInput = None
        self.newSnipDialog = None
        self.snippetButtons = None
        self.newSnippetButtons = None
        self.displayedContent = None

        # Central widget and layout
        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        # Right and left layout and widget
        self.rightWidget = QWidget()
        self.rightLayout = QVBoxLayout()
        self.rightWidget.setLayout(self.rightLayout)
        self.contentLabel = QLabel("Snippet content: ")
        self.rightLayout.addWidget(self.contentLabel)

        self.leftWidget = QWidget()
        self.leftLayout = QVBoxLayout()
        self.leftWidget.setLayout(self.leftLayout)

        # Temporary name for new snippets
        self.name: str = ""
        self.category: str = ""

        # Scroll Area for all snippets
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaLayout = QVBoxLayout()
        self.scrollAreaWidget.setLayout(self.scrollAreaLayout)
        self.scrollArea.setWidget(self.scrollAreaWidget)

        # Top horizontal layout for combo box and buttons
        self.TopHorizon = QWidget()
        self.TopHorizonLayout = QHBoxLayout()
        self.TopHorizon.setLayout(self.TopHorizonLayout)

        # Button to add snippet
        self.addItemButton = QPushButton("Add Snippet")
        self.addItemButton.clicked.connect(self.open_snippet_dialog)

        # Input field for searching for snippets
        self.searchInput = QLineEdit()
        self.searchInput.textChanged.connect(self.search_snippets)

        # Add widgets to layout
        self.TopHorizonLayout.addWidget(self.searchInput)
        self.TopHorizonLayout.addWidget(self.addItemButton)

        # Set up the UI
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Snap")
        self.leftLayout.addWidget(self.TopHorizon)
        self.leftLayout.addWidget(self.scrollArea)
        self.central_layout.addWidget(self.leftWidget)
        self.central_layout.addWidget(self.rightWidget)

        # Dynamically load saved snippets into the UI
        for snippet in self.listOfSnippet:
            button = QPushButton(f"{snippet.name}")
            button.setObjectName(snippet.name)
            button.clicked.connect(lambda checked, btn_name=snippet.name: self.display_content(btn_name))
            self.scrollAreaLayout.addWidget(button)

        self.show()

    def delete_snippet(self):
        """Delete a snippet from the list and update the UI"""
        sender = self.sender()
        snippet_name = sender.text()
        for snippet in self.listOfSnippet:
            if snippet.name == snippet_name:
                self.listOfSnippet.remove(snippet)
                break
        sender.deleteLater()
        self.save_snippets()

    def load_snippets(self):
        """Load the saved snippets from QSettings"""
        snippets_data = self.settings.value("snippets", [])
        return [Snippet.from_dict(data) for data in snippets_data]

    def save_snippets(self):
        """Save the current listOfSnippet to QSettings"""
        snippets_data = [snippet.to_dict() for snippet in self.listOfSnippet]
        self.settings.setValue("snippets", snippets_data)

    def create_snippet(self):
        """Create a new snippet, add to the list, and update the UI"""
        new_snip = Snippet(name=self.name, category=self.category)
        self.listOfSnippet.append(new_snip)
        button = QPushButton(f"{new_snip.name}")
        button.setObjectName(new_snip.name)
        button.clicked.connect(lambda checked, btn_name=new_snip.name: self.display_content(btn_name))
        self.scrollAreaLayout.addWidget(button)
        self.name = ""
        self.category = ""
        self.newSnipDialog.close()

        # Save the updated list of snippets
        self.save_snippets()

    def display_content(self, button_name):
        for snippet in self.listOfSnippet:
            if snippet.name == button_name:
                self.contentLabel.setText(f"Snippet content: {snippet.category}")
                self.displayedContent = snippet.category
                break

    def update_name(self, text):
        """Update snippet name from input"""
        self.name = text

    def update_category(self, text):
        """Update snippet category from input"""
        self.category = text

    def open_snippet_dialog(self):
        """Open a dialog to create a new snippet"""
        self.newSnipDialog = QDialog(self)
        self.newSnipDialog.setWindowTitle("Create new Snippet")

        # Layout for the dialog
        newSnipDialogLayout = QVBoxLayout()

        # Input field for snippet name
        self.snipNameInput = QLineEdit()
        self.snipNameInput.setPlaceholderText("Enter snippet name")

        # Input field for snippet category
        self.snipCateInput = QLineEdit()
        self.snipCateInput.setPlaceholderText("Enter snippet category")

        # Connect text change to update_name and update_category methods
        self.snipNameInput.textChanged.connect(self.update_name)
        self.snipCateInput.textChanged.connect(self.update_category)

        newSnipDialogLayout.addWidget(self.snipNameInput)
        newSnipDialogLayout.addWidget(self.snipCateInput)

        # Push buttons for cancel and create
        dialogOkButton = QPushButton("Create")
        dialogOkButton.clicked.connect(self.create_snippet)

        dialogCancelButton = QPushButton("Cancel")
        dialogCancelButton.clicked.connect(self.newSnipDialog.close)

        dialogButtonLayout = QHBoxLayout()
        dialogButtonHost = QWidget()
        dialogButtonHost.setLayout(dialogButtonLayout)
        dialogButtonLayout.addWidget(dialogCancelButton)
        dialogButtonLayout.addWidget(dialogOkButton)

        newSnipDialogLayout.addWidget(dialogButtonHost)
        self.newSnipDialog.setLayout(newSnipDialogLayout)

        # Show the dialog
        self.newSnipDialog.exec()

    def search_snippets(self, text):
        """Handle changes in the search input"""
        # Loop through the list of widgets (buttons)
        for widget in self.scrollAreaWidget.children():
            # Check if it's a QPushButton
            if isinstance(widget, QPushButton):
                # Check if the search text is not in the button's name (case-insensitive)
                if text.lower().strip() not in widget.objectName().lower():
                    # Hide the widget from the layout
                    widget.hide()
                else:
                    # Display the widget from the layout
                    widget.show()


# Main function
def main():
    app = QApplication(sys.argv)
    main_window = Snap()
    main_window.show()
    sys.exit(app.exec())

