import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import mathtext

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 matplotlib example - Display LaTeX formula'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel(self)
        label.move(50, 50)
        label.resize(200, 100)

        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        parser = mathtext.math_to_image(r"$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$", "test.png" )
        # parser.parse()
        pixmap = QPixmap("test.png")

        label.setPixmap(pixmap)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())