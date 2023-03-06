import Aistant_UI
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


# 连接操作：
# 1.连接前端和自定义槽函数
# 2.自定义槽函数
class Aistant_UI_Agent:
    def __init__(self):
        print(" Aistant connector init.")
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Aistant_UI.Ui_MainWindow()
        ui.setupUi(MainWindow)
        
        self.mainwin = MainWindow
        self.app = app
        self.ui = ui 

        self.ui.action_chatgpt.triggered.connect(self.action_chatgpt_slot_exec)

    def action_chatgpt_slot_exec(self):
        print("action_chatgpt_slot_exec.")

    def Aistant_UI_show(self):
        self.mainwin.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":

    aistant_ui = Aistant_UI_Agent()
    aistant_ui.Aistant_UI_show()

    # ui.action_chatgpt.triggered.connect(print_text_by_q_action) # type: ignore

    # MainWindow.show()
    # sys.exit(app.exec_())
