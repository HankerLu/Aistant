from PIL import Image

# 打开图像文件
image = Image.open('./8666753_message_circle_chat_icon.ico')

# 将图像文件转换为.icns格式
image.save('8666753_message_circle_chat_icon.icns', format='ICNS')
# ImageTool().createFromPng('8666753_message_circle_chat_icon.icon', '8666753_message_circle_chat_icon.icns')