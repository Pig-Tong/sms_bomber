# _*_ coding:utf-8 _*_
import urllib.request
from tkinter import *


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)


def send_sms():
    phone = entry_phone.get()
    url = "https://www.daoyuanketang.com/api/sendmobilecode?mobile=" + phone
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/70.0.3538.77 Safari/537.36"
    headers = {"User_Agent": user_agent, 'Accept': 'application/json, text/plain, */*',
               'Accept-Encoding': 'gzip, deflate, br', 'clientType': 'web'}

    print(url)

    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)


def btnClick():
    if entry_phone.get() == "":
        textLabel['text'] = "请输入手机号"
        return
    if len(entry_phone.get()) != 11:
        textLabel['text'] = "手机号不正确"
        return
    textLabel['text'] = "即将向：" + str(entry_phone.get()) + "发送短信"
    send_sms()


root = Tk(className="短信轰炸机v1.0", )

# 设置窗体大小
center_window(root, 500, 340)
root.maxsize(600, 400)
root.minsize(300, 240)

# 手机号
text_phone = Label(root, text='手机号', justify=LEFT, padx=10)
text_phone.pack(side=TOP)

# 输入框
entry_phone = Entry(root, width=30, bg="white", fg="black")
entry_phone.pack(side=TOP)

# 提示信息
textLabel = Label(root, text='提示显示', justify=LEFT, padx=10)
textLabel.pack(side=TOP)

# 按钮
btn = Button(root)
btn['text'] = '点击测试'
btn['command'] = btnClick
btn.pack(side=BOTTOM)

mainloop()
