from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QTextEdit, QApplication

app = QApplication([])
text_edit = QTextEdit()
document = QTextDocument()
document.setHtml(r"\frac{-b + \sqrt{b^{{2}} - {4} a c}}{{2} a}")
text_edit.setDocument(document)
text_edit.show()
app.exec_()