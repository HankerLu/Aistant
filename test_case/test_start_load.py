from PyQt5 import QtWidgets, QtGui

class StartupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置启动窗口的属性
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 300, 200)
        
        # 添加启动图片
        startup_image = QtWidgets.QLabel(self)
        startup_image.setPixmap(QtGui.QPixmap("startup_image.png"))
        startup_image.setGeometry(50, 50, 200, 100)

# 创建应用程序对象
app = QtWidgets.QApplication([])

# 创建启动窗口对象
startup_window = StartupWindow()

# 显示启动窗口
startup_window.show()

# 运行应用程序
app.exec_()