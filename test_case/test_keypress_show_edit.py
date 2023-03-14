from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        
        # 绑定键盘事件
        self.text_edit.keyPressEvent = self.on_keypress_event
        
    def on_keypress_event(self, event):
        # if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Space:
        if event.key() == Qt.Key_F1:
            cursor = self.text_edit.textCursor()
            pos = cursor.position()

            line_rect = self.text_edit.cursorRect(cursor)
            x = line_rect.left()
            y = line_rect.bottom()

            self.popup = QLineEdit(self.text_edit)
            self.popup.move(x, y)
            self.popup.show()
            
            event.accept()
        else:
            super().keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()