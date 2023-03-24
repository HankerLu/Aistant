#基于openai.ChatCompletion.acreate 的多线程的异步访问的demo

import openai
import asyncio
import os
import threading
import time

async def run_openai_async():
    #以下代码用一条线程来循环执行
    print('run_openai_async running...')
    aistant_chat_total_messages = [{"role": "system", "content": "你是一名得力的助手"},]
    user_question = {"role": "user", "content": ""}
    user_question['content'] = '你好'
    aistant_chat_total_messages.append(user_question) # 新增 
    response = ''
    while True:
        print("chatgpt running...")
        # time.sleep(0.1)
        try:    
            response = await openai.ChatCompletion.acreate(
                model = 'gpt-3.5-turbo',
                messages = aistant_chat_total_messages,
                temperature = 0.1
            )
            print(response.choices[0].message)
        except Exception as e:
            print(e)
        print("chatgpt running...")
#用异步方式运行run_openai_async
print('before runnning run_openai_async')
asyncio.run(run_openai_async())
print("after runnning run_openai_async")
    