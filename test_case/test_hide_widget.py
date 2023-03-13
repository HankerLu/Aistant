import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个按钮和一个标签
        self.button = QPushButton('点击隐藏标签', self)
        self.label = QLabel('这是标签', self)

        # 将按钮和标签移动到某个位置
        self.button.move(20, 20)
        self.label.move(20, 50)

        # 绑定按钮点击事件
        self.button.clicked.connect(self.hide_label)

    def hide_label(self):
        # 隐藏标签
        self.label.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())