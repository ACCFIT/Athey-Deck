import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

class LicensePlateManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("License Plate Manager")
        self.setGeometry(100, 100, 600, 400)
        self.license_plates = []
        self.initUI()

    def initUI(self):
        # Load license plates from file
        self.load_license_plates()

        # Title label
        title_label = QLabel("License Plate Manager", self)
        title_label.setStyleSheet("font-size: 20px;")
        title_label.setAlignment(Qt.AlignCenter)

        # ID input
        self.id_entry = QLineEdit(self)
        self.id_entry.setPlaceholderText("Enter ID")

        id_label = QLabel("ID:", self)

        id_layout = QHBoxLayout()
        id_layout.addWidget(id_label)
        id_layout.addWidget(self.id_entry)

        # License Plate input
        self.plate_entry = QLineEdit(self)
        self.plate_entry.setPlaceholderText("Enter License Plate Pattern")

        plate_label = QLabel("License Plate Pattern:", self)

        plate_layout = QHBoxLayout()
        plate_layout.addWidget(plate_label)
        plate_layout.addWidget(self.plate_entry)

        # Severity input
        self.severity_entry = QLineEdit(self)
        self.severity_entry.setPlaceholderText("Enter Severity (Color Name)")

        severity_label = QLabel("Severity:", self)

        severity_layout = QHBoxLayout()
        severity_layout.addWidget(severity_label)
        severity_layout.addWidget(self.severity_entry)

        # Add Plate button
        self.add_button = QPushButton("Add Plate", self)
        self.add_button.clicked.connect(self.add_license_plate)

        # License Plate list
        self.plate_list = QListWidget(self)
        self.plate_list.setSelectionMode(QListWidget.SingleSelection)
        self.plate_list.itemClicked.connect(self.delete_license_plate)

        # Code display
        self.code_text_edit = QTextEdit(self)
        self.code_text_edit.setPlaceholderText("Generated Code")
        self.code_text_edit.setReadOnly(True)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addLayout(id_layout)
        main_layout.addLayout(plate_layout)
        main_layout.addLayout(severity_layout)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.plate_list)
        main_layout.addWidget(self.code_text_edit)

        self.setLayout(main_layout)

    def add_license_plate(self):
        plate_id = self.id_entry.text().strip()
        plate_pattern = self.plate_entry.text().strip()
        severity = self.severity_entry.text().strip()
        if plate_id and plate_pattern:
            try:
                # Compile the regex pattern
                re.compile(plate_pattern)
                # Append the license plate to the list
                self.license_plates.append((plate_id, plate_pattern, severity))
                # Update the code display
                self.update_code()
                # Clear the input fields
                self.id_entry.clear()
                self.plate_entry.clear()
                self.severity_entry.clear()
            except re.error as e:
                QMessageBox.warning(self, "Error", f"Invalid regular expression: {e}")
        else:
            QMessageBox.warning(self, "Error", "Please enter ID, license plate pattern, and severity")

    def update_code(self):
        code = "# Updated code with license plates\n\n"
        for plate_id, pattern, severity in self.license_plates:
            code += f"license_plates.append(('ID: {plate_id}', '{pattern}', '{severity}'))\n"
        self.code_text_edit.setPlainText(code)

    def delete_license_plate(self, item):
        index = self.plate_list.row(item)
        del self.license_plates[index]
        self.update_code()
        self.update_plate_list()

    def update_plate_list(self):
        self.plate_list.clear()
        for plate_id, pattern, severity in self.license_plates:
            item = QListWidgetItem(f"{plate_id} - {pattern} ({severity})")
            self.plate_list.addItem(item)

    def closeEvent(self, event):
        self.save_license_plates()
        event.accept()

    def save_license_plates(self):
        with open("license_plates.txt", "w") as file:
            for plate_id, pattern, severity in self.license_plates:
                file.write(f"{plate_id}, {pattern}, {severity}\n")

    def load_license_plates(self):
        try:
            with open("license_plates.txt", "r") as file:
                for line in file:
                    try:
                        plate_id, pattern, severity = line.strip().split(",", 2)
                        self.license_plates.append((plate_id.strip(), pattern.strip(), severity.strip()))
                    except ValueError:
                        print("Error parsing line:", line)
                        continue
            self.update_plate_list()  # Update plate list after loading
            self.update_code()  # Update code after loading
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LicensePlateManager()
    window.show()
    sys.exit(app.exec_())
