
# from latexcodec import latex_to_text, text_to_latex
# import latexcodec
# # # 将LaTeX代码转换为字符串
# latex_code = r'$\int_{0}^{\infty} e^{-x^2} dx$'
# string = latex_code.encode("latex")
# print(string)
# from latexcodec import encode

# latex = r'\frac{1}{2}'
# string = encode(latex)
# print(string.decode('utf8'))

# # 将字符串转换为LaTeX代码
# latex_code = text_to_latex(string)

# print(latex_code)  # 输出：\frac{1}{2}

# import latexcodec
# text_latex = b"\\'el\\`eve"
# assert text_latex.decode("latex") == u"élève"
# text_unicode = u"ångström"
# assert text_unicode.encode("latex") == b'\\aa ngstr\\"om'

# import latexcodec
# text_latex = b"\\'el\\`eve"
# assert text_latex.decode("latex") == u"élève"
# text_unicode = u"ångström"
# assert text_unicode.encode("latex") == b'\\aa ngstr\\"om'
# print(text_latex.decode("latex"))

from sympy import *
from IPython.display import display, Math
import time
init_printing(use_latex='mathjax')

x, y, z = symbols('x y z')
expr = x**2 + y**2 + z**2

while True:
    display(Math(r'f(x,y,z) = %s' % latex(expr)))
    time.sleep(1)


import latex2mathml.converter
import xml.etree.ElementTree as ET

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

pageSource = ''

input = r"\frac{1}{2}"
input = r'$\int_{0}^{\infty} e^{-x^2} dx$'
mathml = latex2mathml.converter.convert(input)
# print(mathml)
pageSource = mathml
root = ET.fromstring(mathml)
final_ret = root.find(".//{http://www.w3.org/1998/Math/MathML}mrow").text
print('final_ret:', final_ret)

print('pageSource:', pageSource)
# 首先，导入QApplication和QWebEngineView。

# 然后，编写一个包含HTML代码的多行字符串。 该代码应导入MathJax javascript模块。 然后，写出数学方程式...


# 最后，实例化QApplication，实例化QWebEngineView，并将WebEngineView设置为显示新编写的HTML代码：

pageSource = '<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msubsup><mo data-mjx-texclass="OP">∫</mo><mrow><mn>0</mn></mrow><mrow><mi mathvariant="normal">∞</mi></mrow></msubsup><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mi>d</mi><mi>x</mi></math>'
app = QApplication(sys.argv)
webView = QWebEngineView()
webView.setHtml(pageSource)
# 不要忘记在WebEngineView上调用show。

webView.show()
sys.exit(app.exec_())
