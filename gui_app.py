import tkinter as tk
from tkinter import filedialog, Text # is for what?
import os 

root = tk.Tk() # holds the whole app
#def addApp():

canvas = tk.Canvas(root,height=700,width=700, bg = "#263")
canvas.pack()



openFile = tk.Button(root, text="Open File", padx=10,pady=5, fg="white",bg ="#263d42")
openFile.pack()

runApps = tk.Button(root,text = "Run File",padx=10,pady=5,fg="yellow",bg="#345")
runApps.pack()
root.mainloop()#creates a infinity loop to show our window
