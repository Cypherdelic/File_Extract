import os
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets

class FileSearcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Searcher")

        # Create widgets
        folder_label = QtWidgets.QLabel("Folder to search:")
        self.folder_entry = QtWidgets.QLineEdit()
        folder_button = QtWidgets.QPushButton("Browse", clicked=self.select_folder)

        keyword_label = QtWidgets.QLabel("Keyword:")
        self.keyword_entry = QtWidgets.QLineEdit()

        output_label = QtWidgets.QLabel("Output folder:")
        self.output_entry = QtWidgets.QLineEdit()
        output_button = QtWidgets.QPushButton("Browse", clicked=self.select_output_folder)

        search_button = QtWidgets.QPushButton("Search", clicked=self.search_files)
        search_button.setStyleSheet("background-color: #6C63FF; color: #FFFFFF; padding: 8px; border-radius: 5px;")

        # Layout widgets
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(folder_label, 0, 0, QtCore.Qt.AlignLeft)
        layout.addWidget(self.folder_entry, 1, 0)
        layout.addWidget(folder_button, 1, 1)

        layout.addWidget(keyword_label, 2, 0, QtCore.Qt.AlignLeft)
        layout.addWidget(self.keyword_entry, 3, 0)

        layout.addWidget(output_label, 4, 0, QtCore.Qt.AlignLeft)
        layout.addWidget(self.output_entry, 5, 0)
        layout.addWidget(output_button, 5, 1)

        layout.addWidget(search_button, 6, 0, 1, 2, QtCore.Qt.AlignRight)

        # Set window size
        self.setGeometry(300, 300, 600, 200)

    def select_folder(self):
        """Open a file dialog to allow the user to select a folder."""
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.folder_entry.setText(folder_path)

    def select_output_folder(self):
        """Open a file dialog to allow the user to select an output folder."""
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.output_entry.setText(folder_path)

    def search_files(self):
        """Copy all files containing the keyword in the filename to the output folder."""
        folder_path = self.folder_entry.text()
        keyword = self.keyword_entry.text()
        output_folder = self.output_entry.text()
        if not folder_path or not keyword or not output_folder:
            QtWidgets.QMessageBox.critical(self, "Error", "Please fill in all fields.")
            return
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                if keyword.lower() in filename.lower():
                    shutil.copy(os.path.join(root, filename), output_folder)
        QtWidgets.QMessageBox.information(self, "Success", "Done!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = FileSearcher()
    window.show()
    app.exec_()
