import tkinter as tk

class LoadingScreen:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.label = tk.Label(self.frame, text="Loading...")
        self.label.pack()
        self.frame.pack()

    def start(self):
        self.frame.pack()
        self.parent.update()

    def stop(self):
        self.frame.pack_forget()
        self.parent.update()

import time

root = tk.Tk()
loading_screen = LoadingScreen(root)

# do some time-consuming task
loading_screen.start()
time.sleep(2)
loading_screen.stop()

root.mainloop()