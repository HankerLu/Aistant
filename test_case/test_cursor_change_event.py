from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtCore import Qt

class TextEditor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cursorPositionChanged.connect(self.cursor_position_changed)
        
    def cursor_position_changed(self):
        cursor = self.textCursor()
        print("cursor_position_changed")
        if cursor.position() == 0 and cursor.hasSelection() == False:
            print("光标回到了起点")
            
if __name__ == '__main__':
    app = QApplication([])
    text_editor = TextEditor()
    text_editor.show()
    app.exec_()