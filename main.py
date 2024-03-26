from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os


root=Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

image_icon=PhotoImage(file="image/icon.png")
root.iconphoto(False,image_icon)

Label(root,text="Shareit",font=("Times New Roman", 20, "bold"),bg="#f4fdfe").place(x=20,y=30)

Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="image/send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0)
send.place(x=50,y=100)

receive_image=PhotoImage(file="image/receive.png")
send=Button(root,image=receive_image,bg="#f4fdfe",bd=0)
send.place(x=300,y=100)

Label(root,text="Send",font=("Times New Roman", 20, "bold"),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Recieve",font=("Times New Roman", 20, "bold"),bg="#f4fdfe").place(x=318,y=200)

'''background=PhotoImage(file="image/background.png")
Label(root,image=background).place(x=-2,y=323)'''

root.mainloop()