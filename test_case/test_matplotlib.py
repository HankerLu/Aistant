from matplotlib import mathtext, font_manager
import matplotlib as mpl
mpl.rcParams['savefig.transparent'] = True

#texFont = font_manager.FontProperties(size=30, fname="./OpenSans-Medium.ttf")
texFont = font_manager.FontProperties(size=30, family='serif', math_fontfamily='cm')

mathtext.math_to_image(r"Maths $\int_{0}^{\infty} e^{-x^2} dx$", "output.png", prop=texFont, dpi=300, format='png')


# from IPython.display import Latex

# data = Latex(r"$\sqrt{x^2+y^2}$")
# print(data)


import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from io import BytesIO
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import Qt


def render_latex_to_pixmap(latex):
    fig = plt.figure(figsize=(0.01, 0.01))
    plt.text(0, 0, latex, fontsize=12)
    plt.axis('off')
    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=300, bbox_inches='tight', pad_inches=0)
    buffer_.seek(0)
    pixmap = QPixmap()
    pixmap.loadFromData(buffer_.read())
    return pixmap

class LatexLabel(QLabel):
    def __init__(self, latex):
        super().__init__()
        self.setPixmap(render_latex_to_pixmap(latex))

app = QApplication(sys.argv)
LatexLabel(r"$\frac{-b + \sqrt{b^{{2}} - {4} a c}}{{2} a}$").show()
sys.exit(app.exec_())