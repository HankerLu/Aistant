
import openai
from enum import Enum
import threading
import time

class OpenAIReqStatus(Enum):
   REQ_STATUS_IDLE = 0
   REQ_STATUS_EXEC = 1
   REQ_STATUS_TIMEOUT = 2
class Aistant_Chat_Core():
    def __init__(self):
        print(" Aistant Aistant_Chat_Core init.")
        self.aistant_chat_model_name = "gpt-3.5-turbo"
        self.aistant_role_setting = {"role": "system", "content": "你是一个得力的助手, 你叫chatgpt, 你是基于GPT3.5开发的"}
        self.aistant_history_messages = [ self.aistant_role_setting,]

        self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

        self.thread_chat_completion_do_run = True
        self.thread_chat_completion = threading.Thread(target = self.chat_completion_req_thread_exec)
        self.thread_chat_completion.start()

    def openai_chat_completion_api_req(self):
        print(openai.api_key)
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = self.aistant_history_messages
        )
        return response

    def chat_completion_req_thread_exec(self):
        print("chat bot start chat_completion_req_thread_exec.")
        while self.thread_chat_completion_do_run:
            time.sleep(0.1)
            if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_EXEC:
                response = self.openai_chat_completion_api_req()
                self.aistant_history_messages.append(response.choices[0]['message']) # 新增 completion
                # self.ui_output_update()
                print(response.choices[0]['message'])
                self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

    def update_openai_req_status(self, status):
        print("update_openai_req_status", status)
        self.aistant_chat_completion_req_status = status

    def set_openai_req_thread_do_run(self, do_run):
        self.thread_chat_completion_do_run = do_run

    def chat_core_button_submit_exec(self):
        print("chat_core_button_submit_exec--", self.get_text_edit_input_callback())
    #     prompt_text = self.ui_agent.aistant_ui_get_textEdit_input_text()
        # user_question = {"role": "user", "content": ""}
        # user_question['content'] = prompt
        # self.g_history_messages.append(user_question) # 新增 prompt

        # if self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE or self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_TIMEOUT:
        #     self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_EXEC)
    
    def chat_core_set_get_input_text_cb_ptr(self, get_txt_inpit):
        self.get_text_edit_input_callback = get_txt_inpit