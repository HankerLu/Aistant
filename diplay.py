import tkinter as tk
import requests
import markdown
from tkinterhtml import HtmlFrame

# 获取Markdown文本并将其转换为HTML
url = 'https://raw.githubusercontent.com/adam-p/markdown-here/master/README.md'
response = requests.get(url)
markdown_text = response.text
html_text = markdown.markdown(markdown_text)

# 创建tkinter窗口
root = tk.Tk()

# 在窗口中添加HTML框架
frame = HtmlFrame(root)
frame.set_content(html_text)
frame.pack(fill='both', expand=True)

# 运行窗口
root.mainloop()