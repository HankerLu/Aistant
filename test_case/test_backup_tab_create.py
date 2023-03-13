#========================================================================#
#新建及删除对话标签页
        # self.hide_draft_txt_editor_status = True
        # self.ui.pushButton_3.clicked.connect(self.aistant_create_new_chat_tab_page_exec)
        # self.ui.tabWidget.tabCloseRequested.connect(self.aistant_remove_old_chat_tab_page_exec)
        # # self.ui.tabWidget.removeTab(self.ui.tabWidget.indexOf(self.ui.tab_2))
        
        # self.close_tab_button = QtWidgets.QToolButton()
        # self.close_tab_button.setToolTip('Add New Tab')
        # self.close_tab_button.clicked.connect(self.aistant_create_new_chat_tab_page_exec)
        # self.close_tab_button.setIcon(QtWidgets.QWidget().style().standardIcon(QtWidgets.QStyle.SP_DialogYesButton))
        # self.ui.tabWidget.setCornerWidget(self.close_tab_button, QtCore.Qt.TopRightCorner)

    # def aistant_remove_old_chat_tab_page_exec(self, request_tab_id):
    #     print("aistant_remove_old_chat_tab_page_exec. req_id:", request_tab_id)
    #     if request_tab_id!= self.ui.tabWidget.indexOf(self.ui.tab_2):
    #         print("this is the tab page to be remove")
    #         self.ui.tabWidget.removeTab(request_tab_id) 

    # def aistant_hide_draft_txt_editor(self):
    #     if self.hide_draft_txt_editor_status == True:
    #         self.ui.textEdit_3.setVisible(False)
    #         self.hide_draft_txt_editor_status = False
    #     else:
    #         self.ui.textEdit_3.setVisible(True)
    #         self.hide_draft_txt_editor_status = True

    # def aistant_create_new_chat_tab_page_exec(self):
    #     print("aistant_create_new_chat_tab_page")

    #     # ui_form = Aistant_chat_tab_UI.Ui_Form()
    #     # new_tab = QtWidgets.QWidget()
    #     # Aistant_chat_tab_UI.Ui_Form().setupUi(new_tab)
    #     new_tab = Aistant_Chat_UI_Tab_Agent(self.ui.tabWidget)
    #     new_tab_name = "对话" + str(self.ui.tabWidget.count())
    #     new_tab_insert_pos = self.ui.tabWidget.count() - 1
    #     self.ui.tabWidget.insertTab(new_tab_insert_pos, new_tab, new_tab_name) #基于当前名称更新对话标签名
    #     textbrowser_format = QTextCharFormat()
    #     textbrowser_format.setForeground(QColor(31, 31, 31))
    #     new_tab.ui.textBrowser.setStyleSheet("background-color: rgb(210,210,210);")
    #     new_tab.ui.textBrowser.setCurrentCharFormat(textbrowser_format)  # 应用高亮格式

    #     font = QtGui.QFont()
    #     font.setPointSize(12)
    #     new_tab.ui.textBrowser.setFont(font)
    #     new_tab.ui.textEdit_2.setFont(font)
#------------------------------#
#========================================================================#