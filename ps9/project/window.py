import tkinter as tk
import tkinter.ttk as ttk

class Window:
    def __init__(self, master):
        self.master = master

        frame = ttk.Frame(self.master)
        


root = tk.Tk()
root.geometry("800x1000")
window = Window(root)
root.mainloop()