from PyQt5.QtWidgets import QApplication, QTextBrowser, QLabel
from PyQt5.QtCore import Qt

app = QApplication([])
label = QLabel()
label.setTextFormat(Qt.RichText)
label.setText(
    '<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msubsup><mo data-mjx-texclass="OP">∫</mo><mrow><mn>0</mn></mrow><mrow><mi mathvariant="normal">∞</mi></mrow></msubsup><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>x</mi></math>'
)

label.show()
app.exec_()
