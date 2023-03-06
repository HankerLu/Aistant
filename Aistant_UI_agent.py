from PyQt5 import QtCore, QtGui, QtWidgets
import Aistant_UI
import sys

# 连接操作：
# 1.连接前端和自定义槽函数
# 2.自定义槽函数
class Aistant_UI_Agent:
    def __init__(self):
        print(" Aistant UI agent init.")
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Aistant_UI.Ui_MainWindow()
        ui.setupUi(MainWindow)
        
        self.mainwin = MainWindow
        self.app = app
        self.ui = ui 

        self.ui.action_chatgpt.triggered.connect(self.action_chatgpt_slot_exec)
        self.ui.action_6.triggered.connect(self.action_key_manage_exec)

    def action_chatgpt_slot_exec(self):
        print("action_chatgpt_slot_exec.")
        self.ui.stackedWidget.setCurrentIndex(1)

    def action_key_manage_exec(self):
        print("action_key_manage_exec")
        self.ui.stackedWidget.setCurrentIndex(2)

    def Aistant_UI_show(self):
        self.mainwin.show()
        sys.exit(self.app.exec_())