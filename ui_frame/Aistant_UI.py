# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Aistant_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 1149)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_6.addWidget(self.checkBox_2)
        self.verticalLayout_19.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 607, 831))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout_18.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout_18.addLayout(self.horizontalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_8.addWidget(self.textEdit_2)
        self.verticalLayout_19.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_11.addWidget(self.textEdit_3)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_26.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_26)
        self.horizontalLayout_11.setStretch(0, 4)
        self.horizontalLayout_11.setStretch(1, 1)
        self.verticalLayout_27.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_20.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lineEdit = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_13.addWidget(self.lineEdit)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1250, 1005))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.comboBox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_10.addWidget(self.comboBox_4)
        self.verticalLayout_16.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_9.addWidget(self.comboBox_3)
        self.verticalLayout_16.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_16.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_7.addWidget(self.plainTextEdit)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_2)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_16.addLayout(self.verticalLayout_7)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_15.addWidget(self.label_4)
        self.comboBox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.verticalLayout_15.addWidget(self.comboBox_5)
        self.verticalLayout_16.addLayout(self.verticalLayout_15)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_11.addWidget(self.checkBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 4)
        self.horizontalLayout_5.setStretch(2, 8)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem4)
        self.verticalLayout_16.addLayout(self.verticalLayout_11)
        self.verticalLayout_16.setStretch(3, 1)
        self.verticalLayout_16.setStretch(5, 6)
        self.verticalLayout_17.addLayout(self.verticalLayout_16)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_17.addLayout(self.verticalLayout_6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.addWidget(self.scrollArea_2)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1292, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setEnabled(True)
        self.menu.setGeometry(QtCore.QRect(267, 133, 120, 72))
        self.menu.setTearOffEnabled(False)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setGeometry(QtCore.QRect(347, 133, 120, 94))
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_chatgpt = QtWidgets.QAction(MainWindow)
        self.action_chatgpt.setObjectName("action_chatgpt")
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionAI = QtWidgets.QAction(MainWindow)
        self.actionAI.setObjectName("actionAI")
        self.actionAI_2 = QtWidgets.QAction(MainWindow)
        self.actionAI_2.setObjectName("actionAI_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action_11)
        self.menu_2.addAction(self.action_10)
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.action_8)
        self.menu_3.addAction(self.action_9)
        self.menu_5.addAction(self.action_chatgpt)
        self.menu_5.addAction(self.actionAI)
        self.menu_5.addAction(self.actionA)
        self.menu_5.addAction(self.actionAI_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.action_4)
        self.toolBar.addAction(self.action_5)
        self.toolBar.addAction(self.action_7)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aistant"))
        self.label_9.setText(_translate("MainWindow", "标签主题："))
        self.checkBox_2.setText(_translate("MainWindow", "自动生成主题"))
        self.pushButton_4.setText(_translate("MainWindow", "发送"))
        self.pushButton_5.setText(_translate("MainWindow", "取消"))
        self.pushButton_6.setText(_translate("MainWindow", "保存对话"))
        self.pushButton.setText(_translate("MainWindow", "撤回"))
        self.pushButton_7.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "对话1"))
        self.pushButton_3.setText(_translate("MainWindow", "新建对话"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "草稿"))
        self.pushButton_2.setText(_translate("MainWindow", "保存设置"))
        self.label_7.setText(_translate("MainWindow", "功能：对话基本设置"))
        self.label.setText(_translate("MainWindow", "对话模型"))
        self.label_2.setText(_translate("MainWindow", "默认角色设定（仅在gpt-3.5-turbo模型下有效）"))
        self.label_8.setText(_translate("MainWindow", "默认角色补充描述（你可以基于‘默认角色设定’补充额外的描述和说明）"))
        self.label_3.setText(_translate("MainWindow", "对话文本显示格式"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "text"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "markdown"))
        self.label_4.setText(_translate("MainWindow", "对话代码高亮"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "关闭高亮"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "开启高亮"))
        self.label_5.setText(_translate("MainWindow", "功能：多轮对话设置（设置多轮对话及最大记忆轮数）"))
        self.checkBox.setText(_translate("MainWindow", "开启多轮对话（仅在gpt-3.5-turbo模型下支持开启）"))
        self.label_6.setText(_translate("MainWindow", "多轮对话轮数"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.menu_5.setTitle(_translate("MainWindow", "功能"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.action_6.setText(_translate("MainWindow", "密钥管理"))
        self.action_8.setText(_translate("MainWindow", "使用说明"))
        self.action_9.setText(_translate("MainWindow", "关于..."))
        self.action_10.setText(_translate("MainWindow", "功能设置"))
        self.action_11.setText(_translate("MainWindow", "打开文件"))
        self.action_chatgpt.setText(_translate("MainWindow", "AI对话"))
        self.actionA.setText(_translate("MainWindow", "AI翻译"))
        self.actionAI.setText(_translate("MainWindow", "AI编辑"))
        self.actionAI_2.setText(_translate("MainWindow", "AI编程"))
        self.action_4.setText(_translate("MainWindow", "仅聊"))
        self.action_5.setText(_translate("MainWindow", "聊与写"))
        self.action_7.setText(_translate("MainWindow", "仅写"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
