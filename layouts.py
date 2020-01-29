from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# Creating a Qt QApplication called "app"
app = QApplication([])

# Creating a window to display our layout with. We use the most basic
# widget type called "QWidget" as it is literally only ot be used as a
# container for the layout
window = QWidget()
# Next, we create a Qt Layout using the "QVBoxLayout" widget. this will
# display any widgets in it vertically stacked
layout = QVBoxLayout()

# Creating and adding 3 push buttons to the veritcal layout "Top", "Middle"
# and "bottom". THese should appear in a stack of 3
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Middle'))
layout.addWidget(QPushButton('Bottom'))

# We set the "layout" parameter of our window to be our variable "layout"
window.setLayout(layout)
# We then show the window to the user
window.show()

app.exec_()
