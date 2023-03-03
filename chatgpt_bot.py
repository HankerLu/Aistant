import tkinter as tk
import openai
# import prompt_completion_chat_Chinese
# openai.api_key = "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"


class AIToolBackEnd:
   def __init__(self):
      print("chat bot v2.0")
      self.g_model_name = "gpt-3.5-turbo"
      self.g_history_messages = [         
               {"role": "system", "content": "你是一个得力的助手, 你叫chatgpt, 你是基于GPT3.5开发的"},]

   def on_submit(self):
      prompt = input_field.get()
      user_question = {"role": "user", "content": ""}
      user_question['content'] = prompt
      self.g_history_messages.append(user_question) # 新增 prompt

      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = self.g_history_messages
      )
      self.g_history_messages.append(response.choices[0]['message']) # 新增 completion
      self.update_result_text()

   def update_result_text(self):
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

      result_text.config(state="normal")
      result_text.delete("1.0", "end")
      result_text.insert("end", message_content_total)
      result_text.config(state="disabled")

   def update_key(self):
      print("update key.")
      api_key = key_update_field.get()
      print(api_key)
      openai.api_key = api_key

   def reset_coversation(self):
      print("reset conversation.")
      self.g_history_messages = [{"role": "system", "content": "你是一个得力的助手, 你叫chatgpt, 你是基于GPT3.5开发的"},]
      self.update_result_text()

if __name__ == "__main__":
   ai_tool_backend = AIToolBackEnd()
   
   window = tk.Tk()
   window.title("ChatGPT 本地对话机器人 v2.0")

   input_field = tk.Entry(window, width=140)
   submit_button = tk.Button(window, text="发送", command = ai_tool_backend.on_submit)

   key_update_field = tk.Entry(window, width=80)
   key_update_button = tk.Button(window, text="API_KEY", command = ai_tool_backend.update_key)
   # input_api_key_field = tk.Entry(window, width=60)
   # submit_button = tk.Button(window, text="Submit", command=on_submit)

   reset_coversation_button = tk.Button(window, text="重置按钮", command = ai_tool_backend.reset_coversation)

   result_text = tk.Text(window, state="normal", width=160, height=60)

   key_update_field.pack()
   key_update_button.pack()

   input_field.pack()
   submit_button.pack()

   reset_coversation_button.pack()

   result_text.pack()

   window.mainloop()