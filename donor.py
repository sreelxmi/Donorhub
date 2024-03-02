import tkinter as tk
from tkinter import *
from tkinter import PhotoImage

root = tk.Tk()
root.title("DONORHUB")
root.geometry("500x600")


def show_frame(frame):
    frame.tkraise()

base_frame = tk.Frame(root)
base_frame.place(relheight=1, relwidth=1)

#homepage
home = tk.Frame(base_frame)
home.place(relheight=1, relwidth=1)

image_path= PhotoImage(file=r"C:\Users\sreea\OneDrive\Desktop\project\Donorhub\bg.png")
bg_image=tk.Label(home,image=image_path)
bg_image.place(relheight=1,relwidth=1)

lbl=tk.Label(home,text="DONOR HUB",bg="LightSkyBlue1",fg="red2",font=("Times New Roman",58,"bold"),justify="right")
lbl.place(relx=0.3,rely=0.2,x=400,y=4)

donate_button = tk.Button(home, text="DONATE", font=("Times New Roman",25),command=lambda: show_frame(login))
donate_button.place(relx=0.7, rely=0.5)

#login page
login = tk.Frame(base_frame)
login.place(relheight=1, relwidth=1)

login_l = tk.Label(login, text="Sign-in", font=("Times New Roman", 20))
login_l.pack(pady=20)

show_frame(home)

root.mainloop()
