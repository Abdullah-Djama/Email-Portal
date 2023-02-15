from tkinter import *
import tkinter

window= Tk() 
# instance of a window 
window.geometry("420x420")
window.title("Email Portal")
#window.config(background="#C0C2C9")
login_icon =tkinter.Label(window,text=" Email Login")
username_label=tkinter.Label(window,text="Username")
username_input=tkinter.Entry(window)
password_input=tkinter.Entry(window,show="*")
password_label=tkinter.Label(window,text="Password")
login_button=tkinter.Button(window,text="Login")



# place window on the computer screen

login_icon.grid(row=0,column=0,columnspan=2)
username_label.grid(row=1,column=0)
username_input.grid(row=1,column=1)
password_input.grid(row=2,column=1)
password_label.grid(row=2,column=0)
login_button.grid(row=3,column=0,columnspan=2)

window.mainloop()


