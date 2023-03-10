import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabWidget = QTabWidget(self)
        self.setCentralWidget(self.tabWidget)

        newTabButton = QPushButton("New Tab", self)
        newTabButton.clicked.connect(self.addNewTab)
        self.tabWidget.setCornerWidget(newTabButton)

        # self.tabWidget.tabBarCloseRequested.connect(lambda index: self.tabWidget.removeTab(index))
        # Connect the tabBarCloseRequested signal to a lambda function that removes the tab with the given index

    def addNewTab(self):
        newTab = QWidget()
        self.tabWidget.addTab(newTab, "Tab {}".format(self.tabWidget.count() + 1))

        deleteTabButton = QPushButton("x", self)
        deleteTabButton.clicked.connect(lambda: self.tabWidget.removeTab(self.tabWidget.currentIndex()))

        self.tabWidget.tabBar().setTabButton(self.tabWidget.count() - 1, QTabBar.RightSide, deleteTabButton)
        # Adds the delete button to the right side of the newly added tab


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())