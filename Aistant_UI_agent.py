from PyQt5 import QtCore, QtGui, QtWidgets
import Aistant_UI
import Aistant_chat_tab_UI
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QPlainTextEdit
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.Qt import Qt
import Aistant_setting_manage

# import pickle
# import markdown
class Writer(QObject):
    write_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def write_to_display_widget(self, text):
        self.write_signal.emit(text)

class Aistant_Chat_UI_Tab_Agent(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Aistant_chat_tab_UI.Ui_Form()
        self.ui.setupUi(self)


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
        self.ui.action_10.triggered.connect(self.action_chat_setting_exec)

        self.textBrower_writer = Writer()
        self.textBrower_writer.write_signal.connect(self.ui.textBrowser.setText)
        # self.textBrower_writer.write_signal.connect(self.ui.textBrowser.setMarkdown)
        # self.textBrower_writer.write_signal.connect(self.ui.textBrowser.setHtml)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ui.textBrowser.setFont(font)
        self.ui.textEdit.setFont(font)

        textbrowser_format = QTextCharFormat()
        textbrowser_format.setForeground(QColor(31, 31, 31))
        self.ui.textBrowser.setStyleSheet("background-color: rgb(210,210,210);")
        self.ui.textBrowser.setCurrentCharFormat(textbrowser_format)  # 应用高亮格式


        self.statusbar_writer = Writer()
        self.statusbar_writer.write_signal.connect(self.ui.statusbar.showMessage)
        self.ui.statusbar.showMessage('界面加载完成')

        # self.ui.stackedWidget.keyPressEvent = self.aistant_keyPressEvent
        # self.ui.textEdit.keyPressEvent = self.aistant_keyPressEvent
        # self.mainwin.keyPressEvent = self.aistant_keyPressEvent
        self.mainwin.closeEvent = self.aistant_closeEvent

#工具栏
        self.aistant_chat_windows_show_status = True
        self.ui.action_7.triggered.connect(self.aistant_editor_only_exec)

        self.aistant_edit_window_show_status = True
        self.ui.action_4.triggered.connect(self.aistant_chat_only_exec)

        self.ui.action_5.triggered.connect(self.aistant_chat_editor_both_exec)
#设置参数
        self.chat_setting = Aistant_setting_manage.Aistant_Chat_Setting()

        model_list = self.chat_setting.aistant_chat_model_dict_get_config()
        for i in range(len(model_list)):
            c_m_txt = model_list[i]['company'] + '：' + model_list[i]['model']
            self.ui.comboBox_4.addItem(c_m_txt)

        role_descript_list = self.chat_setting.aistant_select_role_and_descript_get_config()
        for i in range(len(role_descript_list)):
            r_d_txt = role_descript_list[i]['role'] + '：' + role_descript_list[i]['brief']
            # new_r_d_item = Q
            self.ui.comboBox_3.addItem(r_d_txt)

        self.current_role_descript_idx = self.ui.comboBox_3.currentIndex()
        descript_txt = role_descript_list[self.current_role_descript_idx]['descripion']
        self.ui.plainTextEdit.setPlainText(descript_txt)
        self.ui.comboBox_3.currentIndexChanged.connect(self.aistant_update_role_descript)

        # self.chat_setting.aistant_select_role_and_descript_set_config()

#新建及删除对话标签页
        # self.hide_draft_txt_editor_status = True
        # self.ui.pushButton_3.clicked.connect(self.aistant_create_new_chat_tab_page_exec)
        # self.ui.tabWidget.tabCloseRequested.connect(self.aistant_remove_old_chat_tab_page_exec)
        # # self.ui.tabWidget.removeTab(self.ui.tabWidget.indexOf(self.ui.tab_2))
        
        # self.close_tab_button = QtWidgets.QToolButton()
        # self.close_tab_button.setToolTip('Add New Tab')
        # self.close_tab_button.clicked.connect(self.aistant_create_new_chat_tab_page_exec)
        # self.close_tab_button.setIcon(QtWidgets.QWidget().style().standardIcon(QtWidgets.QStyle.SP_DialogYesButton))
        # self.ui.tabWidget.setCornerWidget(self.close_tab_button, QtCore.Qt.TopRightCorner)

    def aistant_remove_old_chat_tab_page_exec(self, request_tab_id):
        print("aistant_remove_old_chat_tab_page_exec. req_id:", request_tab_id)
        if request_tab_id!= self.ui.tabWidget.indexOf(self.ui.tab_2):
            print("this is the tab page to be remove")
            self.ui.tabWidget.removeTab(request_tab_id) 

    def aistant_hide_draft_txt_editor(self):
        if self.hide_draft_txt_editor_status == True:
            self.ui.textEdit_3.setVisible(False)
            self.hide_draft_txt_editor_status = False
        else:
            self.ui.textEdit_3.setVisible(True)
            self.hide_draft_txt_editor_status = True

    def aistant_create_new_chat_tab_page_exec(self):
        print("aistant_create_new_chat_tab_page")

        # ui_form = Aistant_chat_tab_UI.Ui_Form()
        # new_tab = QtWidgets.QWidget()
        # Aistant_chat_tab_UI.Ui_Form().setupUi(new_tab)
        new_tab = Aistant_Chat_UI_Tab_Agent(self.ui.tabWidget)
        new_tab_name = "对话" + str(self.ui.tabWidget.count())
        new_tab_insert_pos = self.ui.tabWidget.count() - 1
        self.ui.tabWidget.insertTab(new_tab_insert_pos, new_tab, new_tab_name) #基于当前名称更新对话标签名
        textbrowser_format = QTextCharFormat()
        textbrowser_format.setForeground(QColor(31, 31, 31))
        new_tab.ui.textBrowser.setStyleSheet("background-color: rgb(210,210,210);")
        new_tab.ui.textBrowser.setCurrentCharFormat(textbrowser_format)  # 应用高亮格式

        font = QtGui.QFont()
        font.setPointSize(12)
        new_tab.ui.textBrowser.setFont(font)
        new_tab.ui.textEdit_2.setFont(font)

#-----对话和编辑窗口开关回调-----#
#"仅写"回调
    def aistant_editor_only_exec(self):
        print("chat_hide_chat_window")
        if self.aistant_chat_windows_show_status:
            self.aistant_hide_chat_window_widgets()
            self.aistant_chat_windows_show_status = False 
        if self.aistant_edit_window_show_status == False:
            self.aistant_show_edit_window_widgets()
            self.aistant_edit_window_show_status = True
        # else:
        #     self.aistant_show_chat_window_widgets()
        #     self.aistant_chat_windows_show_status = True

#"仅聊"回调
    def aistant_chat_only_exec(self):
        if self.aistant_edit_window_show_status:
            self.aistant_hide_edit_window_widgets()
            self.aistant_edit_window_show_status = False
        if self.aistant_chat_windows_show_status == False:
            self.aistant_show_chat_window_widgets()
            self.aistant_chat_windows_show_status = True 

#"聊与写"回调
    def aistant_chat_editor_both_exec(self):
        if self.aistant_edit_window_show_status == False:
            self.aistant_show_edit_window_widgets()
            self.aistant_edit_window_show_status = True
        if self.aistant_chat_windows_show_status == False:
            self.aistant_show_chat_window_widgets()
            self.aistant_chat_windows_show_status = True 

    def aistant_hide_edit_window_widgets(self):
        print("aistant_chat_only_exec")
        self.ui.textEdit_2.setVisible(False)
        self.ui.toolBar_2.setVisible(False)

    def aistant_show_edit_window_widgets(self):
        print("aistant_show_edit_window")
        self.ui.textEdit_2.setVisible(True)
        self.ui.toolBar_2.setVisible(True)

    def aistant_hide_chat_window_widgets(self):
        self.ui.textEdit.setVisible(False)
        self.ui.pushButton_4.setVisible(False)
        self.ui.pushButton_5.setVisible(False)
        self.ui.groupBox_2.setVisible(False)
        self.ui.scrollArea.setVisible(False)
        self.ui.pushButton.setVisible(False)
        self.ui.pushButton_6.setVisible(False)
        self.ui.pushButton_7.setVisible(False)

    def aistant_show_chat_window_widgets(self):
        self.ui.textEdit.setVisible(True)
        self.ui.pushButton_4.setVisible(True)
        self.ui.pushButton_5.setVisible(True)
        self.ui.groupBox_2.setVisible(True)
        self.ui.scrollArea.setVisible(True)
        self.ui.pushButton.setVisible(True)
        self.ui.pushButton_6.setVisible(True)
        self.ui.pushButton_7.setVisible(True)

    def chat_page_button_submit(self):
        print("chat_page_button_submit", self.ui.textEdit.toPlainText())

    def action_chatgpt_slot_exec(self):
        print("action_chatgpt_slot_exec. self.ui.stackedWidget.setCurrentIndex(0).")
        self.ui.stackedWidget.setCurrentIndex(0)

    def action_key_manage_exec(self):
        print("action_key_manage_exec")
        self.ui.stackedWidget.setCurrentIndex(1)

    def action_chat_setting_exec(self):
        print("action_chat_setting_exec")
        self.ui.stackedWidget.setCurrentIndex(2)

    def aistant_ui_get_textEdit_input_text(self):
        print("aistant_ui_get_textEdit", self.ui.textEdit.toPlainText())
        return self.ui.textEdit.toPlainText()

    def aistant_ui_activate_button(self):
        self.ui.pushButton_4.clicked.connect(self.chat_submit_callback)
        self.ui.pushButton_7.clicked.connect(self.chat_clear_callback)
        self.ui.pushButton_5.clicked.connect(self.chat_cancel_callback)
        self.ui.pushButton_6.clicked.connect(self.chat_save_callback)
        self.ui.pushButton.clicked.connect(self.chat_withdraw_callback)

    def Aistant_UI_show(self):
        self.mainwin.show()
        sys.exit(self.app.exec_())

    def aistant_keyPressEvent(self, event):
        print("key pressed trig.", event)
        if event.key() == Qt.Key_Shift:
            print("key pressed Key_Shift")
        elif event.key() == Qt.Key_Enter:
            print("key pressed Key_Enter")

    def aistant_mousePressEvent(self, event):
        print("mouse pressed trig.", event)

    def aistant_returnPressEvent(self):
        print("return pressed trig.")

    def aistant_closeEvent(self, event):
        print("close event trig.")
        if self.chat_core_teminate_callback != None:
            self.chat_core_teminate_callback()

    def aistant_update_role_descript(self, text):
        print("aistant_update_role_descript", text)
        self.current_role_descript_idx = self.ui.comboBox_3.currentIndex()
        descript_txt = self.chat_setting.aistant_select_role_and_descript_get_config()[self.current_role_descript_idx]['descripion']
        self.ui.plainTextEdit.setPlainText(descript_txt)


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

    def aistant_ui_set_chat_withdraw_cb_ptr(self, chat_withdraw_cb):
        self.chat_withdraw_callback = chat_withdraw_cb

    def aistant_ui_teminate_chat_core(self, chat_core_teminate_cb):
        self.chat_core_teminate_callback = chat_core_teminate_cb