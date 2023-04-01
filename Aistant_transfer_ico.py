from PIL import Image


# with open('*.ico', 'rb') as f:
#     for file in f:
#         print(file)

files = ['aistant.ico', 'open.ico', 'find.ico', 'save.ico', 'right.ico', 'both.ico', 'left.ico']

for file in files:
    # 打开图像文件
    image = Image.open(file)

    #获取文件basename
    basename = file.split('.')[0]
    whole_name = basename + '.icns'
    # 将图像文件转换为.icns格式
    image.save(whole_name, format='ICNS')
    # ImageTool().createFromPng('8666753_message_circle_chat_icon.icon', '8666753_message_circle_chat_icon.icns')