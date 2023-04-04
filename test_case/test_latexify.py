import math
import latexify

# import sys
# from PyQt5.QtWidgets import QApplication, QTextEdit
# from PyQt5.QtGui import QTextDocument
# from PyQt5.QtCore import Qt

# app = QApplication(sys.argv)

# # 创建QTextEdit控件

# text_edit = QTextEdit()
@latexify.with_latex#调用latexify的装饰器
def solve(a, b, c):
  return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

print(solve)

# text_edit.setText(solve)
# text_edit.show()
# sys.exit(app.exec_())
