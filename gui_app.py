import tkinter as tk
from tkinter import filedialog, Text # is for what?
import os 

root = tk.Tk() # holds the whole app
canvas = tk.Canvas(root,height=700,width=700, bg = "#263")
canvas.pack()
root.mainloop()#creates a infinity loop to show our window
