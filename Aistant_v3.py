# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal,QThread
from PyQt5.QtWidgets import QFileDialog, QShortcut
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.Qt import Qt
import sys
import json
#增加一个基于pyqt5的启动加载界面
load_app = QtWidgets.QApplication(sys.argv)
#启动加载图片为8666753_message_circle_chat_icon.ico
load_widget = QtWidgets.QWidget()
# load_widget.setWindowFlags(Qt.FramelessWindowHint)
load_widget.setWindowOpacity(0.5)
load_widget.setFixedSize(200, 200)
load_widget.move(500, 300)
# load_widget.setStyleSheet("background-image:url(./8666753_message_circle_chat_icon.ico);")#这句代码没有显示出来，不知道为什么
# load_widget.setStyleSheet("background-image:url(./8666753_message_circle_chat_icon.ico);")
load_widget.show()

import Aistant_UI
import Aistant_setting_manage
import Aistant_editor_find
import openai
from enum import Enum
import threading
import time
import logging

load_widget.hide()

logging.basicConfig(filename='aistant.log', level=logging.INFO)

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

class AistantThread(QThread):
    # 定义一个信号，用于在线程中发射信号
    signal = pyqtSignal(str)
    signal_int = pyqtSignal(int)
    def __init__(self, handle, parent=None):
        super(AistantThread, self).__init__(parent)
        self.run_handle = handle
    
    def run(self):
        # 在线程中执行长时间操作
        if self.run_handle != None:
            ret = self.run_handle()
            
            print("AistantThread:run_handle. RET: ", ret)
            self.signal.emit(ret)
    
    def signal_emit(self, val):
        self.signal_int.emit(val)

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
        logging.info("Aistant UI agent init.")
        # app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Aistant_UI.Ui_MainWindow()
        ui.setupUi(MainWindow)
        
        self.mainwin = MainWindow
        # self.app = app
        self.ui = ui 
        # self.app = app
        self.new_app_list = []
        #设置窗口的图标
        self.mainwin.setWindowIcon(QtGui.QIcon('./aistant.ico'))
        self.ui.action_chatgpt.triggered.connect(self.action_chatgpt_slot_exec)
        self.ui.action_6.triggered.connect(self.create_new_mainwindow_exec)
        self.ui.action_6.setVisible(False)
        self.ui.action_10.triggered.connect(self.action_chat_setting_exec)
        self.ui.action_8.triggered.connect(self.action_chat_help_exec)

        # self.mainwin.setStyleSheet("background-color: rgb(230,255,255);")

        self.chat_textedit_writer = Writer()
        self.chat_textedit_writer.write_signal.connect(self.aistant_chat_textedit_set_txt)

        self.chat_textedit_streamer = Writer()
        self.chat_textedit_streamer.write_signal.connect(self.aistant_chat_textedit_stream_update)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.ui.textEdit.setFont(font)
        self.ui.textEdit.setStyleSheet("background-color: rgb(255,192,203);")

        textbrowser_format = QTextCharFormat()
        textbrowser_format.setForeground(QColor(31, 31, 31))
        self.ui.textEdit_3.setFont(font)
        self.ui.textEdit_3.setStyleSheet("background-color: rgb(255,255,204);")
        # self.ui.textEdit_3.setStyleSheet("background-color: rgb(173,216,230);")
        self.ui.textEdit_3.setCurrentCharFormat(textbrowser_format)  # 应用高亮格式


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
        self.ui.action_7.setIcon(QtGui.QIcon('./right.ico'))

        self.aistant_edit_window_show_status = True
        self.ui.action_4.triggered.connect(self.aistant_chat_only_exec)
        self.ui.action_4.setIcon(QtGui.QIcon('./left.ico'))

        self.ui.action_5.triggered.connect(self.aistant_chat_editor_both_exec)
        self.ui.action_5.setIcon(QtGui.QIcon('./both.ico'))
#设置参数
        self.aistant_setting = Aistant_setting_manage.Aistant_Chat_Setting()

#----------------- 基于本地配置文件的UI当前状态更新 -------------------------#
#角色设定(基于本地配置)
        role_descript_list = self.aistant_setting.aistant_select_role_and_descript_get_config()
        role_id = self.aistant_setting.aistant_setting_get_role_id()
        if role_id != -1:
            self.current_role_descript_idx = role_id
        else:
            logging.info("role id error.")
            self.current_role_descript_idx = 0
        print("role_id: ", self.current_role_descript_idx)
        for i in range(len(role_descript_list)):
            r_d_txt = role_descript_list[i]['role'] + '：' + role_descript_list[i]['brief']
            # new_r_d_item = Q
            self.ui.comboBox_3.addItem(r_d_txt)
        self.ui.comboBox_3.setCurrentIndex(self.current_role_descript_idx)
        self.ui.comboBox_3.currentIndexChanged.connect(self.aistant_change_role_exec)

#模型设定(基于本地配置)

        self.aistant_model_list = self.aistant_setting.aistant_chat_model_dict_get_config()
        for i in range(len(self.aistant_model_list)):
            c_m_txt = self.aistant_model_list[i]['company'] + '：' + self.aistant_model_list[i]['model']
            self.ui.comboBox_4.addItem(c_m_txt)

        model_id = self.aistant_setting.aistant_setting_get_model_id()
        if model_id != -1:
            self.aistant_current_model_idx = model_id
        else:
            self.aistant_current_model_idx = 0 

        self.aistant_current_model_name = self.aistant_model_list[self.aistant_current_model_idx]['model']
        self.aistant_current_model_type = self.aistant_model_list[self.aistant_current_model_idx]['type']
        print("model name and type: ", self.aistant_current_model_type, self.aistant_current_model_name)

        self.ui.comboBox_4.setCurrentIndex(self.aistant_current_model_idx)
        self.ui.comboBox_4.currentIndexChanged.connect(self.aistant_change_model_exec)

#多轮对话设定(基于本地配置)
        self.multi_chat_enable = self.aistant_setting.aistant_setting_get_multi_chat()
        print("self.multi_chat_enable: ", self.multi_chat_enable)
        self.ui.checkBox.setChecked(self.multi_chat_enable)
        self.ui.checkBox.stateChanged.connect(self.aistant_chat_multi_talk_enable) 

#密钥设置
        self.aistant_openai_api_key = self.aistant_setting.aistant_setting_get_cur_key_val()
        
        if self.aistant_openai_api_key != '':
            openai.api_key = self.aistant_openai_api_key
            print("[Init]openai api key update: ", openai.api_key)
        else:
            logging.info("[Init]openai api key empty.")
        self.ui.pushButton_8.clicked.connect(self.aistant_update_and_save_key_exec)

        self.aistant_api_his_keys_list = []

#密钥检测进度条设置
        self.ui.progressBar.setValue(0)
        self.aistant_test_key_count_thread = AistantThread(self.aistant_api_key_test_exec)
        self.aistant_test_key_count_thread.signal_int.connect(self.aistant_api_key_test_update_progressbar)

        self.aistant_test_key_main_thread = AistantThread(self.aistant_api_key_test_block_exec)
        self.aistant_test_key_main_thread.signal.connect(self.ui.label_14.setText)

        self.ui.pushButton_9.clicked.connect(self.aistant_test_api_key_trig_exec)
        self.aistant_api_key_test_status = 0
        self.test_exec_cnt = 0
        self.test_api_key_val = ''
#-------------------------------------------------------------------------#

#编辑器
        self.aistant_editor_changesSaved = True
        
        self.ui.action_12.triggered.connect(self.aistant_editor_save_exec)
        self.ui.action_12.setIcon(QtGui.QIcon('./save.ico'))
        self.ui.action_13.triggered.connect(self.aistant_editor_find_exec)
        self.ui.action_13.setIcon(QtGui.QIcon('./find.ico'))
        self.ui.action_14.triggered.connect(self.aistant_editor_open_exec)
        self.ui.action_14.setIcon(QtGui.QIcon('./open.ico'))
        # fontBox = QtWidgets.QFontComboBox(self)
        # self.ui.fontComboBox.currentFontChanged.connect(lambda font: self.ui.textEdit_2.setCurrentFont(font))
        self.ui.fontComboBox.currentFontChanged.connect(self.aistant_test_editor_change_font)
        self.ui.textEdit_2.setCurrentFont(self.ui.fontComboBox.currentFont())

        # Will display " pt" after each value
        self.ui.spinBox.setSuffix(" pt")

        # self.ui.spinBox.valueChanged.connect(lambda size: self.ui.textEdit_2.setFontPointSize(size))
        self.ui.spinBox.valueChanged.connect(self.aistant_test_editor_change_size)
        self.ui.spinBox.setValue(14)

        self.ui.textEdit_2.cursorPositionChanged.connect(self.aistant_cursor_change_event)
        # self.ui.textEdit_2.currentCharFormatChanged.connect(self.aistant_format_change_event)

        self.aistant_editor_ai_model = 'text-davinci-003'

        self.ui.textEdit_2.setStyleSheet("background-color: rgb(200, 255, 190);")

        # self.filename = ''

#链接按钮
        self.aistant_ui_activate_button()

#智能菜单
        self.aistant_init_smart_menu()

#密钥框加密显示
        self.ui.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit.setPlaceholderText("请输入密码")

        self.ui.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit_4.setPlaceholderText("请输入密码")

        self.aistant_password_mode = True
        self.ui.lineEdit.setText(openai.api_key)
        self.ui.pushButton_11.clicked.connect(self.aistant_encrypt_toggle)
        # self.current_input_origin_key = openai.api_key
        # crypt_key = self.encrypt_string(openai.api_key)
        # self.ui.lineEdit.textChanged.connect(self.aistant_default_key_crypt_handle)
        # self.ui.lineEdit_4.textChanged.connect(self.aistant_test_key_crypt_handle)

#自动生成主题
        self.ui.pushButton_13.clicked.connect(self.aistant_auto_generate_title_trig)
        self.aistant_thread_auto_generate_title = AistantThread(self.aistant_auto_generate_title_exec)
        self.aistant_thread_auto_generate_title.signal.connect(self.ui.lineEdit_3.setText)

#stream流管理
        self.aistant_latest_query_dict = {}
        self.editor_req_stream_res = None
        self.aistant_chat_stream_update_enable = True

#当前加载或保存的对话文件的路径
        self.aistant_current_chat_file_path = ''

#增加一个保存对话输出内容的含有key-value的字典
        self.aistant_chat_output_content_key_value = []

#增加一个对话输出的分割线
        self.aistant_chat_output_divider = '\n\n-----------------------------------\n'
#=========================对话后端=======================================#
        print(" Aistant Aistant_Chat_Server init.")
        self.aistant_role_content_update()
        self.aistant_chat_history_messages = [self.aistant_role_setting,]

        self.aistant_chat_completion_req_status = OpenAIReqStatus.REQ_STATUS_IDLE

        self.thread_chat_completion_do_run = True
        self.thread_chat_completion = threading.Thread(target = self.chat_core_thread_exec)
        self.thread_chat_completion.start()
        
        self.core_threa_run_tick = 0
#======================================================================#
    #析构函数
    def __del__(self):
        print(" Aistant Aistant_Chat_Server del.")
        self.thread_chat_completion_do_run = False

# 调用 OPENAI API
    def aistant_openai_api_req_with_sys(self, sys_setting, prompt_in):
        # print(openai.api_key, ' ', self.aistant_current_model_name)
        try:
            aistant_chat_total_messages = [sys_setting,]
            user_question = {"role": "user", "content": ""}
            user_question['content'] = prompt_in
            aistant_chat_total_messages.append(user_question) # 新增 
            response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = aistant_chat_total_messages,
            temperature = 0.1
            )
            return response.choices[0]['message']['content']
            
        except:
            logging.info("aistant_editor_openai_api_req error")
            response = ''
            return response

    #仿照智能菜单的block_exec
    def aistant_auto_generate_title_exec(self):
        print("aistant_auto_generate_title_exec")
        chat_text = self.ui.textEdit_3.toPlainText()
        edit_text = self.ui.textEdit_2.toPlainText()
        total_text = '以下是聊天内容: ' + chat_text + '\n' + '以下是编辑器内容：' + '\n' + edit_text + '\n'
        sys_setting = {"role": "system", "content": "你是一个总结师，你可以总结出一句话来描述我提供给你的内容,但不要超过10字。我提供的内容包括两个部分，一是聊天内容，\
                       二是编辑器内容。如果聊天内容为空或者编辑器内容为空，那么对应的部分就不需要提供。你需要以‘聊天内容；编辑内容’的格式来回答我。"}
        output_text = self.aistant_openai_api_req_with_sys(sys_setting, total_text)
        print(output_text)
        return output_text
        
    def aistant_auto_generate_title_trig(self):
        print("aistant_auto_generate_title_trig")
        self.aistant_thread_auto_generate_title.start()


    def aistant_encrypt_toggle(self):
        if self.aistant_password_mode == True:
            self.ui.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.pushButton_11.setText('隐藏密钥')
            self.aistant_password_mode = False
        else:
            self.ui.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.pushButton_11.setText('显示密钥')
            self.aistant_password_mode = True

    def aistant_test_editor_change_font(self, font):
        print("aistant_test_editor_change_font: ", font)
        self.ui.textEdit_2.setCurrentFont(font)

    def aistant_test_editor_change_size(self, size):
        print("aistant_test_editor_change_size: ", size)
        self.ui.textEdit_2.setFontPointSize(size)
    
    def aistant_cursor_change_event(self):
        # print("aistant_cursor_change_event....")
        cursor = self.ui.textEdit_2.textCursor()
        if cursor.position() == 0 and cursor.hasSelection() == False:
            logging.info("光标回到了起点")
            self.ui.textEdit_2.setCurrentFont(self.ui.fontComboBox.currentFont())
            self.ui.textEdit_2.setFontPointSize(self.ui.spinBox.value())

    def aistant_format_change_event(self, format):
        logging.info("aistant_format_change_event")
        self.ui.textEdit_2.setCurrentFont(self.ui.fontComboBox.currentFont())
        self.ui.textEdit_2.setFontPointSize(self.ui.spinBox.value())

    def aistant_test_api_key_trig_exec(self):
        logging.info("aistant_test_api_key_trig_exec")
        self.test_api_key_val = self.ui.lineEdit_4.text()
        if self.test_api_key_val == '':
            self.ui.label_14.setText("密钥为空，请输入有效密钥")
            return
        self.ui.label_14.setText("密钥测试中...")
        self.aistant_test_key_count_thread.start()
        self.aistant_test_key_main_thread.start()

    def aistant_api_key_test_exec(self):
        self.test_exec_cnt = 0
        while True:
            time.sleep(0.2)
            print("aistant_api_key_test_exec: ", self.test_exec_cnt)
            if self.test_exec_cnt < 99:
                self.test_exec_cnt = self.test_exec_cnt + 1
            self.aistant_test_key_count_thread.signal_emit(self.test_exec_cnt)
            if self.aistant_api_key_test_status != 0:
                self.aistant_test_key_count_thread.signal_emit(100)
                self.test_exec_cnt = 0
                self.aistant_api_key_test_status = 0
                break

        print("aistant_api_key_test_exec done.")

    def aistant_api_key_test_block_exec(self):
        print("aistant_api_key_test_block_exec")
        ret = ''
        api_key_origin = openai.api_key 
        openai.api_key = self.test_api_key_val
        try:
            aistant_chat_total_messages = [{"role": "system", "content": "你是一名得力的助手"},]
            user_question = {"role": "user", "content": ""}
            user_question['content'] = '在吗'
            aistant_chat_total_messages.append(user_question) # 新增 
            response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = aistant_chat_total_messages
            )
            self.aistant_api_key_test_status = 1
            ret = '密钥测试ok'
            
        except:
            logging.info("aistant_editor_openai_api_req error")
            self.aistant_api_key_test_status = -1
            response = ''
            ret = '密钥测试失败'
        openai.api_key = api_key_origin
        return ret

    def aistant_api_key_test_update_progressbar(self, val):
        # print("aistant_api_key_test_update_progressbar: ", val)
        self.ui.progressBar.setValue(val)

    def aistant_update_and_save_key_exec(self):
        print("aistant_update_and_save_key_exec")
        self.aistant_openai_api_key = self.ui.lineEdit.text()
        if self.aistant_openai_api_key != '':
            openai.api_key = self.aistant_openai_api_key
            print("[Init]openai api key update: ", openai.api_key)
            self.aistant_setting.aistant_setting_set_cur_key_val(openai.api_key)
        else:
            logging.info("[Init]openai api key empty.")

    def aistant_chat_multi_talk_enable(self, state):
        if state:
            self.multi_chat_enable = True
        else:
            self.multi_chat_enable = False
        print("aistant_chat_multi_talk_enable: ",self.multi_chat_enable, state)
        self.aistant_setting.aistant_setting_set_multi_chat(self.multi_chat_enable)

    # def aistant_chat_req_and_update_combo_chat(self):
    #     print("aistant_chat_req_and_update_combo_chat")

    # def aistant_chat_req_and_update_combo_completion(self):
    #     print("aistant_chat_req_and_update_combo_completion")
    
    # def aistant_chat_req_and_update_combo_of_all_type(self):
    #     print("aistant_chat_req_and_update_combo. Type:", self.aistant_current_model_type)
    #     try:
    #         prompt_text = self.aistant_ui_get_input_textedit_exec()
    #         if prompt_text == '':
    #             self.aistant_chat_update_statusbar("发送消息为空")
    #             return ''
            
    #         user_question = {"role": "user", "content": ""}
    #         user_question['content'] = prompt_text
    #         print("chat_core_button_submit_exec--", prompt_text) 
    #         self.aistant_chat_history_messages.append(user_question) # 新增 

    #         if self.aistant_current_model_type == 'Chat':
    #             self.aistant_chat_req_and_update_combo_chat()

    #         elif self.aistant_current_model_type == 'Completion':
    #             self.aistant_chat_req_and_update_combo_completion()

    #         else: 
    #             print("aistant_chat_req_and_update_combo: None")
    #             self.statusbar_writer.write_signal.emit("错误的模型类型")
    #             return
    #     except Exception as e:
    #         print("aistant_chat_req_and_update_combo: ", e)
    #         self.statusbar_writer.write_signal.emit("请求错误")
    #         return
    
    def chat_core_thread_exec(self):
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
                print('-----response_content openai_chat_completion_api_re:', response_content)
                if response_content['role'] == 'system' or response_content['role'] == 'user' or response_content['role'] == 'assistant':
                    print("chat_core_thread_exec system or user or assistant")
                    self.aistant_chat_history_messages.append(self.aistant_latest_query_dict) # 新增 prompt
                    self.aistant_chat_history_messages.append(response_content) # 新增 completion
                self.aistant_chat_ui_output_update()
                self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)
                if response_content['role'] == 'error':
                    self.aistant_chat_update_statusbar(response_content['content'])

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
        err_response = {'role': 'error', 'content': ''}
        try:
            prompt_text = self.aistant_ui_get_input_textedit_exec()
            print("---prompt_text: %s"%prompt_text)
            # if prompt_text == '' or prompt_text == '\r' or prompt_text == '\n' or prompt_text == '\r\n':
            if prompt_text == '':
                # print("chat_core_button_submit_exec-Empty send prompt message.")
                self.aistant_chat_update_statusbar("发送消息为空")
                return err_response
            user_question = {"role": "user", "content": ""}
            user_question['content'] = prompt_text
            self.aistant_latest_query_dict = user_question
            if self.aistant_current_model_type == 'Chat':
                print("self.multi_chat_enable: ", self.multi_chat_enable, self.aistant_chat_stream_update_enable)
                if self.multi_chat_enable:
                    prompt_in_msg = self.aistant_chat_history_messages.copy()
                    prompt_in_msg.append(user_question)
                else:
                    prompt_in_msg = []
                    prompt_in_msg.append(self.aistant_role_setting)
                    prompt_in_msg.append(user_question)
                
                if self.aistant_chat_stream_update_enable == True:
                    response_dict = {'role': 'assistant', 'content': ''}
                    response_content = ''
                    response_chunk = openai.ChatCompletion.create(
                    model = self.aistant_current_model_name,
                    messages = prompt_in_msg,
                    temperature = 0.1,
                    stream = True
                    )
                    msg_role_with_content = '-chatGPT' + ':\n'
                    self.chat_textedit_streamer.write_signal.emit(msg_role_with_content)

                    try:
                        for chunk in response_chunk:
                            chunk_message = chunk['choices'][0]['delta']  # extract the message
                            chat_sin_msg = chunk_message.get('content', '')
                            response_content+=chat_sin_msg
                            self.chat_textedit_streamer.write_signal.emit(chat_sin_msg)
                            if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE:
                                break
                        prompt_in_msg = None
                        response_dict['content'] = response_content
                    except Exception as e:
                        print("openai_chat_completion pass: ", e)
                        pass
                    return response_dict
                else:
                    response = openai.ChatCompletion.create(
                    model = self.aistant_current_model_name,
                    messages = prompt_in_msg,
                    temperature = 0.1
                    )
                    prompt_in_msg = None
                    return response.choices[0]['message']
            elif self.aistant_current_model_type == 'Complete':
                logging.info("openai chat completion api req.Text Complete request.")
                prompt_in = prompt_text + '\n'
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
                logging.info("openai chat completion api req.unknow model type.")
                return err_response

        except Exception as e:
            print("openai_chat_completion_api_req-Exception:", e)
            err_response['content'] = "Exception: " + str(e)
            return err_response

# 更新输出文本
    def aistant_chat_ui_output_update(self):
        message_content_total = ''
        msg_cnt = 0
        #清空 self.aistant_chat_output_content
        self.aistant_chat_output_content_key_value = []
        is_msg_role_with_content_empty = True
        for msg in self.aistant_chat_history_messages:
            msg_cnt = msg_cnt + 1
            if self.aistant_current_model_type == 'Chat':
                role_msg = 'Unknown'
                if msg_cnt == 1:
                    role_msg = '-user(system setting)'           
                if msg['role'] == 'user':
                    role_msg = '-user'
                elif msg['role'] == 'assistant':
                    role_msg = '-chatGPT'
                elif msg['role'] == 'error':
                    role_msg = '-error'
                msg_role_with_content = role_msg + ':\n' + msg['content']
                message_content_total += msg_role_with_content
                is_msg_role_with_content_empty = False
            elif self.aistant_current_model_type == 'Complete':
                if isinstance(msg, dict) and msg['role'] == 'user':
                    msg_role_with_content = 'user' + ':\n' + msg['content']
                elif isinstance(msg, dict):
                    continue
                else:
                    msg_role_with_content = self.aistant_current_model_name + ':' + msg
                message_content_total += msg_role_with_content
                is_msg_role_with_content_empty = False  
            
            if is_msg_role_with_content_empty == False:
                tmp_output_content_key_value = {'msg_output': '', 'msg_origin': ''}
                tmp_output_content_key_value['msg_output'] = msg_role_with_content
                tmp_output_content_key_value['msg_origin'] = msg
                self.aistant_chat_output_content_key_value.append(tmp_output_content_key_value)
            
            # 统一换行
            message_content_total += self.aistant_chat_output_divider
        
        # 最终文本输出到面板
        self.aistant_ui_display_txt_output_emit(message_content_total)

    def aistant_reset_submit_exec(self):
        print("aistant_reset_submit_exec")
        self.ui.textEdit.clear()

    def aistant_chat_textedit_set_txt(self, txt_out):
        # self.ui.textEdit.clear()
        self.ui.textEdit_3.setText(txt_out)
        # self.ui.textEdit_3.setLineWrapMode(QtWidgets.QTextEdit.FixedPixelWidth)
        textedit_bar = self.ui.textEdit_3.verticalScrollBar()
        textedit_bar.setValue(textedit_bar.maximum())
        print("aistant_chat_textedit_set_txt: ", textedit_bar.maximum())

    def aistant_chat_update_statusbar(self, content):
        self.aistant_ui_update_statusbar_txt(content)

    def aistant_chat_textedit_stream_update(self, content):
        cursor = self.ui.textEdit_3.textCursor()
        cursor.setPosition(len(self.ui.textEdit_3.toPlainText()))
        cursor.insertText(content)
        cursor.setPosition(len(self.ui.textEdit_3.toPlainText()))
        self.ui.textEdit_3.setTextCursor(cursor)

#callback release
# 发送消息
    def chat_core_button_submit_exec(self):
        if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE or self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_TIMEOUT:
            self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_EXEC)

    def chat_core_button_clear_exec(self):
        logging.info("chat core button clear.")
        # self.aistant_role_whole_content = self.role_brief_txt + self.role_custom_txt
        # self.aistant_role_setting = {"role": "system", "content": self.aistant_role_whole_content}
        self.aistant_chat_history_messages = [self.aistant_role_setting,]
        self.aistant_chat_ui_output_update()

    def chat_core_button_cancel_exec(self):
        logging.info("chat core button cancel.")
        self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

    def chat_core_button_save_exec(self):
        logging.info("chat core button save.")
        self.aistant_ui_save_current_chat_exec()

    def chat_core_button_withdraw_exec(self):
        logging.info("set chat core withdraw.")
        if len(self.aistant_chat_history_messages) > 2:
            del self.aistant_chat_history_messages[-1]
            del self.aistant_chat_history_messages[-1]
            self.aistant_chat_ui_output_update()

    def chat_core_teminate_thread_exec(self):
        self.thread_chat_completion_do_run = False

#========================================================================#

#-----对话和编辑窗口开关回调-----#
#将不存在的widget注释
#"仅写"回调
    def aistant_editor_only_exec(self):
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
        self.ui.textEdit_2.setVisible(False)
        self.ui.toolBar_2.setVisible(False)
        self.ui.fontComboBox.setVisible(False)
        self.ui.spinBox.setVisible(False)

    def aistant_show_edit_window_widgets(self):
        self.ui.textEdit_2.setVisible(True)
        self.ui.toolBar_2.setVisible(True)
        self.ui.fontComboBox.setVisible(True)
        self.ui.spinBox.setVisible(True)

    def aistant_hide_chat_window_widgets(self):
        self.ui.textEdit.setVisible(False)
        self.ui.textEdit_3.setVisible(False)
        self.ui.pushButton_4.setVisible(False)
        self.ui.pushButton_5.setVisible(False)
        # self.ui.groupBox_2.setVisible(False)
        # self.ui.scrollArea.setVisible(False)
        self.ui.pushButton.setVisible(False)
        self.ui.pushButton_6.setVisible(False)
        self.ui.pushButton_7.setVisible(False)
        self.ui.pushButton_14.setVisible(False)
        self.ui.pushButton_15.setVisible(False)
        self.ui.pushButton_16.setVisible(False)
        self.ui.pushButton_17.setVisible(False)

    def aistant_show_chat_window_widgets(self):
        self.ui.textEdit.setVisible(True)
        self.ui.textEdit_3.setVisible(True)
        self.ui.pushButton_4.setVisible(True)
        self.ui.pushButton_5.setVisible(True)
        # self.ui.groupBox_2.setVisible(True)
        # self.ui.scrollArea.setVisible(True)
        self.ui.pushButton.setVisible(True)
        self.ui.pushButton_6.setVisible(True)
        self.ui.pushButton_7.setVisible(True)
        self.ui.pushButton_14.setVisible(True)
        self.ui.pushButton_15.setVisible(True)
        self.ui.pushButton_16.setVisible(True)
        self.ui.pushButton_17.setVisible(True)

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

    def action_chat_help_exec(self):
        print("action_chat_help_exec")
        self.ui.stackedWidget.setCurrentIndex(1)

    def aistant_ui_get_textEdit_input_text(self):
        print("aistant_ui_get_textEdit", self.ui.textEdit.toPlainText())
        return self.ui.textEdit.toPlainText()

#创建一个新的进程
    def create_new_mainwindow_exec(self):
        print("create_new_mainwindow_exec")
        new_app = QtWidgets.QApplication(sys.argv)
        new_aistant_ui = Aistant_UI_Agent()
        new_aistant_ui.Aistant_UI_show()
        self.new_app_list.append(new_app)

        # self.new_main_win = QtWidgets.QMainWindow()
        # ui = Aistant_UI.Ui_MainWindow()
        # ui.setupUi(self.new_main_win)
        
        # self.new_main_win.show()


# 恢复默认设置
    def aistant_ui_recover_default_setting(self):
        print("aistant_ui_recover_default_setting")
        self.aistant_setting.aistant_recover_with_default_setting()
        self.ui.statusbar.showMessage("恢复默认设置成功, 重启软件生效！")


    def aistant_ui_activate_button(self):
        self.ui.pushButton_4.clicked.connect(self.chat_core_button_submit_exec)
        # self.ui.pushButton_4.setShortcut("Ctrl+A")
        self.ui.pushButton_7.clicked.connect(self.chat_core_button_clear_exec)
        self.ui.pushButton_5.clicked.connect(self.chat_core_button_cancel_exec)
        self.ui.pushButton_6.clicked.connect(self.chat_core_button_save_exec)
        self.ui.pushButton.clicked.connect(self.chat_core_button_withdraw_exec)

        self.ui.pushButton_2.clicked.connect(self.aistant_ui_recover_default_setting)

        self.ui.pushButton_12.clicked.connect(self.aistant_save_role_custom_exec)
        self.ui.pushButton_14.clicked.connect(self.aistant_ui_load_current_chat_exec)
        self.ui.pushButton_15.clicked.connect(self.aistant_reset_submit_exec)

        self.ui.pushButton_16.clicked.connect(self.aistant_ui_new_chat_file_save_exec)
        self.ui.pushButton_17.clicked.connect(self.aistant_ui_sync_chat_modify_exec)

    def Aistant_UI_show(self):
        self.mainwin.show()

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
        self.mainwin.close()
        # if self.app != None:
        #     self.app.quit()

# 更新模型回调
    def aistant_change_model_exec(self, model_idx):
        # 更新model最新idx, 名称和类型
        self.aistant_current_model_idx = self.ui.comboBox_4.currentIndex()
        self.aistant_current_model_name = self.aistant_model_list[self.aistant_current_model_idx]['model']
        self.aistant_current_model_type = self.aistant_model_list[self.aistant_current_model_idx]['type']
        print("aistant_change_model_exec: ", self.aistant_current_model_idx, ' ',self.aistant_current_model_name, ' ',self.aistant_current_model_type)
        self.aistant_chat_history_messages = [self.aistant_role_setting,]
        self.aistant_setting.aistant_setting_set_model_id(self.aistant_current_model_idx)

# 更新角色回调
    def aistant_change_role_exec(self, role_idx):
        print("aistant update role descript", role_idx)
       # 更新token中role的content
        self.aistant_role_content_update()
        # 更新历史信息
        if len(self.aistant_chat_history_messages) >= 1:
            self.aistant_chat_history_messages[0] = self.aistant_role_setting
        # 更新问答输出面板
        self.aistant_chat_ui_output_update()
        # 更新配置文件
        self.aistant_setting.aistant_setting_set_role_id(role_idx)

# 保存'自定义'角色回调
    def aistant_save_role_custom_exec(self):
        logging.info("aistant_save_role_custom_exec")
        self.aistant_role_content_update()
        # 更新历史信息
        if len(self.aistant_chat_history_messages) >= 1:
            self.aistant_chat_history_messages[0] = self.aistant_role_setting
        # 更新问答输出面板
        self.aistant_chat_ui_output_update()

    def aistant_role_content_update(self):
        self.current_role_descript_idx = self.ui.comboBox_3.currentIndex()
        # self.role_name = self.aistant_setting.aistant_select_role_and_descript_get_config()[self.current_role_descript_idx]['role']
        self.role_brief_txt = self.aistant_setting.aistant_select_role_and_descript_get_config()[self.current_role_descript_idx]['brief']
        self.role_custom_txt = self.ui.plainTextEdit.toPlainText()
        if self.role_brief_txt != '自定义':
            self.aistant_role_whole_content = self.role_brief_txt
            print(self.role_brief_txt)
        else:
            self.aistant_role_whole_content = self.role_custom_txt
        self.aistant_role_setting = {"role": "system", "content": self.aistant_role_whole_content}

# ------editor 
    def aistant_editor_open_exec(self):
        logging.info("aistant_editor_open_exec")
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self.ui.stackedWidget, 'Open File',".","(*.txt)")[0]

        if self.filename:
            with open(self.filename,"rt") as file:
                self.ui.textEdit_2.setText(file.read())
    
    def aistant_editor_save_exec(self):
        logging.info("aistant_editor_save_exec")
        # Only open dialog if there is no filename yet
        #PYQT5 Returns a tuple in PyQt5, we only need the filename
        # if not self.filename:
        self.filename = QtWidgets.QFileDialog.getSaveFileName(self.ui.stackedWidget, 'Save File')[0]

        if self.filename:
            
            # Append extension if not there yet
            if not self.filename.endswith(".txt"):
              self.filename += ".txt"
            # if not self.filename.endswith(".txt"):
            #       self.filename += ".txt"

            # We just store the contents of the text file along with the
            # format in html, which Qt does in a very nice way for us
            with open(self.filename,"wt") as file:
                # file.write(self.ui.textEdit_2.toHtml())
                file.write(self.ui.textEdit_2.toPlainText())

            self.aistant_editor_changesSaved = True

    def aistant_editor_find_exec(self):
        logging.info("aistant_editor_find_exec")
        Aistant_editor_find.Find(self.ui.textEdit_2).show()

# 编辑器智能菜单
    def aistant_init_smart_menu(self):
        # 创建快捷键和弹出菜单
        self.aistant_s_menu_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F1), self.ui.textEdit_2)
        # self.aistant_s_menu_shortcut = QtWidgets.QShortcut('Ctrl+Space', self.ui.textEdit_2)
        self.aistant_s_menu_shortcut.activated.connect(self.aistant_show_smart_menu)
        self.aistant_s_menu_shortcut.setContext
        self.aistant_smart_menu = QtWidgets.QMenu(self.ui.textEdit_2)
        self.aistant_smart_action_query = QtWidgets.QAction('询问', self.ui.textEdit_2)
        self.aistant_smart_action_summarize = QtWidgets.QAction('总结', self.ui.textEdit_2)
        self.aistant_smart_action_explain = QtWidgets.QAction('解释', self.ui.textEdit_2)
        self.aistant_smart_action_continue = QtWidgets.QAction('续写', self.ui.textEdit_2)
        self.aistant_smart_action_improve = QtWidgets.QAction('改进', self.ui.textEdit_2)
        #增加中英互译选项
        self.aistant_smart_action_translate = QtWidgets.QAction('翻译', self.ui.textEdit_2)

        self.aistant_smart_menu.addAction(self.aistant_smart_action_query)
        self.aistant_smart_menu.addAction(self.aistant_smart_action_summarize)
        self.aistant_smart_menu.addAction(self.aistant_smart_action_explain)
        self.aistant_smart_menu.addAction(self.aistant_smart_action_continue)
        self.aistant_smart_menu.addAction(self.aistant_smart_action_improve)
        self.aistant_smart_menu.addAction(self.aistant_smart_action_translate)
        # 菜单选项链接回调
        self.aistant_smart_menu.setEnabled(True)

        self.aistant_smart_line_edit = QtWidgets.QLineEdit(self.ui.page)
        self.aistant_smart_line_edit.hide()
        self.aistant_smart_line_edit.returnPressed.connect(self.aistant_smart_line_return_exec)

        # openai后台线程
        self.aistant_query_thread = AistantThread(self.aistant_smart_query_block_exec)
        self.aistant_query_thread.signal.connect(self.aistant_smart_query_update_ui_text)

        self.aistant_summarize_thread = AistantThread(self.aistant_smart_summarize_block_exec)
        self.aistant_summarize_thread.signal.connect(self.aistant_smart_summarize_update_ui_text)

        #基于上面的定义进行仿写
        self.aistant_explain_thread = AistantThread(self.aistant_smart_explain_block_exec)
        self.aistant_explain_thread.signal.connect(self.aistant_smart_explain_update_ui_text)

        self.aistant_continue_thread = AistantThread(self.aistant_smart_continue_block_exec)
        self.aistant_continue_thread.signal.connect(self.aistant_smart_continue_update_ui_text)

        self.aistant_improve_thread = AistantThread(self.aistant_smart_improve_block_exec)
        self.aistant_improve_thread.signal.connect(self.aistant_smart_improve_update_ui_text)

        #增加中英互译线程
        self.aistant_translate_thread = AistantThread(self.aistant_smart_translate_block_exec)
        self.aistant_translate_thread.signal.connect(self.aistant_smart_translate_update_ui_text)

        # self.aistant_stream_signal = pyqtSignal(str)
        # self.aistant_stream_signal.connect(self.aistant_smart_stream_display_exec)

        self.aistant_editor_writer = Writer()
        self.aistant_editor_writer.write_signal.connect(self.aistant_smart_stream_display_exec)

        #Aition触发回调询问
        self.aistant_smart_action_query.triggered.connect(self.aistant_smart_query_trig)
        self.aistant_smart_action_summarize.triggered.connect(self.aistant_smart_summarize_trig)

        self.aistant_smart_action_explain.triggered.connect(self.aistant_smart_explain_trig)
        self.aistant_smart_action_continue.triggered.connect(self.aistant_smart_continue_trig)
        self.aistant_smart_action_improve.triggered.connect(self.aistant_smart_improve_trig)

        self.aistant_smart_action_translate.triggered.connect(self.aistant_smart_translate_trig)
# 弹出智能菜单
    def aistant_show_smart_menu(self):
        # 显示弹出菜单
        # TODO: 前置触发条件，其他条件下直接过滤
        cursor_x = self.ui.textEdit_2.cursorRect().left()
        cursor_y = self.ui.textEdit_2.cursorRect().bottom()
        cursor_position = self.ui.textEdit_2.mapToGlobal(QtCore.QPoint(cursor_x, cursor_y))
        self.aistant_smart_menu.exec_(cursor_position)

# 智能菜单->询问
    # 更新界面
    def aistant_smart_query_update_ui_text(self, content):
        print("aistant_smart_query_update_ui_text.")
        self.ui.textEdit_2.append(content)

    def aistant_smart_summarize_update_ui_text(self, content):
        print("aistant_smart_summarize_update_ui_text.")
        self.ui.textEdit_2.append(content)

    def aistant_smart_explain_update_ui_text(self, content):
        print("aistant_smart_explain_update_ui_text.")
        self.ui.textEdit_2.append(content)

    def aistant_smart_continue_update_ui_text(self, content):
        print("aistant_smart_continue_update_ui_text.")
        self.ui.textEdit_2.append(content)

    def aistant_smart_improve_update_ui_text(self, content):
        print("aistant_smart_improve_update_ui_text.")
        self.ui.textEdit_2.append(content)

    def aistant_smart_translate_update_ui_text(self, content):
        print("aistant_smart_translate_update_ui_text.")
        self.ui.textEdit_2.append(content)
    
    def aistant_smart_stream_display_exec(self, content):
        cursor = self.ui.textEdit_2.textCursor()
        cursor.setPosition(len(self.ui.textEdit_2.toPlainText()))
        cursor.insertText(content)
        cursor.setPosition(len(self.ui.textEdit_2.toPlainText()))
        self.ui.textEdit_2.setTextCursor(cursor)
        # self.ui.textEdit_2.insertPlainText(content)

    # 阻塞部分询问
    # 智能询问
    def aistant_smart_query_trig(self):
        self.aistant_query_thread.start()

    def aistant_smart_query_block_exec(self):
        cursor = self.ui.textEdit_2.textCursor()
        selected_text = cursor.selectedText()
        selected_text = selected_text + '\n' + '请对以上内容进行回答。'
        print("aistant_smart_query_block_exec in:", selected_text)
        out_text = self.aistant_stream_openai_api_req('query', selected_text)
        print("aistant_smart_query_block_exec out.")
        return out_text

    # 智能总结
    def aistant_smart_summarize_trig(self):
        self.aistant_summarize_thread.start()

    def aistant_smart_summarize_block_exec(self):
        cursor = self.ui.textEdit_2.textCursor()
        selected_text = cursor.selectedText()
        selected_text = selected_text + '\n' + '请对以上内容进行总结。'
        print("aistant_smart_summarize_block_exec in:", selected_text)
        out_text = self.aistant_stream_openai_api_req('other', selected_text)
        print("aistant_smart_summarize_block_exec out.")
        return out_text
    
    # 智能解释
    def aistant_smart_explain_trig(self):
        self.aistant_explain_thread.start()

    def aistant_smart_explain_block_exec(self):
        cursor = self.ui.textEdit_2.textCursor()
        selected_text = cursor.selectedText()
        selected_text = selected_text + '\n' + '请对以上内容进行解释。'
        print("aistant_smart_explain_block_exec in:", selected_text)
        out_text = self.aistant_stream_openai_api_req('other', selected_text)
        print("aistant_smart_explain_block_exec out.")
        return out_text
    
    # 智能续写
    def aistant_smart_continue_trig(self):
        self.aistant_continue_thread.start()
    
    def aistant_smart_continue_block_exec(self):
        cursor = self.ui.textEdit_2.textCursor()
        selected_text = cursor.selectedText()
        selected_text = selected_text + '\n' + '请续写以上内容。'
        print("aistant_smart_continue_block_exec in:", selected_text)
        out_text = self.aistant_stream_openai_api_req('other', selected_text)
        print("aistant_smart_continue_block_exec out.")
        return out_text
    
    # 智能改进
    def aistant_smart_improve_trig(self):
        self.aistant_improve_thread.start()
        # print("aistant_smart_improve_trig in.")
        # cursor = self.ui.textEdit_2.textCursor()
        # selected_text = cursor.selectedText()
        # selected_text = selected_text + '\n' + '请对以上内容进行改进。'
        # print("aistant_smart_improve_block_exec in:", selected_text)
        # self.aistant_stream_openai_api_req('other', selected_text)

    def aistant_smart_improve_block_exec(self):
        cursor = self.ui.textEdit_2.textCursor()
        selected_text = cursor.selectedText()
        selected_text = selected_text + '\n' + '请对以上内容进行改进。'
        print("aistant_smart_improve_block_exec in:", selected_text)
        # out_text = self.aistant_editor_openai_api_req('other', selected_text)
        out_text = self.aistant_stream_openai_api_req('other', selected_text)
        print("aistant_smart_improve_block_exec out.") 
        return out_text
    
    def aistant_smart_translate_block_exec(self):
        cursor = self.ui.textEdit_2.textCursor()
        selected_text = cursor.selectedText()
        selected_text = selected_text + '\n'
        print("aistant_smart_translate_block_exec in:", selected_text)
        out_text = self.aistant_stream_openai_api_req('translate', selected_text)
        print("aistant_smart_translate_block_exec out.")
        return out_text

    def aistant_smart_translate_trig(self):
        self.aistant_translate_thread.start()

    # def aistant_response_append_to_textedit(self):
    #     for chunk in self.editor_req_stream_res:
    #         chunk_message = chunk['choices'][0]['delta']
    #         single_msg = chunk_message.get('content', '')
    #         print('111111....----:   ',single_msg)
    #         self.ui.textEdit_2.append(single_msg)
    #         self.timer_count = self.timer_count + 1
    #         if self.timer_count == 2:
    #             self.timer.stop()
    #             self.timer_count = 0
    #             self.editor_req_stream_res = []
    #             self.chat_stream_res_len = 0
    #             print('timer stoped.')

    def aistant_stream_openai_api_req(self, requester, prompt_in):
        # print(openai.api_key, ' ', self.aistant_current_model_name)
        print("aistant_stream_openai_api_req in.")
        self.statusbar_writer.write_signal.emit('智能编辑正在请求中...')
        try:
            # response = openai.Completion.create(
            # model = self.aistant_editor_ai_model,
            # # model = 'curie',
            # prompt = prompt_in,
            # temperature=0.7,
            # max_tokens=1000,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0
            # )
            # return response.choices[0]["text"]

            # time.sleep(0.1)
            if requester == 'query':
                aistant_chat_total_messages = [{"role": "system", "content": "你是一名得力的助手。"},]
            elif requester == 'translate':
                aistant_chat_total_messages = [{"role": "system", "content": "你是一名翻译专家。请翻译我之后提供给你的内容。如果内容是英文，请翻译成中文；如果内容是中文，请翻译成英文。另外，请只输出翻译结果。"},]
            else:
                aistant_chat_total_messages = [{"role": "system", "content": "你是一位文案编辑或文案优化专家。我将会向你提供各种文本,并在最后向你提出'回答''总结''改进''解释''续写'等方面的要求，你需要以文本内容为基础，结合我的请求，对文本内容进行相关的操作。"},]
            user_question = {"role": "user", "content": ""}
            user_question['content'] = prompt_in
            aistant_chat_total_messages.append(user_question) # 新增 
            print('before openai.ChatCompletion.create')
            self.editor_req_stream_res = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = aistant_chat_total_messages,
            temperature = 0.1,
            stream=True
            )
            self.aistant_editor_writer.write_signal.emit('\n')

            try:
                for chunk in self.editor_req_stream_res:
                    chunk_message = chunk['choices'][0]['delta']  # extract the message
                    single_msg = chunk_message.get('content', '')
                    # self.aistant_improve_thread.signal.emit(single_msg)
                    self.aistant_editor_writer.write_signal.emit(single_msg)
                    print(single_msg)
            except Exception as e:
                pass
            #-----------------------------------#
            # # iterate through the stream of events
            # for chunk in self.editor_req_stream_res:
            #     chunk_message = chunk['choices'][0]['delta']  # extract the message
            #     single_msg = chunk_message.get('content', '')
            #     self.ui.textEdit_2.insertPlainText(single_msg)
            #     # cursor = self.ui.textEdit_2.textCursor()
            #     # cursor.setPosition(len(self.ui.textEdit_2.toPlainText()))
            #     # cursor.insertText(single_msg)
            #     # cursor.setPosition(len(self.ui.textEdit_2.toPlainText()))
            #     # self.ui.textEdit_2.setTextCursor(cursor)
            #     print('single_msg----:   ', single_msg)           
            #-----------------------------------#
            # from PyQt5.QtCore import QTimer
            # # self.chat_stream_res_len = len(self.editor_req_stream_res)
            # # print('self.chat_stream_res_len: ', self.chat_stream_res_len)
            # self.timer = QTimer()
            # self.timer.timeout.connect(self.aistant_response_append_to_textedit)
            # self.timer.start(1000)
            # self.timer_count = 0
            self.statusbar_writer.write_signal.emit('智能编辑完成。')
            return ''
            
        except Exception as e:
            logging.info("aistant_editor_openai_api_req error")
            print("aistant_editor_openai_api_req error", e)
            self.statusbar_writer.write_signal.emit('智能编辑请求异常，请重试。')
            return ''

# 调用 OPENAI API
    def aistant_editor_openai_api_req(self, requester, prompt_in):
        # print(openai.api_key, ' ', self.aistant_current_model_name)
        try:
            # response = openai.Completion.create(
            # model = self.aistant_editor_ai_model,
            # # model = 'curie',
            # prompt = prompt_in,
            # temperature=0.7,
            # max_tokens=1000,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0
            # )
            # return response.choices[0]["text"]

            # time.sleep(0.1)
            if requester == 'query':
                aistant_chat_total_messages = [{"role": "system", "content": "你是一名得力的助手。"},]
            else:
                aistant_chat_total_messages = [{"role": "system", "content": "你是一位文案编辑或文案优化专家。我将会向你提供各种文本,并在最后向你提出'回答''总结''改进''解释''续写'等方面的要求，你需要以文本内容为基础，结合我的请求，对文本内容进行相关的操作。"},]
            user_question = {"role": "user", "content": ""}
            user_question['content'] = prompt_in
            aistant_chat_total_messages.append(user_question) # 新增 
            response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = aistant_chat_total_messages,
            temperature = 0.1
            )
            return response.choices[0]['message']['content']
            
        except:
            logging.info("aistant_editor_openai_api_req error")
            response = ''
            return response

# 编辑行弹出回调
    def aistant_show_smart_line(self):
        print("aistant_show_smart_lineedit")
        cursor_x = self.ui.textEdit_2.cursorRect().left()
        cursor_y = self.ui.textEdit_2.cursorRect().bottom()
        cursor_position = self.ui.textEdit_2.mapToGlobal(QtCore.QPoint(cursor_x, cursor_y))
        
        self.aistant_smart_line_edit.move(cursor_position)
        self.aistant_smart_line_edit.show()
        # print("aistant_show_smart_lineedit---")
        # self.ui.lineEdit_3.move(cursor_position.x(), cursor_position.y())

# 编辑行回车隐藏回调
    def aistant_smart_line_return_exec(self):
        print("aistant_smart_line_return_exec")
        self.aistant_smart_line_edit.hide()
# ------------------------------------------------------------------------ #
# callback release
    def aistant_ui_get_input_textedit_exec(self):
        return self.ui.textEdit.toPlainText()

    def aistant_ui_display_txt_output_emit(self, txt_display):
        # self.ui.textEdit_3.setText(txt_display)
        # html = markdown.markdown(txt_display)
        self.chat_textedit_writer.write_to_display_widget(txt_display)

    def aistant_ui_update_statusbar_txt(self, txt_display):
        self.statusbar_writer.write_to_display_widget(txt_display)

    def aistant_ui_sync_chat_modify_exec(self):
        print("aistant_ui_sync_chat_modify_exec")
        self.statusbar_writer.write_signal.emit('同步对话编辑中...')
        current_textedit_plaintext = self.ui.textEdit_3.toPlainText()
        #将current_textedit_plaintext基于 self.aistant_chat_output_divider 分割，并构建一个list
        try:
            current_textedit_plaintext_list = current_textedit_plaintext.split(self.aistant_chat_output_divider)
            print("current_textedit_plaintext_list len: ", len(current_textedit_plaintext_list), 
                  'len of kv: ', len(self.aistant_chat_output_content_key_value))
            #轮询current_textedit_plaintext_list，并在self.aistant_chat_output_content_key_value 逐条同步
            chat_sync_count = 0
            self.aistant_chat_history_messages = []
            for single_chat in current_textedit_plaintext_list:
                # print("single_chat: ", single_chat)
                # print("single_chat len: ", len(single_chat))
                tmp_single_his_origin = self.aistant_chat_output_content_key_value[chat_sync_count]['msg_origin']
                if single_chat != self.aistant_chat_output_content_key_value[chat_sync_count]['msg_output']:
                    tmp_single_his_origin['content'] = single_chat
                self.aistant_chat_history_messages.append(tmp_single_his_origin)
                chat_sync_count += 1
                if chat_sync_count == len(self.aistant_chat_output_content_key_value):
                    break
            self.aistant_chat_ui_output_update()
            self.statusbar_writer.write_signal.emit('同步对话编辑完成。')
            # print("current_textedit_plaintext_list: ", current_textedit_plaintext_list)
            # print("current_textedit_plaintext_list len: ", len(current_textedit_plaintext_list))
        except Exception as e:
            print("aistant_ui_sync_chat_modify_exec error", e)
            self.statusbar_writer.write_signal.emit('同步编辑内容失败，请勿修改分隔符。')
            return
        # print('aistant_ui_sync_chat_modify_exec success', self.aistant_chat_history_messages)

    # 另存对话
    def aistant_ui_new_chat_file_save_exec(self):
        print("aistant_ui_new_chat_file_save_exec")
        filename, _ = QFileDialog.getSaveFileName(self.ui.stackedWidget, "保存对话", "", "文本文件 (*.txt);;所有文件 (*)")
        print("local_save_file_path new: ", filename)
        if filename == '':
            print("save_conversation_name_input no file")
            return
        if filename:
            with open(filename, "w") as file:
                save_text = 'Aistant '+ 'model: ' + self.aistant_current_model_name + '\n' + self.ui.textEdit_3.toPlainText()
                save_text = save_text + '\n' + '----------Aistant Origin----------' + '\n'
                file.write(save_text)
                # 将  self.aistant_chat_history_messages 转换为str，并且显示汉字
                
                #TypeError: dump() missing 1 required positional argument: 'fp'
                #TypeError: write() argument must be str, not bytes
                json.dump(self.aistant_chat_history_messages, file)
                self.statusbar_writer.write_signal.emit('对话已保存。')

    # 保存对话
    def aistant_ui_save_current_chat_exec(self):
        print("aistant_ui_save_current_chat_exec")
        local_save_file_path = ''
        if self.aistant_current_chat_file_path != '':
            local_save_file_path = self.aistant_current_chat_file_path
            print("local_save_file_path exist")
        else:
            local_save_file_path, _ = QFileDialog.getSaveFileName(self.ui.stackedWidget, "保存对话", "", "文本文件 (*.txt);;所有文件 (*)")
            print("local_save_file_path new: ", local_save_file_path)
        filename = local_save_file_path
        if filename == '':
            print("save_conversation_name_input no file")
            return
        if filename:
            with open(filename, "w") as file:
                save_text = 'Aistant '+ 'model: ' + self.aistant_current_model_name + '\n' + self.ui.textEdit_3.toPlainText()
                save_text = save_text + '\n' + '----------Aistant Origin----------' + '\n'
                file.write(save_text)
                # 将  self.aistant_chat_history_messages 转换为str，并且显示汉字
                
                #TypeError: dump() missing 1 required positional argument: 'fp'
                #TypeError: write() argument must be str, not bytes
                json.dump(self.aistant_chat_history_messages, file)
                self.aistant_current_chat_file_path = filename
                self.statusbar_writer.write_signal.emit('对话已保存。')
                
    #加载对话
    def aistant_ui_load_current_chat_exec(self):
        print("aistant_ui_load_current_chat_exec")
        filename, _ = QFileDialog.getOpenFileName(self.ui.stackedWidget, "加载对话", "", "文本文件 (*.txt);;所有文件 (*)")
        if filename == '':
            print("load_conversation_name_input no file")
            return
        if filename:
            with open(filename, "r") as file:
                file_content = file.read() 
                #检查file_content是否以 Aistant model 开头
                if not file_content.startswith('Aistant model: '):
                    print("load_conversation_name_input not Aistant model:")
                    #通知statusbar
                    self.aistant_ui_update_statusbar_txt("加载对话失败，文件格式不正确(只支持gpt-3.5-turbo或gpt-3.5-turbo-0301)")
                    return
                #获取第1行中 'Aistant model: '之后的内容
                model_name = file_content.split('Aistant model: ', 1)[1].split('\n', 1)[0]
                print('model_name:::' + model_name)
                #获取 self.aistant_model_list 中的model_name对应的model_id
                model_id = self.aistant_setting.aistant_chat_model_dict_get_idx_by_model(model_name)
                if model_id == None:
                    print("load_conversation_name_input model_name not found")
                    #通知statusbar
                    self.aistant_ui_update_statusbar_txt("加载对话失败，模型异常")
                    return
                self.aistant_current_model_idx = model_id
                self.aistant_current_model_name = self.aistant_model_list[self.aistant_current_model_idx]['model']
                self.aistant_current_model_type = self.aistant_model_list[self.aistant_current_model_idx]['type']
                # print('model_id:::' + model_id)
                print(self.aistant_current_model_name, self.aistant_current_model_type)
                try:
                    #提取 ----------Aistant Origin---------- 之后的内容,赋值给 str1
                    str_load = file_content.split('----------Aistant Origin----------\n', 1)[1]
                    # print("sss:::" + str_load)
                    load_dict = json.loads(str_load)
                    self.aistant_chat_history_messages = load_dict
                    self.aistant_chat_ui_output_update()
                    self.aistant_current_chat_file_path = filename
                    print("aistant_current_chat_file_path:::" + self.aistant_current_chat_file_path)     
                except:
                    print('load origin content exception')
                    self.aistant_ui_update_statusbar_txt("加载对话失败，文件格式异常")
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
    app = QtWidgets.QApplication(sys.argv)
    aistant_ui = Aistant_UI_Agent()
    aistant_ui.Aistant_UI_show()
    print("after Aistant_UI_show")
    # #如果aistant_ui中的new_app存在，就调用quit()方法
    # if hasattr(aistant_ui, 'new_app'):
    #     aistant_ui.new_app.quit()
    sys.exit(app.exec_())