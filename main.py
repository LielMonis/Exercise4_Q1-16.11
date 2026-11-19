import os
import sys
import subprocess
import platform
from About import About_window

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QSpinBox,
    QLabel,
    QFileDialog,
    QMessageBox,
)

class GradesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grades Manager")
        self.resize(600, 700)

        #Buttons
        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_file)

        self.update_button = QPushButton("Update File")
        self.update_button.clicked.connect(self.update_file)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.show_about)

        #Bonus input
        self.bonus_label = QLabel("Bonus points (press ENTER):")
        self.bonus_input = QSpinBox()
        self.bonus_input.setRange(0, 100)
        # returnPressed fires only when the user presses ENTER
        self.bonus_input.lineEdit().returnPressed.connect(self.add_bonus)

        #Table
        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(["ID", "Original Grades", "Corrected Grades"])
        self.table.horizontalHeader().setStretchLastSection(True)

        #Layouts
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.load_button)
        top_layout.addWidget(self.update_button)
        top_layout.addWidget(self.about_button)

        bonus_layout = QHBoxLayout()
        bonus_layout.addWidget(self.bonus_label)
        bonus_layout.addWidget(self.bonus_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bonus_layout)
        main_layout.addWidget(self.table)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        #About section
        self.About = About_window()

        #the lists that i need to open
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Choose a CSV file", "", "CSV Files (*.csv)"
        )
        if not file_name:
            return  # User pressed Cancel
        self.selected_file = file_name

        # MY CODE HERE

    def update_table(self):
        self.table.clearContents()
        for row in range(len(self.student_ids)):
            self.table.setItem(row, 0, QTableWidgetItem(str(self.student_ids[row])))
            if row < len(self.original_grades):
                self.table.setItem(row, 1, QTableWidgetItem(str(self.original_grades[row])))
            if row < len(self.corrected_grades):
                self.table.setItem(row, 2, QTableWidgetItem(str(self.corrected_grades[row])))

    def add_bonus(self):
        # MY CODE HERE
        pass

    def update_file(self):
        # MY CODE HERE
        pass

    def open_file(self, path):
        """Open a file in its default app (e.g. Excel for CSV files)."""
        system = platform.system()
        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", path])
        else:  # Linux
            subprocess.run(["xdg-open", path])

    def show_about(self):
        self.About.show()

def load_style(app):
    style_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.qss")
    if os.path.exists(style_path):
        with open(style_path, "r") as f:
            app.setStyleSheet(f.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_style(app)
    window = GradesWindow()
    window.show()
    sys.exit(app.exec())