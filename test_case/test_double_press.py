
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QShortcut
from PyQt5.QtGui import QKeySequence, QKeyEvent
from PyQt5.QtCore import QTimer, QDateTime, Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.shortcut = QShortcut(QKeySequence(Qt.Key_Return), self)
        self.shortcut.activated.connect(self.handle_double_return)

        self.last_timestamp = QDateTime.currentDateTime()

    def handle_double_return(self):
        current_timestamp = QDateTime.currentDateTime()
        elapsed_milliseconds = self.last_timestamp.msecsTo(current_timestamp)

        if elapsed_milliseconds <= 500:
            print("Handle double Return!")
        else:
            print("Handle single Return!")
            
        self.last_timestamp = current_timestamp


if __name__ == "__main__":
    app = QApplication([])
    w = MyWidget()
    w.show()
    app.exec_()