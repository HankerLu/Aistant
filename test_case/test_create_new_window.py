import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建按钮
        self.button = QPushButton('Create new window', self)
        self.button.clicked.connect(self.create_new_window)

    def create_new_window(self):
        # 创建新窗口
        self.new_window = MainWindow()
        self.new_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())