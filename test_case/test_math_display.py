# from PyQt5.QtWidgets import QApplication, QLabel

# app = QApplication([])
# label = QLabel()
# label.setText("<html>x<sup>2</sup>+y<sup>2</sup>=z<sup>2</sup></html>")
# label.show()
# app.exec_()

# from PyQt5.QtWidgets import QApplication, QTextBrowser

# app = QApplication([])
# browser = QTextBrowser()
# browser.setHtml("""
#     <html>
#         <head>
#             <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>
#         </head>
#         <body>
#             <p>$$\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}$$</p>
#         </body>
#     </html>
# """)
# browser.show()
# app.exec_()

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

pageSource ="""
             <html><head>
             <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML">                    
             </head>
             <body>
             <p><center>[wp_ad_camp_3]</center></p><p>
<mathjax style="font-size:2.3em">$$u = \\int_{-\\infty}^{\\infty}(awesome)\\cdot du$$</mathjax>
</p>
             </body></html>
            """

app = QApplication(sys.argv)
webView = QWebEngineView()
webView.setHtml(pageSource)

webView.show()
sys.exit(app.exec_())