from PyQt5.QtWidgets import QApplication, QTextEdit, QMenu, QAction, QShortcut, QVBoxLayout, QWidget

class AistantSmartMenu(QWidget):
    def __init__(self, editor_widget = QTextEdit(), parent=None):
        super(AistantSmartMenu, self).__init__(parent)

        # 创建快捷键和弹出菜单
        shortcut = QShortcut('Ctrl+;', self)
        shortcut.activated.connect(self.show_menu)
        self.menu = QMenu(self)
        self.menu.addAction(QAction('选项1', self))
        self.menu.addAction(QAction('选项2', self))
        self.menu.setEnabled(False)
        self.text_edit = editor_widget
        
    def show_menu(self):
        # 显示弹出菜单
        cursor_position = self.text_edit.mapToGlobal(self.text_edit.pos())
        cursor_position.setY(cursor_position.y() + self.text_edit.cursorRect().bottom())
        self.menu.exec_(cursor_position)