from PyQt5.QtCore import QObject, pyqtSignal
import time

class Writer(QObject):
    write_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def write_to_browser(self, text):
        # 在子线程中调用write_signal，发送文本信号
        self.write_signal.emit(text)

import sys
import threading
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        print("0000")
        super().__init__()
        self.initUI()
        self.writer_thread = threading.Thread(target=self.write_to_browser_thread)
        self.writer_thread.start()
        self.writer = Writer()
        self.writer.write_signal.connect(self.write_to_browser_slot)
        print("1111")

    def initUI(self):
        self.textBrowser = QTextEdit()
        self.setCentralWidget(self.textBrowser)

    @pyqtSlot(str)
    def write_to_browser_slot(self, text):
        self.textBrowser.setText(text)

    def write_to_browser_thread(self):
        while True:
            # 在子线程中通过writer调用槽函数write_to_browser_slot
            print("222")
            self.writer.write_to_browser("Hello from the writer thread!")
            time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()