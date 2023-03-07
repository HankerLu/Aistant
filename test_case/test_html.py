from PyQt5.QtWidgets import QApplication, QTextBrowser
app = QApplication([])
text = QTextBrowser()
text.setHtml('''
    <img src="./test.png" alt="Image"/>
''')
text.show()
app.exec_()