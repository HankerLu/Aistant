import openai
import aiohttp
import asyncio
from aiohttp import ClientSession
import time
openai.api_key = "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"  # supply your API key however you choose

start_time = time.time()

# send a ChatCompletion request to count to 100
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        # {'role': 'user', 'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'}
        {"role": "system", "content": '我希望你能扮演一名得力的助手的角色。'},
        {'role': 'user', 'content': '你好'}
    ],
    temperature=0,
    stream=True  # again, we set stream=True
)

# create variables to collect the stream of chunks
collected_chunks = []
collected_messages = []
# iterate through the stream of events
try:
    for chunk in response:
        chunk_time = time.time() - start_time  # calculate the time delay of the chunk
        collected_chunks.append(chunk)  # save the event response
        chunk_message = chunk['choices'][0]['delta']  # extract the message
        collected_messages.append(chunk_message)  # save the message
        print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text
except Exception as e:
    print(e)
    pass

# print the time delay and text received
print(f"Full response received {chunk_time:.2f} seconds after request")
full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
print(f"Full conversation received: {full_reply_content}")

# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {'role': 'user', 'content': "What's 1+1? Answer in one word."}
#     ],
#     temperature=0,
#     stream=True  # this time, we set stream=True
# )

# for chunk in response:
#     print(chunk)