from PyQt5.QtWidgets import *
from searchbar import searchBar


class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.title = "Weather App"
        self.setWindowTitle(self.title)
        self.initUi()

    def initUi(self):
        main_layout = QVBoxLayout()

        self.searchbar_layer = searchBar(self)
        main_layout.addLayout(self.searchbar_layer)


if __name__ == "__main__":
    app = QApplication([])
    window = mainWindow()
    window.show()
    app.exec_()
