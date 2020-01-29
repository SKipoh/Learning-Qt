from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox

# Creating the Qt application "app"
app = QApplication([])

# Creating a push button called "button" and giving it the text value
# of "click me"
button = QPushButton("click me")


# Creating a function that will be called when our push button is pressed.
# This will create an a QMessageBox called "alert" and set the text value
# of it too "Button has been clicked". we then finally hand control of it
# to Qt
def on_button_clicked():
    alert = QMessageBox()
    alert.setText("Button has been clicked")
    alert.exec_()

# We now attach this function to the "button.clicked" signal using
# "button.clciked.connect". This will tell Qt that whenever the ".clicked"
# signal occurs, we run our function to display a message
button.clicked.connect(on_button_clicked)
button.show()

app.exec_()
