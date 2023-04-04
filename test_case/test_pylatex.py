from pylatexenc.latex2text import LatexNodes2Text

import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# 创建QTextEdit控件
text_edit = QTextEdit()

latex = r"""\textbf{Hi there!} Here is \emph{an equation}:
... \begin{equation}
...     \zeta = x + i y
... \end{equation}
... where $i$ is the imaginary unit.
... """

latex = "$$\int_{0}^{\infty} e^{-x^2} dx$$"
# latex = r"$\frac{1}{2}$"
txt_from_latex = LatexNodes2Text().latex_to_text(latex)
print(txt_from_latex)

# 将QTextDocument设置为QTextEdit的文档
text_edit.setText(txt_from_latex)

# 显示QTextEdit控件
text_edit.show()

sys.exit(app.exec_())
