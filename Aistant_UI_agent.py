from PyQt5 import QtCore, QtGui, QtWidgets
import Aistant_UI
import sys
from PyQt5.QtCore import QObject, pyqtSignal

class Writer(QObject):
    write_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def write_to_browser(self, text):
        self.write_signal.emit(text)

# 连接操作：
# 1.连接前端和自定义槽函数
# 2.自定义槽函数
class Aistant_UI_Agent:
    def __init__(self):
        print(" Aistant UI agent init.")
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Aistant_UI.Ui_MainWindow()
        ui.setupUi(MainWindow)
        
        self.mainwin = MainWindow
        self.app = app
        self.ui = ui 

        self.ui.action_chatgpt.triggered.connect(self.action_chatgpt_slot_exec)
        self.ui.action_6.triggered.connect(self.action_key_manage_exec)

        self.textBrower_writer = Writer()
        self.textBrower_writer.write_signal.connect(self.ui.textBrowser.setText)

    def chat_page_button_submit(self):
        print("chat_page_button_submit", self.ui.textEdit.toPlainText())

    def action_chatgpt_slot_exec(self):
        print("action_chatgpt_slot_exec. self.ui.stackedWidget.setCurrentIndex(0).")
        self.ui.stackedWidget.setCurrentIndex(0)

    def action_key_manage_exec(self):
        print("action_key_manage_exec")
        self.ui.stackedWidget.setCurrentIndex(1)

    def aistant_ui_get_textEdit_input_text(self):
        print("aistant_ui_get_textEdit", self.ui.textEdit.toPlainText())
        return self.ui.textEdit.toPlainText()

    def aitant_ui_activate_button(self):
        self.ui.pushButton_4.clicked.connect(self.chat_submit_callback)

    def Aistant_UI_show(self):
        self.mainwin.show()
        sys.exit(self.app.exec_())

# callback release
    def aistant_ui_get_input_textedit_exec(self):
        # print("aistant_ui_get_input_textedit_exec")
        return self.ui.textEdit.toPlainText()

    def aistant_ui_display_txt_output_exec(self, txt_display):
        # self.ui.textBrowser.setText(txt_display)
        self.textBrower_writer.write_to_browser(txt_display)

# callback consume
    def aistant_ui_set_chat_submit_cb_ptr(self, chat_submit_cb):
        # print("aistant_ui_set_chat_submit_callback", chat_submit_cb)
        self.chat_submit_callback = chat_submit_cb

