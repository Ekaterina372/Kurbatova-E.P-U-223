"""
Платформа операционной системы IoF
Репозиторий: github.com/ARMmbed/mbed-os
user - ARMmbed
"""
import json
import requests
from tkinter import*
import os
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)

def buttonAction():
    with open(path + "\\result.txt","w") as file:
        user = txtField.get()
        url = f"https://api.github.com/users/{user}"
        userInfo = requests.get(url).json()
        enum = ['company', 'created_at', 'email', 'id', 'name', 'url']
        data = userInfo.keys()
        for i in data:
            if i in enum:
                file.write(f"{i}:{userInfo[i]}" + '\n')
    head.configure(text = "Feel good (o･ω･o)\n you can find your data in 'result.txt' file in root")

root = Tk()
root.title('Get user data')
root.geometry('700x300')
root["bg"] = "#E0FFFF"

head = Label(root, fg = "black", bg= "#E0FFFF", text = 'Enter username', font = ('', 22))
head.pack(expand=True)
txtField = Entry(root,width=40)
txtField.pack(expand=True)
button = Button(root, text = 'GET DATA',command = buttonAction)
button.pack(expand=True)
root.mainloop()