from PyQt5.QtWidgets import *

# Creating the QApplication called "app"
app = QApplication([])
# Creating a window to display our current and forecast weather
window = QWidget()

# Creating a layout to hold the searchbar and search button
searchBarLayout = QHBoxLayout()
# Creating a search bar for the user to search for their city
searchBarLayout.addWidget(QLineEdit(placeholderText="Please Enter Your City..."))
searchBarLayout.addWidget(QPushButton("Search"))

# Creating the mainLyout as a Vertical layout
mainLayout = QVBoxLayout()
mainLayout.addLayout(searchBarLayout)

# Setting our window's main layout to be "mainLayout". This contains all our
# sub-layers that hold the searchbar, forecast and the detailed information
# of the day's forecast
window.setLayout(mainLayout)

window.show()

app.exec_()
