import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class ColorSwapper(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout and widgets
        self.layout = QVBoxLayout()

        # Hex input
        self.hex_input = QLineEdit(self)
        self.hex_input.setPlaceholderText("Enter RGB Hex Code (e.g., #47FF00)")
        self.layout.addWidget(self.hex_input)

        # Original RGB label and color square
        self.rgb_label = QLabel("RGB Color:")
        self.rgb_color_square = QLabel()
        self.rgb_color_square.setFixedSize(100, 100)
        self.rgb_hex_label = QLabel()
        self.layout.addWidget(self.rgb_label)
        self.layout.addWidget(self.rgb_color_square)
        self.layout.addWidget(self.rgb_hex_label)

        # Converted BGR label and color square
        self.bgr_label = QLabel("BGR Color:")
        self.bgr_color_square = QLabel()
        self.bgr_color_square.setFixedSize(100, 100)
        self.bgr_hex_label = QLabel()
        self.layout.addWidget(self.bgr_label)
        self.layout.addWidget(self.bgr_color_square)
        self.layout.addWidget(self.bgr_hex_label)

        # Converted GBR label and color square
        self.gbr_label = QLabel("GBR Color:")
        self.gbr_color_square = QLabel()
        self.gbr_color_square.setFixedSize(100, 100)
        self.gbr_hex_label = QLabel()
        self.layout.addWidget(self.gbr_label)
        self.layout.addWidget(self.gbr_color_square)
        self.layout.addWidget(self.gbr_hex_label)

        # Converted GRB label and color square
        self.grb_label = QLabel("GRB Color:")
        self.grb_color_square = QLabel()
        self.grb_color_square.setFixedSize(100, 100)
        self.grb_hex_label = QLabel()
        self.layout.addWidget(self.grb_label)
        self.layout.addWidget(self.grb_color_square)
        self.layout.addWidget(self.grb_hex_label)

        # Converted RBG label and color square
        self.rbg_label = QLabel("RBG Color:")
        self.rbg_color_square = QLabel()
        self.rbg_color_square.setFixedSize(100, 100)
        self.rbg_hex_label = QLabel()
        self.layout.addWidget(self.rbg_label)
        self.layout.addWidget(self.rbg_color_square)
        self.layout.addWidget(self.rbg_hex_label)

        # Converted BRG label and color square
        self.brg_label = QLabel("BRG Color:")
        self.brg_color_square = QLabel()
        self.brg_color_square.setFixedSize(100, 100)
        self.brg_hex_label = QLabel()
        self.layout.addWidget(self.brg_label)
        self.layout.addWidget(self.brg_color_square)
        self.layout.addWidget(self.brg_hex_label)

        # Copy button
        self.copy_button = QPushButton("Copy to Clipboard", self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.layout.addWidget(self.copy_button)

        # Connect input to the update function
        self.hex_input.textChanged.connect(self.update_colors)

        # Set layout
        self.setLayout(self.layout)
        self.setWindowTitle("RGB to BGR, GBR, GRB, RBG, BRG Converter")

    def update_colors(self):
        hex_code = self.hex_input.text().strip()

        # Validate hex code
        if len(hex_code) == 7 and hex_code[0] == '#':
            try:
                # Remove the '#' if it exists
                if hex_code.startswith("#"):
                    hex_code = hex_code[1:]

                # Convert RGB hex to RGB values
                rgb = QColor(f"#{hex_code}").getRgb()
                r, g, b = rgb[0], rgb[1], rgb[2]

                # Convert to BGR
                bgr_hex = f"#{b:02X}{g:02X}{r:02X}"
                self.bgr_color_square.setStyleSheet(f"background-color: {bgr_hex};")
                self.bgr_hex_label.setText(f"BGR: {bgr_hex}")

                # Convert to GBR
                gbr_hex = f"#{g:02X}{b:02X}{r:02X}"
                self.gbr_color_square.setStyleSheet(f"background-color: {gbr_hex};")
                self.gbr_hex_label.setText(f"GBR: {gbr_hex}")

                # Convert to GRB
                grb_hex = f"#{g:02X}{r:02X}{b:02X}"
                self.grb_color_square.setStyleSheet(f"background-color: {grb_hex};")
                self.grb_hex_label.setText(f"GRB: {grb_hex}")

                # Convert to RBG
                rbg_hex = f"#{r:02X}{b:02X}{g:02X}"
                self.rbg_color_square.setStyleSheet(f"background-color: {rbg_hex};")
                self.rbg_hex_label.setText(f"RBG: {rbg_hex}")

                # Convert to BRG
                brg_hex = f"#{b:02X}{r:02X}{g:02X}"
                self.brg_color_square.setStyleSheet(f"background-color: {brg_hex};")
                self.brg_hex_label.setText(f"BRG: {brg_hex}")

                # Display original RGB
                rgb_hex = f"#{r:02X}{g:02X}{b:02X}"
                self.rgb_color_square.setStyleSheet(f"background-color: {rgb_hex};")
                self.rgb_hex_label.setText(f"RGB: {rgb_hex}")

            except ValueError:
                # Handle invalid hex code
                self.rgb_color_square.setStyleSheet("background-color: white;")
                self.rgb_hex_label.setText("RGB: Invalid")
                self.bgr_color_square.setStyleSheet("background-color: white;")
                self.bgr_hex_label.setText("BGR: Invalid")
                self.gbr_color_square.setStyleSheet("background-color: white;")
                self.gbr_hex_label.setText("GBR: Invalid")
                self.grb_color_square.setStyleSheet("background-color: white;")
                self.grb_hex_label.setText("GRB: Invalid")
                self.rbg_color_square.setStyleSheet("background-color: white;")
                self.rbg_hex_label.setText("RBG: Invalid")
                self.brg_color_square.setStyleSheet("background-color: white;")
                self.brg_hex_label.setText("BRG: Invalid")
        else:
            # Handle invalid hex code format
            self.rgb_color_square.setStyleSheet("background-color: white;")
            self.rgb_hex_label.setText("RGB: Invalid")
            self.bgr_color_square.setStyleSheet("background-color: white;")
            self.bgr_hex_label.setText("BGR: Invalid")
            self.gbr_color_square.setStyleSheet("background-color: white;")
            self.gbr_hex_label.setText("GBR: Invalid")
            self.grb_color_square.setStyleSheet("background-color: white;")
            self.grb_hex_label.setText("GRB: Invalid")
            self.rbg_color_square.setStyleSheet("background-color: white;")
            self.rbg_hex_label.setText("RBG: Invalid")
            self.brg_color_square.setStyleSheet("background-color: white;")
            self.brg_hex_label.setText("BRG: Invalid")

    def copy_to_clipboard(self):
        # Get text to copy
        text = (
            f"RGB: {self.rgb_hex_label.text()}\n"
            f"BGR: {self.bgr_hex_label.text()}\n"
            f"GBR: {self.gbr_hex_label.text()}\n"
            f"GRB: {self.grb_hex_label.text()}\n"
            f"RBG: {self.rbg_hex_label.text()}\n"
            f"BRG: {self.brg_hex_label.text()}"
        )

        # Copy text to clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorSwapper()
    window.show()
    sys.exit(app.exec_())
