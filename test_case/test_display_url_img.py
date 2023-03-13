import urllib.request
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel

url = 'https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png' # 图片的URL地址
data = urllib.request.urlopen(url).read()

# 将数据转换为QPixmap对象
pixmap = QPixmap()
pixmap.loadFromData(data)

# 创建QLabel对象并设置Pixmap
label = QLabel()
label.setPixmap(pixmap)

# 显示窗口
app = QApplication([])
label.show()
app.exec_()