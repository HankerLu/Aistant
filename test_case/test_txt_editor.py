import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.geometry("800x600")
        self.master.minsize(400, 300)

        # Create menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Create menus
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.theme_menu = tk.Menu(self.menu_bar, tearoff=False)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)

        # File menu items
        self.file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Save as...", accelerator="Ctrl+Shift+S", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", accelerator="Alt+F4", command=self.exit)

        # Edit menu items
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste_text)

        # Theme menu items
        self.theme_menu.add_command(label="Light", command=self.light_theme)
        self.theme_menu.add_command(label="Dark", command=self.dark_theme)
        self.theme_menu.add_command(label="Custom...", command=self.custom_theme)

        # Create text widget
        self.text_widget = tk.Text(self.master, wrap="word")
        self.text_widget.pack(fill="both", expand=True)

        # Create scrollbar
        self.scroll_bar = ttk.Scrollbar(self.text_widget)
        self.scroll_bar.pack(side="right", fill="y")

        # Attach scrollbar to text widget
        self.text_widget.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.text_widget.yview)

        # Set default theme
        self.light_theme()

    # File menu functions
    def new_file(self):
        self.text_widget.delete("1.0", tk.END)
        self.current_file = None

    def open_file(self):
        self.current_file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.current_file:
            self.master.title(os.path.basename(self.current_file))
            with open(self.current_file, "r") as f:
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert("1.0", f.read())

    def save_file(self):
        if not self.current_file:
            self.save_file_as()
        else:
            with open(self.current_file, "w") as f:
                f.write(self.text_widget.get("1.0", tk.END))

    def save_file_as(self):
        self.current_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.current_file:
            with open(self.current_file, "w") as f:
                f.write(self.text_widget.get("1.0", tk.END))
            self.master.title(os.path.basename(self.current_file))

    def exit(self):
        self.master.quit()

    # Edit menu functions
    def cut_text(self):
        self.text_widget.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_widget.event_generate("<<Paste>>")

    # Theme menu functions
    def light_theme(self):
        self.text_widget.config(bg="white", fg="black")

    def dark_theme(self):
        self.text_widget.config(bg="black", fg="white")

    def custom_theme(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()