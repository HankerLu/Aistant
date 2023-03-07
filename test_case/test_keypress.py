from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 创建布局和标签
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Press a key", self)
        self.layout.addWidget(self.label)
        
        # 设置小部件焦点策略
        self.setFocusPolicy(Qt.StrongFocus)
        
    def keyPressEvent(self, event):
        # 按下Escape键退出
        if event.key() == Qt.Key_Escape:
            self.close()
        # 显示按下的键
        text = f"Key {event.key()} {event.text()}"
        self.label.setText(text)
            
# class KPE_Detector(QWidget):
#     def __init__(self):
#         super(KPE_Detector, self).__init__()
#         self.label = QLabel("cxvxvdffdsf sddfdsfsd wererwer", self)
#         self.setFocusPolicy(QtCore.Qt.StrongFocus)
#         print("KPE_Detector init.")

#     def mousePressEvent(self, e):
#         print('A mouse button was pressed!')
#         # event.ignore()

#     def keyPressEvent(self, e):
#         print("detect key presss event.", e)

# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()
        
#         # 创建布局和标签
#         self.layout = QGridLayout(self)
#         # 设置小部件焦点策略
#         self.setFocusPolicy(QtCore.Qt.StrongFocus)
        
#     def keyPressEvent(self, event):
#         print("key pressed1.")

# class MyWidget2(QWidget):
#     def __init__(self, layout):
#         super().__init__()
        
#         # 创建布局和标签
#         self.layout = layout
#         # 设置小部件焦点策略
#         self.setFocusPolicy(QtCore.Qt.StrongFocus)
        
#     def keyPressEvent(self, event):
#         print("key pressed2.")

if __name__ == "__main__":
    app = QApplication([])
    w = MyWidget()
    w.show()
    app.exec_()