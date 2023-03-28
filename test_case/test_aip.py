import aiohttp
import asyncio


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


head = {
    'Content-Type': 'application/json',
    'Authorization' : 'Bearer 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'
}

# async def post(session):
#     print('post start')
#     async with session.post(URL, json=payload, headers = head) as response:
#         print('post with session')
#         return await response.text()
#         # return 

# async def main():
#     print('main start')
#     # connector = aiohttp.TCPConnector(port=8080)
#     async with aiohttp.ClientSession() as session:
#         try:
#             html = await post(session)
#             print(html)
#         except Exception as e:
#             print('main:', e)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


async def apost():
    print('apost start')
    async with aiohttp.ClientSession() as session:
        print('session start')
        async with session.request(
            'POST', URL, headers=head, json=payload,
        ) as response:
            print('response start')
            return await response.text()

print('start')
loop = asyncio.get_event_loop()
loop.run_until_complete(apost())