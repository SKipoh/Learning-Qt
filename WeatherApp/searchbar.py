from PyQt5 import QHBoxLayout, QLineEdit, QPushButton

# Creating a layout to hold the searchbar and search button
searchBarLayout = QHBoxLayout()
# Creating a search bar for the user to search for their city
searchBarLayout.addWidget(QLineEdit(placeholderText="Please Enter Your City..."))
searchBarLayout.addWidget(QPushButton("Search"))
