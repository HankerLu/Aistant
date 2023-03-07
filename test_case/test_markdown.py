from PyQt5.QtWidgets import QApplication, QTextBrowser, QVBoxLayout, QWidget
import markdown
import os
file_path = 'D:\Entrepreneurship\HankAmy\SW2303\chatbot_prj\test_case\example.md'
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

os_path_file = os.path.basename(file_path)
print(os_path_file)
with open(os_path_file, 'r') as f:
    md_text = f.read()

# Convert Markdown to HTML
html = markdown.markdown(md_text)

# Create a QTextBrowser widget and load the HTML
text_browser = QTextBrowser()
text_browser.setHtml(html)

# Add the QTextBrowser to the layout
layout.addWidget(text_browser)
window.setLayout(layout)
window.show()
app.exec_()