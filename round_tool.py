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

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

round_pic_name = ""
COLOR = "orange"
windows = tk.Tk()
windows.config(bg=COLOR)

windows.title("round_tool")
windows.geometry("900x600+300+70")

name_result = tk.Label(windows, text = "輸入圓角後的檔名", bg=COLOR, font = ("arial", 20), heigh = 6)
select = tk.Label(windows, text = "選擇要圓角的圖片", bg=COLOR, font = ("arial", 20), heigh = 5)
result = tk.Entry(windows, show=None, font=('Arial', 14))
tab = tk.Label(windows, text = " ", bg=COLOR, font = ("arial", 20), heigh = 1)

def quit(self):
    self.root.destroy()

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
    global round_pic_name
    global SaveAs
    global filename
    global click
    round_pic_name = result.get()
    if round_pic_name == "":
        round_pic_name = "noname"
    if click == 1:
        createFolder('./temp/')
        createFolder('./rounded/')
        createFolder('./unrounded/')
        SaveDirectory = os.getcwd()
        SaveAs = os.path.join(SaveDirectory, 'temp')
        shutil.copy(filename, SaveAs)

        browser = webdriver.Chrome()
        browser.set_window_position(-3000, 0)
        browser.get("http://www.roundpic.com/")
        browser.find_element_by_name("file").send_keys(filename)
        browser.find_element_by_xpath("//button[text()='Round it!']").click()
        result_name = browser.find_element_by_id("name")
        result_name.clear()
        result_name.send_keys(round_pic_name)
        browser.find_element_by_xpath('//input[@type="button"]').click()
        time.sleep(5)
        browser.close()

        SaveAs_2 = os.path.join(SaveDirectory, 'rounded')
        path = get_download_path()
        shutil.copy(path + "\\" + round_pic_name + ".jpg", SaveAs_2)
        os.remove(path + "\\" + round_pic_name + ".jpg")

        messagebox.showinfo("完成", "已完成圓角")
        shutil.rmtree(SaveAs)
    else:
        messagebox.showerror("錯誤", "請先選擇檔案")

def close():
    windows.quit()

pick = tk.Button(windows, text = '選擇', font = ('Arial', 15), width = 10, height = 1, command = choose)
action = tk.Button(windows, text = '開始', font = ('Arial', 15), width = 10, height = 1, command = gogo)
leave = tk.Button(windows, text = '離開', font = ('Arial', 15), width = 10, height = 1, command = close)

select.pack()
pick.pack()
name_result.pack()
result.pack()
tab.pack()
action.pack()
leave.pack()

windows.mainloop()
