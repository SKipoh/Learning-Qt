from PyQt5 import QHBoxLayout, QLabel

class forecast(QHBoxLayout):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
