import tkinter as tk
import ttkbootstrap as ttk
import os

def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()


def open_window(window_type="none"):
        # filewin = ttk.Toplevel(root)
        # filewin.geometry("500x200")
        # button = ttk.Button(filewin, text=window_type)
        # button.pack()
        if (window_type == "New NSA Window"):
                os.system('python nsa_window.py')


root = tk.Tk()
root.title("Soliver")
root.geometry("750x270")
menubar = ttk.Menu(root)
filemenu = ttk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New NSA", command=lambda:open_window("New NSA Window"))
filemenu.add_command(label="New sVSWR", command=lambda:open_window("New sVSWR Window"))

filemenu.add_separator()

filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = ttk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = ttk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
