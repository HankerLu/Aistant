import re
import requests
from PIL import Image
from io import BytesIO
import time
import cv2

import urllib.request
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel


# 需要检测的文本
text = "这是一张图片：https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"

# 正则表达式匹配图片链接
pattern = re.compile(r'(https?:\/\/\S+\.(?:jpg|jpeg|png|gif))')
image_urls = pattern.findall(text)



# 显示窗口
app = QApplication([])

# 下载并检测每个图片链接
for url in image_urls:
    response = requests.get(url)
    print(BytesIO(response.content))
    image = Image.open(BytesIO(response.content)).convert('RGBA')
    image.save('./cat.png')
    pixmap = QPixmap('./cat.png')
    # pixmap.loadFromData(image)

    # 创建QLabel对象并设置Pixmap
    label = QLabel()
    label.setPixmap(pixmap)
    label.show()
    app.exec_()
    