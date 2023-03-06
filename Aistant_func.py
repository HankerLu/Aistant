
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
                self.ui_output_update()
                # print(response.choices[0]['message'])
                self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

    def update_openai_req_status(self, status):
        print("update_openai_req_status", status)
        self.aistant_chat_completion_req_status = status

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
            if msg['role'] == 'user':
                role_msg = '用户'
            elif msg['role'] == 'assistant':
                role_msg = 'chatGPT'
                msg_role_with_content = role_msg + ':\n' + msg['content']
                message_content_total += msg_role_with_content
                message_content_total += '\n'
                message_content_total += '\n'
        self.set_display_txt_output_callback(message_content_total)

    # def update_result_text(self, message_total):
    #     # html = markdown.markdown(message_total)
    #     # result_text.set_content(html)
    #     result_text.config(state="normal")
    #     result_text.delete("1.0", "end")
    #     result_text.insert("end", message_total)
    #     result_text.config(state="disabled")


#callback release
    def chat_core_button_submit_exec(self):
        prompt_text = self.get_text_edit_input_callback()
        print("chat_core_button_submit_exec--", prompt_text)
    #     prompt_text = self.ui_agent.aistant_ui_get_textEdit_input_text()
        user_question = {"role": "user", "content": ""}
        user_question['content'] = prompt_text
        self.aistant_history_messages.append(user_question) # 新增 prompt

        if self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE or self.aistant_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_TIMEOUT:
            self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_EXEC)
            # response = self.openai_chat_completion_api_req()
            # self.aistant_history_messages.append(response.choices[0]['message']) # 新增 completion
            # self.ui_output_update()

#callback consume
    def chat_core_set_get_input_text_cb_ptr(self, get_txt_input):
        self.get_text_edit_input_callback = get_txt_input

    def chat_core_set_display_response_cb_ptr(self, display_response):
        self.set_display_txt_output_callback = display_response