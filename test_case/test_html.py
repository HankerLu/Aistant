# from PyQt5.QtWidgets import QApplication, QTextBrowser, QLabel
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
# app = QApplication([])
# text = QTextBrowser()
# text.setFont(QFont("Times", 12))
# text.setMarkdown(
#     '<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msubsup><mo data-mjx-texclass="OP">∫</mo><mrow><mn>0</mn></mrow><mrow><mi mathvariant="normal">∞</mi></mrow></msubsup><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>x</mi></math>'
# )
# text.show()
# app.exec_()

# import sys
# from PyQt5.QtWidgets import QApplication, QTextBrowser
# import markdown

# app = QApplication(sys.argv)

# # 创建QTextBrowser控件
# text_browser = QTextBrowser()

# # 将Markdown文本转换为HTML格式
# md_text = "# Hello, world!\n\nThis is a **Markdown** text."
# html_text = markdown.markdown(md_text)

# # 将HTML文本设置为QTextBrowser的内容
# text_browser.setHtml(html_text)

# # 显示QTextBrowser控件
# text_browser.show()

# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWebEngineWidgets import QWebEngineView

# app = QApplication(sys.argv)

# # 创建QWebEngineView控件
# web_view = QWebEngineView()

# # 构造HTML文本，使用KaTeX库渲染数学公式
# html_text = """
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="utf-8">
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.11.1/katex.min.css">
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.11.1/katex.min.js"></script>
# </head>
# <body>
#     <p>这是一段包含KaTeX数学公式的文本：</p>
#     <p>$$E=mc^2$$</p>
#     <p>$$\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$$</p>
# </body>
# </html>
# """

# # 将HTML文本设置为QWebEngineView的内容
# web_view.setHtml(html_text)

# # 显示QWebEngineView控件
# web_view.show()

# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# 创建QTextEdit控件
text_edit = QTextEdit()

# 创建QTextDocument对象
document = QTextDocument()

# 插入包含LaTeX公式的HTML文本
html_text = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <p>这是一段包含LaTeX公式的文本：</p>
    <p>$$E=mc^2$$</p>
    <p>$$\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$$</p>
</body>
</html>
"""
document.setHtml(html_text)

# 将QTextDocument设置为QTextEdit的文档
text_edit.setDocument(document)

# 设置QTextEdit为只读模式
text_edit.setReadOnly(True)

# 显示QTextEdit控件
text_edit.show()

sys.exit(app.exec_())