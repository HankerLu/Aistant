from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.webview = QWebEngineView()
        self.webview.load(QUrl.fromLocalFile('/test_case/test_res.html'))
        # self.webview.setHtml('<body><h1>MathJax Example</h1><p>Here is an example of a math formula:</p><p>$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$</p></body>', 
        #                      QUrl("https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())