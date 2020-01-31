from PyQt5 import QHBoxLayout, QLabel, QVBoxLayout


class forecast(QHBoxLayout):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent



class tile(QVBoxLayout):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.timeText = ""

        self.addwidget(QLabel())
