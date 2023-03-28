from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout
import sys
import time
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.textEdit = QTextEdit()
        vbox.addWidget(self.textEdit)
        self.setLayout(vbox)
        self.show()

        for i in range(10):
            time.sleep(0.5)
            self.textEdit.append(str(i))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())