import tkinter as tk
import openai
import markdown
from enum import Enum
from tkinterhtml import HtmlFrame
import threading
import time
# import prompt_completion_chat_Chinese
# openai.api_key = "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"

class OpenAIReqStatus(Enum):
   REQ_STATUS_IDLE = 0
   REQ_STATUS_EXEC = 1

class AIToolBackEnd:
   def __init__(self):
      print("chat bot v2.0")
      self.g_model_name = "gpt-3.5-turbo"
      self.g_history_messages = [         
               {"role": "system", "content": "你是一个得力的助手, 你叫chatgpt, 你是基于GPT3.5开发的"},]
      self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

      self.thread_chat_completion_do_run = True
      self.thread_chat_completion = threading.Thread(target = self.chat_completion_req_thread_exec)
      self.thread_chat_completion.start()

   def chat_completion_req_thread_exec(self):
      print("chat bot start chat_completion_req_thread_exec.")
      while self.thread_chat_completion_do_run:
         time.sleep(0.1)
         if self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_EXEC:
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = self.g_history_messages
            )
            self.g_history_messages.append(response.choices[0]['message']) # 新增 completion
            self.ui_output_update()
            self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

   def on_submit(self):
      prompt = input_field.get()
      user_question = {"role": "user", "content": ""}
      user_question['content'] = prompt
      self.g_history_messages.append(user_question) # 新增 prompt

      if self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE:
         self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_EXEC)
      # response = openai.ChatCompletion.create(
      # model="gpt-3.5-turbo",
      # messages = self.g_history_messages
      # )
      # self.g_history_messages.append(response.choices[0]['message']) # 新增 completion
      # self.ui_output_update()

   def ui_output_update(self):
      message_content_total = ''
      msg_cnt = 0
      for msg in self.g_history_messages:
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
      self.update_result_text(message_content_total)
   
   def update_result_text(self, message_total):
      # html = markdown.markdown(message_total)
      # result_text.set_content(html)
      result_text.config(state="normal")
      result_text.delete("1.0", "end")
      result_text.insert("end", message_total)
      result_text.config(state="disabled")

   def update_key(self):
      print("update key.")
      api_key = key_update_field.get()
      print(api_key)
      openai.api_key = api_key

   def reset_coversation(self):
      print("reset conversation.")
      self.g_history_messages = [{"role": "system", "content": "你是一个得力的助手, 你叫chatgpt, 你是基于GPT3.5开发的"},]
      self.ui_output_update()

   def get_openai_req_status_str(self):
      ret_str = "未知状态"
      if self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE:
         ret_str = "无请求"
      elif self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_EXEC:
         ret_str = "请求中"
      return ret_str

   def update_openai_req_status(self, status):
      print("update_openai_req_status", status)
      self.g_chat_completion_req_status = status
      # str_status = self.get_openai_req_status_str()
      # self.update_req_status_label.config(text = str_status)
      # self.update_label_callback()

   def set_openai_req_thread_do_run(self, do_run):
      self.thread_chat_completion_do_run = do_run


if __name__ == "__main__":
   
   ai_tool_backend = AIToolBackEnd()

   window = tk.Tk()
   window.title("ChatGPT 本地对话机器人 v2.0")

   # API_KEY 更新输入框
   key_update_field = tk.Entry(window, width=80)
   key_update_field.pack()

   # API_KEY 更新按钮
   key_update_button = tk.Button(window, text="API_KEY", command = ai_tool_backend.update_key)
   key_update_button.pack()

   # prompt 输入框
   input_field = tk.Entry(window, width=140)
   input_field.pack()

   # prompt 提交按钮
   submit_button = tk.Button(window, text="发送", command = ai_tool_backend.on_submit)
   submit_button.pack()

   # 重置对话按钮
   reset_coversation_button = tk.Button(window, text="重置按钮", command = ai_tool_backend.reset_coversation)
   reset_coversation_button.pack()

   # 对话展示展示框
   result_text = tk.Text(window, state="normal", width=160, height=60)
   result_text.pack()

   # 请求状态展示文本
   req_status_label = tk.Label(window, text = "加载中")
   req_status_label.pack()

   update_label_do_run = True
   def update_status_label_thread_exec():
      while update_label_do_run:
         time.sleep(0.1)
         str_status = ai_tool_backend.get_openai_req_status_str() 
         req_status_label.config(text = str_status)

   label_update_thread = threading.Thread(target=update_status_label_thread_exec)
   label_update_thread.start()

   window.mainloop()

   update_label_do_run = False
   ai_tool_backend.set_openai_req_thread_do_run(False)

