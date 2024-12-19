from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st,text="Restart",font=("Time New Roman",20,"bold"),
                  relief=RAISED,cursor="plus",command=restart)
r_button.place(x=140,y=100, height=50,width=180)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=140,y=150, height=50,width=180)

lg_button = Button(st,text="Log-Out",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=140,y=200, height=50,width=180)

sd_button = Button(st,text="Shut-Down",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=shutdown)
sd_button.place(x=140,y=250, height=50,width=180)

st.mainloop()