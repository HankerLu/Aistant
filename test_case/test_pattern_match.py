
import re
#构造一个 '用户:' + '{内容}' + 'chatGPT:' + '{内容}' 的正则表达式
# pattern =
pattern = r"用户:(.*)chatGPT:(.*)"
# file_content = 用户(设定):
# 我希望你能扮演一名得力的助手的角色。

# 用户:
# 你好

# chatGPT:
# 你好，有什么我可以帮助你的吗？


#上面内容在每一行 后面增加/
file_content = '用户(设定):/我希望你能扮演一名得力的助手的角色。/用户:/你好/chatGPT:/你好，有什么我可以帮助你的吗？/'

match = re.search(pattern, file_content)
if match:
    print("match")