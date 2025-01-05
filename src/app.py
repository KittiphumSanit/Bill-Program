import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout


class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.label = QLabel("Hello, PyQt5!", self)
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Enter some text here")
        self.display_label = QLabel("", self)
        self.button = QPushButton("Update Label", self)

        # Connect button click to handler
        self.button.clicked.connect(self.on_button_click)

        # Arrange widgets using a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.display_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Window settings
        self.setWindowTitle("PyQt5 Example with Input")
        self.setGeometry(100, 100, 300, 200)

    def on_button_click(self):
        # Update display_label with the text from text_input
        input_text = self.text_input.text()
        self.display_label.setText(f"You entered: {input_text}")


# Main application logic
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SimpleApp()
    main_window.show()
    sys.exit(app.exec_())
