from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Right-click menu')

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        action = QAction("Action", self)
        menu.addAction(action)
        menu.exec_(self.mapToGlobal(event.pos()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())