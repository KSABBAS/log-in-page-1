from tkinter import *
login=Tk()
login.geometry("1520x850")
login.config(background="#6BBDFF")
wellcome=Frame(login,bg="#A3D9FF")
wellcome.place(x=560,y=300,height=200,width=400)
l=Label(login,text="wellcome",fg="#F1F264",font=("groove","130"),bg="#6BBDFF")
l.place(x=400,y=80)
wellcome2=Frame(login ,bg="#A3D9FF")
wellcome2.place(x=560,y=530,height=110,width=400)
e1=Entry(wellcome,width=27,font=("groove","10"),fg="gray",bg="white")
e1.place(x=20,y=40)
e2=Entry(wellcome,width=27,font=("groove","10"),fg="gray",bg="white")
e2.place(x=20,y=90)
l1=Label(wellcome,text='user name \\ email ', bg="#A3D9FF",fg="#F1F264",font=("family","13"))
l1.place(x=225,y=35)
l2=Label(wellcome,text=' password ', bg="#A3D9FF",fg="#F1F264",font=("family","13"))
l2.place(x=235,y=85)
b1=Button(wellcome,text="log in",bg="white",font=("family","15"),padx=4,pady=.001,relief="flat")
b1.place(x=300,y=150)
l3=Label(wellcome2,text="if you don't have an account click sign in ", bg="#A3D9FF",fg="#F1F264",font=("family","12"))
l3.place(x=15,y=10)

b2=Button(wellcome2,font=("family","13"),padx=4,pady=.001,text="sign in",bg="white",relief="flat")
b2.place(x=300,y=60)










login.mainloop()