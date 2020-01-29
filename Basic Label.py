from PyQt5.QtWidgets import QApplication, QLabel

# Creating a QApplication called "app". THis is required and EVERY app
# must have EXACTLY one of these. the Sqaure brackets represent any command
# line arguments parsed to the application. This app doesn't use any and
# thus none are parsed
app = QApplication([])
# Creating a label widget that can contain text, and calling it "label"
label = QLabel("Hello World")
# Telling Qt to display this label on screen
label.show()

# Lastly, we hand control over to Qt and tell it to run the application until
# the user closes it
app.exec_()
