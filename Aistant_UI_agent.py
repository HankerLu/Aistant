from PyQt5 import QtCore, QtGui, QtWidgets
import Aistant_UI
# import Aistant_chat_tab_UI
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QShortcut
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.Qt import Qt
import Aistant_setting_manage

from ext import *

import openai
from enum import Enum
import threading
import time

class OpenAIReqStatus(Enum):
    REQ_STATUS_IDLE = 0
    REQ_STATUS_EXEC = 1
    REQ_STATUS_TIMEOUT = 2

# import pickle
# import markdown
class Writer(QObject):
    write_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def write_to_display_widget(self, text):
        self.write_signal.emit(text)

# class Aistant_Chat_UI_Tab_Agent(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Aistant_chat_tab_UI.Ui_Form()
#         self.ui.setupUi(self)


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

#模型设置
        self.aistant_model_list = self.chat_setting.aistant_chat_model_dict_get_config()
        for i in range(len(self.aistant_model_list)):
            c_m_txt = self.aistant_model_list[i]['company'] + '：' + self.aistant_model_list[i]['model']
            self.ui.comboBox_4.addItem(c_m_txt)

        self.aistant_current_model_idx = self.ui.comboBox_4.currentIndex()
        self.aistant_current_model_name = self.aistant_model_list[self.aistant_current_model_idx]['model']
        self.aistant_current_model_type = self.aistant_model_list[self.aistant_current_model_idx]['type']
        print("model name and type: ", self.aistant_current_model_type, self.aistant_current_model_name)
        self.ui.comboBox_4.currentIndexChanged.connect(self.aistant_update_model_descript)


#角色设置
        role_descript_list = self.chat_setting.aistant_select_role_and_descript_get_config()
        for i in range(len(role_descript_list)):
            r_d_txt = role_descript_list[i]['role'] + '：' + role_descript_list[i]['brief']
            # new_r_d_item = Q
            self.ui.comboBox_3.addItem(r_d_txt)

        # self.ui.comboBox_3.setCurrentIndex(0)
        # self.current_role_descript_idx = len(role_descript_list) - self.ui.comboBox_3.currentIndex()
        # ("self.current_role_descript_idx", self.current_role_descript_idx)
        # self.current_role_descript_idx = 0
        self.current_role_descript_idx = self.ui.comboBox_3.currentIndex()
        self.role_brief_txt = role_descript_list[self.current_role_descript_idx]['brief']
        self.descript_txt = role_descript_list[self.current_role_descript_idx]['descripion']
        self.ui.plainTextEdit.setPlainText(self.descript_txt)
        # 设置角色变更更新回调
        self.ui.comboBox_3.currentIndexChanged.connect(self.aistant_update_role_descript)


#编辑器
        self.aistant_editor_changesSaved = True
        
        self.ui.action_12.triggered.connect(self.aistant_editor_save_exec)
        self.ui.action_13.triggered.connect(self.aistant_editor_find_exec)
        self.ui.action_14.triggered.connect(self.aistant_editor_open_exec)
        # fontBox = QtWidgets.QFontComboBox(self)
        self.ui.fontComboBox.currentFontChanged.connect(lambda font: self.ui.textEdit_2.setCurrentFont(font))

        # Will display " pt" after each value
        self.ui.spinBox.setSuffix(" pt")

        self.ui.spinBox.valueChanged.connect(lambda size: self.ui.textEdit_2.setFontPointSize(size))

        self.ui.spinBox.setValue(14)

#密钥设置
        self.aistant_openai_api_key = openai.api_key

#链接按钮
        self.aistant_ui_activate_button()

#智能菜单
        self.aistant_init_smart_menu()

#=========================对话后端=======================================#
        print(" Aistant Aistant_Chat_Server init.")
        self.aistant_role_whole_content = self.role_brief_txt + self.descript_txt
        self.aistant_role_setting = {"role": "system", "content": self.aistant_role_whole_content}
        self.aistant_chat_history_messages = [self.aistant_role_setting,]

        self.aistant_chat_completion_req_status = OpenAIReqStatus.REQ_STATUS_IDLE

        self.thread_chat_completion_do_run = True
        self.thread_chat_completion = threading.Thread(target = self.chat_core_thread_exec)
        self.thread_chat_completion.start()
        
        self.core_threa_run_tick = 0
#======================================================================#


    def chat_core_thread_exec(self):
        print("chat bot start chat_core_thread_exec.")
        while self.thread_chat_completion_do_run:
            time.sleep(0.1)
            self.core_threa_run_tick +=1
            # if keyboard.is_pressed('enter') and keyboard.is_pressed('shift'):
            #     print("New line Command.")
            # elif keyboard.is_pressed('enter'):
            #     print("Key enter press.")
            #     # self.chat_core_button_submit_exec()
            if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_EXEC:
                response_content = self.openai_chat_completion_api_req()
                print('-----response_content', response_content)
                if response_content == '':  
                    self.aistant_chat_update_statusbar('API请求错误')
                    continue
                self.aistant_chat_history_messages.append(response_content) # 新增 completion
                self.ui_output_update()
                # print(response.choices[0]['message'])
                self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

    def get_openai_req_status_str(self):
        ret_str = "未知状态"
        if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE:
            ret_str = "无请求"
        elif self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_EXEC:
            ret_str = "请求中"
        elif self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_TIMEOUT:
                ret_str = "请求超时"
        return ret_str

    def update_openai_req_status(self, status):
        print("update_openai_req_status", status)
        self.aistant_chat_completion_req_status = status
        self.aistant_chat_update_statusbar(self.get_openai_req_status_str())

    def set_openai_req_thread_do_run(self, do_run):
        self.thread_chat_completion_do_run = do_run

# openai 请求接口
    def openai_chat_completion_api_req(self):
        print(openai.api_key, ' ', self.aistant_current_model_name)
        try:
            if self.aistant_current_model_type == 'Chat':
                response = openai.ChatCompletion.create(
                model = self.aistant_current_model_name,
                messages = self.aistant_chat_history_messages
                )
                return response.choices[0]['message']
            elif self.aistant_current_model_type == 'Complete':
                print("openai_chat_completion_api_req.Text Complete request.")
                prompt_in = self.aistant_ui_get_input_textedit_exec() + '\n'
                response = openai.Completion.create(
                model = self.aistant_current_model_name,
                prompt = prompt_in,
                temperature=0.7,
                max_tokens=200,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
                return response.choices[0]["text"]
            else:
                print("openai_chat_completion_api_req.Unknow request type.")
                response = ''
                return response

        except:
            print(response.choices[0]['message'])
            response = ''
            return response
# 更新输出文本
    def ui_output_update(self):
        message_content_total = ''
        msg_cnt = 0
        for msg in self.aistant_chat_history_messages:
            msg_cnt = msg_cnt + 1
            if self.aistant_current_model_type == 'Chat':
                role_msg = 'Unknown'
                if msg_cnt == 1:
                    role_msg = '用户(设定)'
                if msg['role'] == 'user':
                    role_msg = '用户'
                elif msg['role'] == 'assistant':
                    role_msg = 'chatGPT'
                msg_role_with_content = role_msg + ':\n' + msg['content']
                message_content_total += msg_role_with_content
            elif self.aistant_current_model_type == 'Complete':
                if isinstance(msg, dict) and msg['role'] == 'user':
                    msg_role_with_content = '用户' + ':\n' + msg['content']
                elif isinstance(msg, dict):
                    continue
                else:
                    msg_role_with_content = self.aistant_current_model_name + ':' + msg
                message_content_total += msg_role_with_content
            # 统一换行
            message_content_total += '\n\n'
        
        # 最终文本输出到面板
        self.aistant_ui_display_txt_output_exec(message_content_total)

    def aistant_chat_update_statusbar(self, content):
        self.aistant_ui_update_statusbar_txt(content)

#callback release
# 发送消息
    def chat_core_button_submit_exec(self):
        prompt_text = self.aistant_ui_get_input_textedit_exec()
        print("---prompt_text: %s"%prompt_text)
        # if prompt_text == '' or prompt_text == '\r' or prompt_text == '\n' or prompt_text == '\r\n':
        if prompt_text == '':
            # print("chat_core_button_submit_exec-Empty send prompt message.")
            self.aistant_chat_update_statusbar("发送消息为空")
            return 
        print("chat_core_button_submit_exec--", prompt_text)
    #     prompt_text = self.ui_agent.aistant_ui_get_textEdit_input_text()
        if self.aistant_current_model_type == 'Chat': 
            user_question = {"role": "user", "content": ""}
            user_question['content'] = prompt_text
            self.aistant_chat_history_messages.append(user_question) # 新增 
        elif self.aistant_current_model_type == 'Complete':
            user_question = {"role": "user", "content": ""}
            user_question['content'] = prompt_text
            self.aistant_chat_history_messages.append(user_question) # 新增 

        if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE or self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_TIMEOUT:
            self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_EXEC)

    def chat_core_button_clear_exec(self):
        print("chat core button clear.")
        # self.aistant_role_whole_content = self.role_brief_txt + self.descript_txt
        # self.aistant_role_setting = {"role": "system", "content": self.aistant_role_whole_content}
        self.aistant_chat_history_messages = [self.aistant_role_setting,]
        self.ui_output_update()

    def chat_core_button_cancel_exec(self):
        print("chat core button cancel.")
        self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

    def chat_core_button_save_exec(self):
        print("chat core button save.")
        self.aistant_ui_save_current_chat_exec()

    def chat_core_button_withdraw_exec(self):
        print("set chat core withdraw.")
        if len(self.aistant_chat_history_messages) > 2:
            del self.aistant_chat_history_messages[-1]
            del self.aistant_chat_history_messages[-1]
            self.ui_output_update()

    def chat_core_teminate_thread_exec(self):
        self.thread_chat_completion_do_run = False

#========================================================================#

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
        self.ui.fontComboBox.setVisible(False)
        self.ui.spinBox.setVisible(False)

    def aistant_show_edit_window_widgets(self):
        print("aistant_show_edit_window")
        self.ui.textEdit_2.setVisible(True)
        self.ui.toolBar_2.setVisible(True)
        self.ui.fontComboBox.setVisible(True)
        self.ui.spinBox.setVisible(True)

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

# 保存所有设置
    def aistant_ui_update_all_setting(self):
        print("aistant_ui_update_all_setting")

    def aistant_ui_activate_button(self):
        self.ui.pushButton_4.clicked.connect(self.chat_core_button_submit_exec)
        # self.ui.pushButton_4.setShortcut("Ctrl+A")
        self.ui.pushButton_7.clicked.connect(self.chat_core_button_clear_exec)
        self.ui.pushButton_5.clicked.connect(self.chat_core_button_cancel_exec)
        self.ui.pushButton_6.clicked.connect(self.chat_core_button_save_exec)
        self.ui.pushButton.clicked.connect(self.chat_core_button_withdraw_exec)

        self.ui.pushButton_2.clicked.connect(self.aistant_ui_update_all_setting)

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
        if self.chat_core_teminate_thread_exec != None:
            self.chat_core_teminate_thread_exec()
# 更新模型回调
    def aistant_update_model_descript(self, model_idx):
        # 更新model最新idx, 名称和类型
        self.aistant_current_model_idx = self.ui.comboBox_4.currentIndex()
        self.aistant_current_model_name = self.aistant_model_list[self.aistant_current_model_idx]['model']
        self.aistant_current_model_type = self.aistant_model_list[self.aistant_current_model_idx]['type']
        print("aistant_update_model_descript: ", self.aistant_current_model_idx, ' ',self.aistant_current_model_name, ' ',self.aistant_current_model_type)
        self.aistant_chat_history_messages = [self.aistant_role_setting,]

# 更新角色回调
    def aistant_update_role_descript(self, role_idx):
        print("aistant_update_role_descript", role_idx)
        # 候选框id
        self.current_role_descript_idx = self.ui.comboBox_3.currentIndex()
        # 角色简称
        self.descript_txt = self.chat_setting.aistant_select_role_and_descript_get_config()[self.current_role_descript_idx]['descripion']
        # 角色描述
        self.role_brief_txt = self.chat_setting.aistant_select_role_and_descript_get_config()[self.current_role_descript_idx]['brief']
        # 更新角色描述到设置面板
        self.ui.plainTextEdit.setPlainText(self.descript_txt) #更新
        # 更新token中role的content
        self.aistant_role_whole_content = self.role_brief_txt + self.descript_txt
        # 更新完整的role token
        self.aistant_role_setting = {"role": "system", "content": self.aistant_role_whole_content}
        # 更新历史信息
        if len(self.aistant_chat_history_messages) >= 1:
            self.aistant_chat_history_messages[0] = self.aistant_role_setting
        # 更新问答输出面板
        self.ui_output_update()

# ------editor 
    def aistant_editor_open_exec(self):
        print("aistant_editor_open_exec")
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self.ui.stackedWidget, 'Open File',".","(*.writer)")[0]

        if self.filename:
            with open(self.filename,"rt") as file:
                self.ui.textEdit_2.setText(file.read())
    
    def aistant_editor_save_exec(self):
        print("aistant_editor_save_exec")
        # Only open dialog if there is no filename yet
        #PYQT5 Returns a tuple in PyQt5, we only need the filename
        if not self.filename:
          self.filename = QtWidgets.QFileDialog.getSaveFileName(self.ui.stackedWidget, 'Save File')[0]

        if self.filename:
            
            # Append extension if not there yet
            if not self.filename.endswith(".writer"):
              self.filename += ".writer"
            # if not self.filename.endswith(".txt"):
            #       self.filename += ".txt"

            # We just store the contents of the text file along with the
            # format in html, which Qt does in a very nice way for us
            with open(self.filename,"wt") as file:
                file.write(self.ui.textEdit_2.toHtml())
                # file.write(self.ui.textEdit_2.toPlainText())

            self.aistant_editor_changesSaved = True

    def aistant_editor_find_exec(self):
        print("aistant_editor_find_exec")
        find.Find(self).show()

# 编辑器智能菜单
    def aistant_init_smart_menu(self):
        # 创建快捷键和弹出菜单
        self.aistant_s_menu_shortcut = QtWidgets.QShortcut('Ctrl+;', self.ui.textEdit_2)
        self.aistant_s_menu_shortcut.activated.connect(self.aistent_show_smart_menu)
        self.aistant_smart_menu = QtWidgets.QMenu(self.ui.textEdit_2)
        self.aistant_smart_action_query = QtWidgets.QAction('询问', self.ui.textEdit_2)
        self.aistant_smart_action_summarize = QtWidgets.QAction('总结', self.ui.textEdit_2)
        self.aistant_smart_menu.addAction(self.aistant_smart_action_query)
        self.aistant_smart_menu.addAction(self.aistant_smart_action_summarize)
        
        # 菜单选项链接回调
        self.aistant_smart_action_query.triggered.connect(self.aistant_smart_query_exec)
        self.aistant_smart_action_summarize.triggered.connect(self.aistant_smart_summarize_exec)
        
        self.aistant_smart_menu.setEnabled(True)

    def aistent_show_smart_menu(self):
        # 显示弹出菜单
        # TODO: 前置触发条件，其他条件下直接过滤
        cursor_x = self.ui.textEdit_2.cursorRect().left()
        cursor_y = self.ui.textEdit_2.cursorRect().bottom()
        cursor_position = self.ui.textEdit_2.mapToGlobal(QtCore.QPoint(cursor_x, cursor_y))
        self.aistant_smart_menu.exec_(cursor_position)

    def aistant_smart_query_exec(self):
        print("aistant_smart_query_exec")

    def aistant_smart_summarize_exec(self):
        print("aistant_smart_summarize_exec")
# ------------------------------------------------------------------------ #
# callback release
    def aistant_ui_get_input_textedit_exec(self):
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


if __name__ == "__main__":
    aistant_ui = Aistant_UI_Agent()
    aistant_ui.Aistant_UI_show()
