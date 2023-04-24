from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('MainWindow')

        # 设置背景图片
        palette = QPalette()
        pixmap = QPixmap("background.jpg")
        palette.setBrush(self.backgroundRole(), QBrush(pixmap))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()