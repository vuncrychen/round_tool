from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import filedialog
from selenium import webdriver
import tkinter as tk
import shutil
import time
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

windows = tk.Tk()

windows.title("round_tool")
windows.geometry("900x600")

select = tk.Label(windows, text = "選擇要圓角的圖片", font = ("arial", 20), heigh = 8)
messagebox.showinfo("歡迎", "圓角結果路徑將與瀏覽器下載路徑相同\n\n處理過程約20秒\n\n(取決於您的網速度及電腦效能)")

click = 0
filename = ""
def choose():
    global filename
    global click
    filename = filedialog.askopenfilename(filetype = (("jpeg files","*.jpg"),("all files","*.*")))
    if filename == "":
        messagebox.showwarning("警告", "您還沒選取任何檔案")
    else:
        messagebox.showinfo("已選擇檔案路徑", filename)
        click += 1

SaveAs = ""
def gogo():
    global SaveAs
    global filename
    global click
    if click == 1:
        createFolder('./temp/')
        SaveDirectory = os.getcwd()
        SaveAs = os.path.join(SaveDirectory, 'temp')
        shutil.copy(filename, SaveAs)

        browser = webdriver.Chrome()
        browser.set_window_position(-3000, 0)
        browser.get("http://www.roundpic.com/")
        browser.find_element_by_name("file").send_keys(filename)
        browser.find_element_by_xpath("//button[text()='Round it!']").click()
        browser.find_element_by_xpath('//input[@type="button"]').click()
        time.sleep(10)
        browser.close()

        messagebox.showinfo("完成", "已完成圓角")
        shutil.rmtree(SaveAs)
    else:
        messagebox.showerror("錯誤", "請先選擇檔案")

pick = tk.Button(windows, text = '選擇', font = ('Arial', 15), width = 10, height = 1, command = choose)
action = tk.Button(windows, text = '開始', font = ('Arial', 15), width = 10, height = 1, command = gogo)

select.pack()
pick.pack()
action.pack()

windows.mainloop()