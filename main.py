from tkinter import *
import numpy as np
window=Tk()
window.title("CALCULATOR")
window.configure(bg="#3D3C3A")
window.geometry("677x500")
window.resizable(width="False",height="False")

number=StringVar()

def clear():
    entrytxt.delete(0)


def allclear():
    entrytxt.delete(0,END)

entrytxt=Entry(window,width=35,bd=40,textvariable=number,bg="#3D3C3A",fg="black",font=("times",25,"bold"))
entrytxt.grid(row=0,column=0,columnspan=12)
#btnframe
btnframe=Frame(window,width=50,bg="#3D3C3A")
btnframe.grid(row=1,column=0)

btnclr=Button(btnframe,text="CL",bd=3,bg="black",width=12,height=2,fg="white",activebackground="blue",command=clear)
btnclr.grid(row=0,column=0)

btnallclr=Button(btnframe,text="AC",bd=3,bg="red",width=12,height=2,fg="black",activebackground="blue",command=allclear)
btnallclr.grid(row=0,column=1)

btnroot=Button(btnframe,text="√",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("√"))
btnroot.grid(row=0,column=2)

btnpl=Button(btnframe,text="+",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("+"))
btnpl.grid(row=0,column=3)

btnmin=Button(btnframe,text="*",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("*"))
btnmin.grid(row=1,column=3)

btnmul=Button(btnframe,text="-",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("-"))
btnmul.grid(row=2,column=3)


btnsl=Button(btnframe,text="^",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("^"))
btnsl.grid(row=4,column=3)

btneq=Button(btnframe,text="=",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("="))
btneq.grid(row=3,column=3)

btndiv=Button(btnframe,text="%",bd=3,bg="gray",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("%"))
btndiv.grid(row=4,column=2)


def btnclck(num):
   data=entrytxt.get()
   count1=data
   entrytxt.delete(0,END)
   entrytxt.insert(0,str(count1)+str(num))

def coss():
  data1=entrytxt.get()
  var1=int(data1)
  cos=np.cos(var1)
  entrytxt.insert(0,cos)

def cossh():
  data2=entrytxt.get()
  var2=int(data2)
  cosh=np.cosh(var2)
  entrytxt.insert(0,cosh)

def sin():
  data3=entrytxt.get()
  var3=int(data3)
  sin=np.sin(var3)
  entrytxt.insert(0,sin)
def sinh():
  data4=entrytxt.get()
  var4=int(data4)
  sinh=np.sinh(var4)
  entrytxt.insert(0,sinh)

def tan():
  data5=entrytxt.get()
  var5=int(data5)
  tan=np.tan(var5)
  entrytxt.insert(0,tan)

def tanh():
  data6=entrytxt.get()
  var6=int(data6)
  tanh=np.tan(var6)
  entrytxt.insert(0,tanh)


def log():
    data7=entrytxt.get()
    var7=int(data7)
    log=np.log10(var7)
    entrytxt.insert(0,log)
def sqroot():
    data8=entrytxt.get()
    var8=int(data8)
    sq=np.sqrt(var8)
    entrytxt.insert(0,sq)

def div():
    data9=entrytxt.get()
    var9=int(data9)
    div=np.divide(var9,var9)
    entrytxt.insert(0,div)


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


btndot=Button(btnframe,text=".",bd=3,bg="#4B5320",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("."))
btndot.grid(row=4,column=1)

btndiv=Button(btnframe,text="π",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btndiv.grid(row=0,column=4)

btn2py=Button(btnframe,text="2π",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btn2py.grid(row=1,column=4)

btnln=Button(btnframe,text="ln",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnln.grid(row=2,column=4)

btnlog=Button(btnframe,text="log₁₀",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=log)
btnlog.grid(row=3,column=4)

btnopen=Button(btnframe,text="(",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck("("))
btnopen.grid(row=4,column=4)

btnclos=Button(btnframe,text=")",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=lambda:btnclck(")"))
btnclos.grid(row=4,column=5)

btncos=Button(btnframe,text="cosθ",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=coss)
btncos.grid(row=0,column=5)


btncosh=Button(btnframe,text="cosh",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=cossh)
btncosh.grid(row=1,column=5)

btntan=Button(btnframe,text="tanθ",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=tan)
btntan.grid(row=2,column=5)

btntanh=Button(btnframe,text="tanh",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=tanh)
btntanh.grid(row=3,column=5)

btnsin=Button(btnframe,text="sinθ",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=sin)
btnsin.grid(row=0,column=6)

btnsinh=Button(btnframe,text="sinh",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=sinh)
btnsinh.grid(row=1,column=6)

btnqube=Button(btnframe,text=chr(8731),bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=sqroot)
btnqube.grid(row=2,column=6)

btnsinh=Button(btnframe,text=chr(247),bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue",command=div)
btnsinh.grid(row=3,column=6)

btnx=Button(btnframe,text="x!",bd=3,bg="#C19A6B",width=12,height=2,fg="black",activebackground="blue")
btnx.grid(row=4,column=6)


window.mainloop()