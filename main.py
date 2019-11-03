import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import filedialog

class MessageWindow(tk.Toplevel):
    def __init__(self, title, message):
        super().__init__()
        self.details_expanded = False
        self.title(title)
        self.geometry("300x75+{}+{}".format(self.master.winfo_x(), self.master.winfo_y()))
        self.resizable(False, False)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        tk.Label(self, text=message).grid(row=0, column=0, columnspan=3, pady=(7, 7), padx=(7, 7), sticky="ew")
        tk.Button(self, text="OK", command=self.master.destroy).grid(row=1, column=1, sticky="e")
        tk.Button(self, text="Cancel", command=self.destroy).grid(row=1, column=2, padx=(7, 7), sticky="e")

windows = tk.Tk()

windows.title("round_tool")
windows.geometry("500x500")

s = tk.Label(windows, text = "FILE", font = ("arial", 20), heigh = 8)
messagebox.showinfo("menu", "welcome to the round_tool\n\nresult will be in the same folder with this python file")


filename = " "
def choose():
    global filename
    filename = filedialog.askopenfilename(filetype = (("jpeg files","*.jpg"),("all files","*.*")))
    # print("123" + filename + "456")
    # print(type(filename))
    if filename == "":
        # messagebox.showinfo("selected", filename)
        messagebox.showwarning("warring", "you selected nothing")
    else:
        # messagebox.showinfo("warring", "you didn't selected anything")
        messagebox.showinfo("selected", filename)

def gogo():
    print("gogo")

def exit_windows():
    MessageWindow("Quit", "Are you sure you want to quit?")

b = tk.Button(windows, text = 'open', font = ('Arial', 15), width = 10, height = 1, command = choose)
g = tk.Button(windows, text = 'go', font = ('Arial', 15), width = 10, height = 1, command = gogo)

s.pack()
b.pack()
g.pack()

windows.protocol("WM_DELETE_WINDOW", exit_windows)
windows.mainloop()
