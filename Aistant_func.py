
import openai
from enum import Enum
import threading
import time
import keyboard

class OpenAIReqStatus(Enum):
   REQ_STATUS_IDLE = 0
   REQ_STATUS_EXEC = 1
   REQ_STATUS_TIMEOUT = 2
class Aistant_Chat_Core():
    def __init__(self):
        print(" Aistant Aistant_Chat_Core init.")
        self.aistant_chat_model_name = "gpt-3.5-turbo"
        self.aistant_role_setting = {"role": "system", "content": "你是一个得力的助手, 你叫chatgpt, 你是基于GPT3.5开发的"}
        self.aistant_history_messages = [self.aistant_role_setting,]

        self.aistant_chat_completion_req_status = OpenAIReqStatus.REQ_STATUS_IDLE

        self.thread_chat_completion_do_run = True
        self.thread_chat_completion = threading.Thread(target = self.chat_core_thread_exec)
        self.thread_chat_completion.start()
        
        self.core_threa_run_tick = 0

    def openai_chat_completion_api_req(self):
        print(openai.api_key)
        try:
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = self.aistant_history_messages
            )
            return response
        except:
            response = ''
            return response

    def chat_core_thread_exec(self):
        print("chat bot start chat_core_thread_exec.")
        while self.thread_chat_completion_do_run:
            time.sleep(0.1)
            self.core_threa_run_tick +=1
            if keyboard.is_pressed('enter') and keyboard.is_pressed('shift'):
                print("New line Command.")
            elif keyboard.is_pressed('enter'):
                self.chat_core_button_submit_exec()
            if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_EXEC:
                response = self.openai_chat_completion_api_req()
                if response == '':  
                    self.aistant_chat_update_statusbar('API请求错误')
                    continue
                self.aistant_history_messages.append(response.choices[0]['message']) # 新增 completion
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

    def ui_output_update(self):
        message_content_total = ''
        msg_cnt = 0
        for msg in self.aistant_history_messages:
            msg_cnt = msg_cnt + 1
            if msg_cnt == 1:
                continue
            role_msg = 'Unknown'
            print(msg['role'])
            if msg['role'] == 'user':
                role_msg = '用户'
            elif msg['role'] == 'assistant':
                role_msg = 'chatGPT'
            msg_role_with_content = role_msg + ':\n' + msg['content']
            message_content_total += msg_role_with_content
            message_content_total += '\n'
            message_content_total += '\n'
        if self.set_display_txt_output_callback != None:
            self.set_display_txt_output_callback(message_content_total)

    def aistant_chat_update_statusbar(self, content):
        if self.update_statusbar_txt_callback != None:
            self.update_statusbar_txt_callback(content)


#callback release
    def chat_core_button_submit_exec(self):
        if self.get_text_edit_input_callback != None:
            prompt_text = self.get_text_edit_input_callback()
            print("---prompt_text: %s"%prompt_text)
            # if prompt_text == '' or prompt_text == '\r' or prompt_text == '\n' or prompt_text == '\r\n':
            if prompt_text == '':
                # print("chat_core_button_submit_exec-Empty send prompt message.")
                self.aistant_chat_update_statusbar("发送消息为空")
                return 
        print("chat_core_button_submit_exec--", prompt_text)
    #     prompt_text = self.ui_agent.aistant_ui_get_textEdit_input_text()
        user_question = {"role": "user", "content": ""}
        user_question['content'] = prompt_text
        self.aistant_history_messages.append(user_question) # 新增 prompt

        if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE or self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_TIMEOUT:
            self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_EXEC)

    def chat_core_button_clear_exec(self):
        print("chat core button clear.")
        self.aistant_history_messages = [self.aistant_role_setting,]
        self.ui_output_update()

    def chat_core_button_cancel_exec(self):
        print("chat core button cancel.")
        self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

    def chat_core_button_save_exec(self):
        print("chat core button save.")
        if self.save_current_chat_callback != None:
            self.save_current_chat_callback()

    def chat_core_button_withdraw_exec(self):
        print("set chat core withdraw.")
        if len(self.aistant_history_messages) > 2:
            del self.aistant_history_messages[-1]
            del self.aistant_history_messages[-1]
            self.ui_output_update()

    def chat_core_teminate_thread_exec(self):
        self.thread_chat_completion_do_run = False

#callback consume
    def chat_core_set_get_input_text_cb_ptr(self, get_txt_input):
        self.get_text_edit_input_callback = get_txt_input

    def chat_core_set_display_response_cb_ptr(self, display_response):
        self.set_display_txt_output_callback = display_response

    def chat_core_set_save_chat_cb_ptr(self, save_chat_txt):
        self.save_current_chat_callback = save_chat_txt

    def chat_core_set_update_statusbar_cb_ptr(self, update_statusbar_callback):
        self.update_statusbar_txt_callback = update_statusbar_callback