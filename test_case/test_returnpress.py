from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QVBoxLayout, QWidget, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("文本编辑和回车按键发送")

        # 创建一个编辑框
        self.text_edit = QLineEdit()
        # 将回车键的按下信号连接到发送消息槽
        self.text_edit.returnPressed.connect(self.send_message)

        # 设置布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.text_edit)

        self.setCentralWidget(central_widget)

    def send_message(self):
        # 获取文本编辑框中的文本
        text = self.text_edit.toPlainText()
        # 显示发送的消息
        print("发送消息:", text)
        # 清空文本编辑框
        self.text_edit.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()