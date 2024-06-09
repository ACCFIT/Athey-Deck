import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import re

class LicensePlateManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LPM")
        self.setWindowIcon(QIcon("img/Logo.png"))
        self.setGeometry(100, 100, 600, 600)
        self.license_plates = []
        self.load_license_plates()
        self.initUI()

    def initUI(self):
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
        self.severity_entry.setPlaceholderText("Enter Severity")

        severity_label = QLabel("Severity (Yellow, Orange, or Red):", self)

        severity_layout = QHBoxLayout()
        severity_layout.addWidget(severity_label)
        severity_layout.addWidget(self.severity_entry)

        # Add Plate button
        self.add_button = QPushButton("Add Plate", self)
        self.add_button.clicked.connect(self.add_license_plate)

        # Delete Plate button
        self.delete_button = QPushButton("Delete Plate", self)
        self.delete_button.clicked.connect(self.delete_selected_license_plate)

        # License Plate list
        self.plate_list = QListWidget(self)
        self.plate_list.setSelectionMode(QListWidget.SingleSelection)

        # Code display
        #self.code_text = QTextEdit(self)
        #self.code_text.setPlaceholderText("Generated Code")
        #self.code_text.setReadOnly(True)

        # Apply, Cancel, and OK buttons
        self.apply_button = QPushButton("Apply", self)
        self.apply_button.clicked.connect(self.apply_changes)
        self.apply_button.setEnabled(False)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.cancel_changes)
        self.cancel_button.setEnabled(False)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.ok_and_close)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.apply_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.ok_button)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addLayout(id_layout)
        main_layout.addLayout(plate_layout)
        main_layout.addLayout(severity_layout)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.delete_button)
        main_layout.addWidget(self.plate_list)
        #main_layout.addWidget(self.code_text)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        self.update_plate_list()
        self.update_code()

    def add_license_plate(self):
        plate_id = self.id_entry.text().strip()
        plate_pattern = self.plate_entry.text().strip()
        severity = self.severity_entry.text().strip()
        if plate_id and plate_pattern:
            try:
                re.compile(plate_pattern)  # Compile the regex pattern
                plate_pattern = plate_pattern.upper()
                severity = severity.upper()
                self.license_plates.append((plate_id,r'\b' + plate_pattern + r'\b',severity))
                self.update_code()
                self.update_plate_list()
                self.apply_button.setEnabled(True)
                self.cancel_button.setEnabled(True)
            except re.error as e:
                QMessageBox.warning(self, "Error", f"Invalid regular expression: {e}")
        else:
            QMessageBox.warning(self, "Error", "Please enter both ID and regular expression")

    def update_code(self):
        code = "# Updated code with license plates\n\n"
        for plate_id, pattern, severity in self.license_plates:
            code += f"'ID: {plate_id}', '{pattern}', '{severity}'\n"
        #self.code_text.setPlainText(code)

    def delete_selected_license_plate(self):
        selected_item = self.plate_list.currentItem()
        if selected_item:
            index = self.plate_list.row(selected_item)
            del self.license_plates[index]
            self.update_code()
            self.update_plate_list()
            self.apply_button.setEnabled(True)
            self.cancel_button.setEnabled(True)

    def update_plate_list(self):
        self.plate_list.clear()
        for plate_id, pattern, severity in self.license_plates:
            pattern = pattern[2:-2]
            plate_str = f"{plate_id} - {pattern} ({severity})"
            item = QListWidgetItem(plate_str)
            self.plate_list.addItem(item)

    def apply_changes(self):
        self.save_license_plates()
        QMessageBox.information(self, "Info", "Changes applied successfully")
        self.apply_button.setEnabled(False)
        self.cancel_button.setEnabled(False)
        self.original_license_plates = self.license_plates.copy()

    def cancel_changes(self):
        self.license_plates = self.original_license_plates.copy()
        self.update_plate_list()
        self.update_code()
        self.apply_button.setEnabled(False)
        self.cancel_button.setEnabled(False)

    def ok_and_close(self):
        self.save_license_plates()
        self.close()
    
    def closeEvent(self, event):
        #self.save_license_plates()
        event.accept()

    def save_license_plates(self):
        with open("license_plates.txt", "w") as file:
            for plate_id, pattern, severity in self.license_plates:
                file.write(f"{plate_id},{pattern},{severity}\n")

    def load_license_plates(self):
        self.license_plates.clear()
        try:
            with open("license_plates.txt", "r") as file:
                for line in file:
                    plate_id, plate_pattern, severity = line.strip().split(",", 2)
                    self.license_plates.append((plate_id.strip(), plate_pattern.strip(), severity.strip()))
            self.original_license_plates = self.license_plates.copy()
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LicensePlateManager()
    window.show()
    sys.exit(app.exec_())
