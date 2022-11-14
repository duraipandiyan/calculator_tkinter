from tkinter import *
import numpy as np
window=Tk()
window.title("CALCULATOR")
window.configure(bg="#3D3C3A")
window.geometry("677x500")
window.resizable(width="False",height="False")

number=IntVar()

entrytxt=Entry(window,width=35,bd=40,textvariable=number,bg="#3D3C3A",fg="black",font=("times",25,"bold"))
entrytxt.grid(row=0,column=0,columnspan=12)
#btnframe
btnframe=Frame(window,width=50,bg="#3D3C3A")
btnframe.grid(row=1,column=0)

btnclr=Button(btnframe,text="CL",bd=3,bg="black",width=12,height=2,fg="white",activebackground="blue")
btnclr.grid(row=0,column=0)

btnallclr=Button(btnframe,text="AC",bd=3,bg="red",width=12,height=2,fg="black",activebackground="blue")
btnallclr.grid(row=0,column=1)

btnroot=Button(btnframe,text="√",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue")
btnroot.grid(row=0,column=2)

btnpl=Button(btnframe,text="+",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue")
btnpl.grid(row=0,column=3)

btnmin=Button(btnframe,text="*",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue")
btnmin.grid(row=1,column=3)

btnmul=Button(btnframe,text="-",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue")
btnmul.grid(row=2,column=3)


btnsl=Button(btnframe,text="^",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue")
btnsl.grid(row=4,column=3)

btneq=Button(btnframe,text="=",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue")
btneq.grid(row=3,column=3)

btndiv=Button(btnframe,text="%",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue")
btndiv.grid(row=4,column=2)


def btnclck(num):
   data=entrytxt.get()
   counters=(num)
   entrytxt.insert(str(counters)+str(data))

def coss():
 cos=np.cos()
    

btn1=Button(btnframe,text="1",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(1))
btn1.grid(row=1,column=0)

btn2=Button(btnframe,text="2",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(2))
btn2.grid(row=1,column=1)

btn3=Button(btnframe,text="3",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(3))
btn3.grid(row=1,column=2)

btn4=Button(btnframe,text="4",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(4))
btn4.grid(row=2,column=0)

btn5=Button(btnframe,text="5",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(5))
btn5.grid(row=2,column=1)

btn6=Button(btnframe,text="6",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(6))
btn6.grid(row=2,column=2)

btn7=Button(btnframe,text="7",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(7))
btn7.grid(row=3,column=0)

btn8=Button(btnframe,text="8",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(8))
btn8.grid(row=3,column=1)

btn9=Button(btnframe,text="9",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(9))
btn9.grid(row=3,column=2)

btn0=Button(btnframe,text="0",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(0))
btn0.grid(row=4,column=0)


btndot=Button(btnframe,text=".",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue")
btndot.grid(row=4,column=1)

btndiv=Button(btnframe,text="π",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btndiv.grid(row=0,column=4)

btn2py=Button(btnframe,text="2π",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btn2py.grid(row=1,column=4)

btnln=Button(btnframe,text="ln",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnln.grid(row=2,column=4)

btnlog=Button(btnframe,text="log₁₀",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnlog.grid(row=3,column=4)

btnopen=Button(btnframe,text="(",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnopen.grid(row=4,column=4)

btnclos=Button(btnframe,text=")",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnclos.grid(row=4,column=5)

btncos=Button(btnframe,text="cosθ",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=coss)
btncos.grid(row=0,column=5)


btncosh=Button(btnframe,text="cosh",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btncosh.grid(row=1,column=5)

btntan=Button(btnframe,text="tanθ",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btntan.grid(row=2,column=5)

btntanh=Button(btnframe,text="tanh",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btntanh.grid(row=3,column=5)

btnsin=Button(btnframe,text="sinθ",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnsin.grid(row=0,column=6)

btnsinh=Button(btnframe,text="sinh",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnsinh.grid(row=1,column=6)

btnqube=Button(btnframe,text=chr(8731),bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnqube.grid(row=2,column=6)

btnsinh=Button(btnframe,text=chr(247),bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnsinh.grid(row=3,column=6)

btnx=Button(btnframe,text="x!",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnx.grid(row=4,column=6)


window.mainloop()