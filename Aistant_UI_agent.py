from PyQt5 import QtCore, QtGui, QtWidgets
import Aistant_UI
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtGui import QTextCharFormat, QColor

import markdown
class Writer(QObject):
    write_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def write_to_display_widget(self, text):
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
        # self.textBrower_writer.write_signal.connect(self.ui.textBrowser.setMarkdown)
        # self.textBrower_writer.write_signal.connect(self.ui.textBrowser.setHtml)

        self.statusbar_writer = Writer()
        self.statusbar_writer.write_signal.connect(self.ui.statusbar.showMessage)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ui.textBrowser.setFont(font)
        self.ui.textEdit.setFont(font)

        textbrowser_format = QTextCharFormat()
        textbrowser_format.setForeground(QColor(31, 31, 31))
        # textbrowser_format.setBackground(QColor(0, 255, 0)) 
        # self.ui.textBrowser.setStyleSheet("background-color: balck;")
        self.ui.textBrowser.setStyleSheet("background-color: rgb(210,210,210);")
        self.ui.textBrowser.setCurrentCharFormat(textbrowser_format)  # 应用高亮格式

        self.ui.statusbar.showMessage('界面加载完成')

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
        self.ui.pushButton_7.clicked.connect(self.chat_clear_callback)
        self.ui.pushButton_5.clicked.connect(self.chat_cancel_callback)
        self.ui.pushButton_6.clicked.connect(self.chat_save_callback)

    def Aistant_UI_show(self):
        self.mainwin.show()
        sys.exit(self.app.exec_())


# callback release
    def aistant_ui_get_input_textedit_exec(self):
        # print("aistant_ui_get_input_textedit_exec")
        return self.ui.textEdit.toPlainText()

    def aistant_ui_display_txt_output_exec(self, txt_display):
        # self.ui.textBrowser.setText(txt_display)
        # html = markdown.markdown(txt_display)
        self.textBrower_writer.write_to_display_widget(txt_display)

    def aistant_ui_update_statusbar_txt(self, txt_display):
        self.statusbar_writer.write_to_display_widget(txt_display)

    def aistant_ui_save_current_chat_exec(self):
        print("aistant_ui_save_current_chat_exec")
        filename, _ = QFileDialog.getSaveFileName(self.ui.stackedWidget, "保存对话", "", "文本文件 (*.txt);;所有文件 (*)")
        if filename == '':
            print("save_conversation_name_input no file")
            return
        if filename:
            with open(filename, "w") as file:
                file.write(self.ui.textBrowser.toPlainText())

# callback consume
    def aistant_ui_set_chat_submit_cb_ptr(self, chat_submit_cb):
        # print("aistant_ui_set_chat_submit_callback", chat_submit_cb)
        self.chat_submit_callback = chat_submit_cb

    def aistant_ui_set_chat_clear_cb_ptr(self, chat_clear_cb):
        self.chat_clear_callback = chat_clear_cb

    def aistant_ui_set_chat_cancel_cb_ptr(self, chat_cancel_cb):
        self.chat_cancel_callback = chat_cancel_cb

    def aistant_ui_set_chat_save_cb_ptr(self, chat_save_cb):
        self.chat_save_callback = chat_save_cb