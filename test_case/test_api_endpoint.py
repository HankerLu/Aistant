import requests
import threading
import time
import re
import asyncio
import aiohttp

URL = 'https://api.openai.com/v1/chat/completions'

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "你好"},],
    # 'top_p': 1,
    # 'n': 1,
    'stream': True,
    # 'temperature': 0.9,
    # 'presence_penalty': 0,
    # 'frequency_penalty': 0,
}


headers = {
    'Content-Type': 'application/json',
    'Authorization' : 'Bearer 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'
}

# async def req_post():
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.post(URL, json=payload, headers=headers) as response:
#                 print(response.status)
#                 res = await response.text()
#                 return res
#     except Exception as e:
#         print(e)

# async def req_get():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(URL) as resp:
#             print(resp.status)
#             res = await resp.text()
#             return res



# async def main():
#     await req_post()

# print('start')
# asyncio.run(main())
# get请求
# 创建使用session


def req_api():
    print('req_api start')
    # while True:
    response = ''
    try:
        response =  requests.post(URL, json=payload, headers=headers)
        # response.encoding = 'utf-8'
        # ret_json = response.json()
        txt = response.text
        #将 所有 {"delta":{"content": 与 },"index": 之间的内容提取出来，不要用re.findall

        pattern = re.compile(r'{"delta":{"content":.*?},"index":')
        ret = pattern.findall(txt)
        #打印ret成员
        final_ret = ''
        for i in ret:
            # print('-----:', i[21:-11])
            final_ret+=i[21:-11]
        print(final_ret.encode('latin-1').decode('utf-8'))
        # print('thread status:    ', response.status_code)
    except Exception as e:
        print('thread exception:  ', e)
if __name__ == '__main__':
    print('main start')
    threading.Thread(target=req_api).start()
    while True:
        time.sleep(1)
        print("main loop")
        try:
            #用异步的方式获取response.text
            # print(response.text)
            # response =  requests.post(URL, json=payload, headers=headers)
            # print(response.text)
            continue
        except:
            print('req exception')



