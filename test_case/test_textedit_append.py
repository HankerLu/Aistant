# from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout
# import sys
# import time
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         vbox = QVBoxLayout()
#         self.textEdit = QTextEdit()
#         vbox.addWidget(self.textEdit)
#         self.setLayout(vbox)
#         self.show()

#     def display_0(self):
#         # for i in range(10):
        
#         self.textEdit.append('str(0)')

#     def display_1(self):

#         self.textEdit.append('str(1)')

#     def display_2(self):
#         self.textEdit.append('str(2)')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     time.sleep(0.5)
#     ex.display_0()
#     while True:
#         time.sleep(0.5)
#     ex.display_1()
#     time.sleep(0.5)
#     ex.display_2()
#     sys.exit(app.exec_())


from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

# import Qtimer
from PyQt5.QtCore import QTimer

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.timer = QTimer()
        self.timer.timeout.connect(self.append_text)
        self.timer.start(200)

    def append_text(self):
        self.text_edit.insertPlainText("1")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())