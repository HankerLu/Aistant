# from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
# from PyQt5.QtGui import QIcon
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setGeometry(100, 100, 300, 200)
#         self.setWindowTitle('Right-click menu')

#     def contextMenuEvent(self, event):
#         menu = QMenu(self)
#         action = QAction("Action", self)
#         menu.addAction(action)
#         menu.exec_(self.mapToGlobal(event.pos()))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QTextEdit, QMenu, QAction, QShortcut, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 创建文本编辑框
        self.text_edit = QTextEdit(self)
        self.text_edit.setObjectName('text_edit')

        # 创建快捷键和弹出菜单
        shortcut = QShortcut('Ctrl+;', self)
        shortcut.activated.connect(self.show_menu)
        self.menu = QMenu(self)
        self.menu.addAction(QAction('选项1', self))
        self.menu.addAction(QAction('选项2', self))
        self.menu.setEnabled(False)
    
        # 添加布局
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
        
    def show_menu(self):
        # 显示弹出菜单
        cursor_position = self.text_edit.mapToGlobal(self.text_edit.pos())
        cursor_position.setY(cursor_position.y() + self.text_edit.cursorRect().bottom())
        self.menu.exec_(cursor_position)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()