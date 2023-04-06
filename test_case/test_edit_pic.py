from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QTextEdit, QApplication
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPixmap

app = QApplication([])
text_edit = QTextEdit()
#向textedit增加一张图片
document = QTextDocument()
document.addResource(QTextDocument.ImageResource, QUrl("image://test.png"), QPixmap("test.png"))
document.setHtml("<img src='image://test.png' />")

text_edit.setDocument(document)
text_edit.show()
app.exec_()