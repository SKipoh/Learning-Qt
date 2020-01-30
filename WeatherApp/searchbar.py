from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QMessageBox


class searchBar(QHBoxLayout):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.addWidget(QLineEdit(placeholderText="Please Enter A City..."))
        searchButton = QPushButton("Search")
        self.addWidget(searchButton)
        searchButton.clicked.connect(self.on_clicked)

    def on_clicked():
        alert = QMessageBox()
        alert.setText("Button Clicked")
        alert.exec_()
