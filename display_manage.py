import tkinter as tk
import markdown
from html.parser import HTMLParser

class MarkdownViewer(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        self.text = tk.Text(self, wrap="word", font=("Helvetica", 12))
        self.text.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self, command=self.text.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.text.configure(yscrollcommand=self.scrollbar.set)
        self.text.tag_configure("bold", font=("Helvetica", 12, "bold"))
        self.text.tag_configure("italic", font=("Helvetica", 12, "italic"))

    def set_text(self, text):
        html = markdown.markdown(text)
        self.text.delete("1.0", "end")
        self.insert_html(html)

    def insert_html(self, html):
        parser = HTMLParser()
        parser.handle_data = self.handle_data
        parser.feed(html)

    def handle_data(self, data):
        if data.startswith("<strong>") and data.endswith("</strong>"):
            self.text.insert("end", data[8:-9], "bold")
        elif data.startswith("<em>") and data.endswith("</em>"):
            self.text.insert("end", data[4:-5], "italic")
        else:
            self.text.insert("end", data)

if __name__ == "__main__":
    root = tk.Tk()
    viewer = MarkdownViewer(root)
    viewer.pack(fill="both", expand=True)

    markdown_text = """
    # Heading 1
    This is a **bold** and *italic* text.

    ## Heading 2
    This is a [link](https://www.example.com).

    ### Heading 3
    This is a list:
    - Item 1
    - Item 2
    - Item 3
    """
    viewer.set_text(markdown_text)

    root.mainloop()