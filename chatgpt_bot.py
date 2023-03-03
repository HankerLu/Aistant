import tkinter as tk
import openai
import markdown
from enum import Enum
from tkinterhtml import HtmlFrame
import threading
import time
from tkinter import simpledialog
from tkinter import filedialog

# from timeout_decorator import timeout, TimeoutError
# import concurrent.futures as futures
# def timeout(timelimit):
#     def decorator(func):
#         def decorated(*args, **kwargs):
#             with futures.ThreadPoolExecutor(max_workers=1) as executor:
#                 future = executor.submit(func, *args, **kwargs)
#                 try:
#                     result = future.result(timelimit)
#                 except futures.TimeoutError:
#                     print('Timeout!')
#                     raise TimeoutError from None
#                 else:
#                     print("Exec Done")
#                 executor._threads.clear()
#                 futures.thread._threads_queues.clear()
#                 return result
#         return decorated
#     return decorator

class OpenAIReqStatus(Enum):
   REQ_STATUS_IDLE = 0
   REQ_STATUS_EXEC = 1
   REQ_STATUS_TIMEOUT = 2

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

   # @timeout(5)
   def openai_chat_completion_api_req(self):
      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = self.g_history_messages
      )
      return response

   def chat_completion_req_thread_exec(self):
      print("chat bot start chat_completion_req_thread_exec.")
      while self.thread_chat_completion_do_run:
         time.sleep(0.1)
         if self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_EXEC:
            response = self.openai_chat_completion_api_req()
            self.g_history_messages.append(response.choices[0]['message']) # 新增 completion
            self.ui_output_update()
            self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

   def on_submit(self):
      prompt = input_field.get()
      user_question = {"role": "user", "content": ""}
      user_question['content'] = prompt
      self.g_history_messages.append(user_question) # 新增 prompt

      if self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE or self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_TIMEOUT:
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

   def cancel_openai_req(self):
      print("cancel openai req.")
      self.update_openai_req_status(OpenAIReqStatus.REQ_STATUS_IDLE)

   def save_conversation_name_input(self):
      # text = simpledialog.askstring("Input", "请输入保存文件名:")
      # print("Input: " + str(text))
      # final_save_name = str(text) + '.txt'
      file_path = filedialog.asksaveasfilename(defaultextension='.txt')
      if file_path == '':
         print("save_conversation_name_input no file")
         return
      with open(file_path, 'w') as file:
         text = result_text.get('1.0', 'end-1c') # 获取 Text 组件的文本内容
         file.write(text)


   def get_openai_req_status_str(self):
      ret_str = "未知状态"
      if self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_IDLE:
         ret_str = "无请求"
      elif self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_EXEC:
         ret_str = "请求中"
      elif self.g_chat_completion_req_status == OpenAIReqStatus.REQ_STATUS_TIMEOUT:
             ret_str = "请求超时"
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
   submit_button = tk.Button(window, text="发送", width=40, command = ai_tool_backend.on_submit)
   submit_button.pack()
   # submit_button.grid(row=0, column=0)

   # 重置对话按钮
   reset_coversation_button = tk.Button(window, text="清空对话", width=40, command = ai_tool_backend.reset_coversation)
   reset_coversation_button.pack()
   # reset_coversation_button.grid(row=0, column=1)

   # 取消请求按钮
   cancel_req_button = tk.Button(window, text="取消请求", width=40, command = ai_tool_backend.cancel_openai_req)
   cancel_req_button.pack()
   # cancel_req_button.grid(row=1, column=0)

   # 保存对话按钮
   save_coversation_button = tk.Button(window, text="保存对话", command = ai_tool_backend.save_conversation_name_input)
   save_coversation_button.pack(side="bottom", fill="both")
   # save_coversation_button.grid(row=1, column=1)

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

