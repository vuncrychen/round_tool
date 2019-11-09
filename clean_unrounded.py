from tkinter import messagebox
import shutil
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

path = os.getcwd() + "\\" + "unrounded"

if os.path.isdir(path):
    shutil.rmtree(path)
    createFolder('./unrounded/')
    messagebox.showinfo("提示", "已清除")
else:
    messagebox.showerror("錯誤", "重要檔案遺失\n\n請嘗試重新執行 round_tool.py")