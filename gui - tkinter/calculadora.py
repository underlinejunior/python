from tkinter import *

tela = Tk()
tela.geometry("400x300")
tela.title("C A L C U L A D O R A")

def r_soma():
    res = (float(e1.get()) + float(e2.get()))
    r.configure(text=res)

def r_sub():
    res = (float(e1.get()) - float(e2.get()))
    r.configure(text=res)

def r_mult():
    res = (float(e1.get()) * float(e2.get()))
    r.configure(text=res)

def r_div():
    res = (float(e1.get()) / float(e2.get()))
    r.configure(text=res)

numero1 = Label(tela, text='Número 1:', bg='lightgreen')
numero1.grid(row=1, column=1)
e1 = Entry(tela)
e1.grid(row=1, column=2)
numero2 = Label(tela, text='Número 2:', bg='lightgreen')
numero2.grid(row=2, column=1)
e2 = Entry(tela)
e2.grid(row=2, column=2)
r = Label(tela, text='Resultado:', bg='lightgreen')
r.grid(row=3, column=2)
btn1 = Button(tela, text="+", command=r_soma, bg='blue', fg='white')
btn2 = Button(tela, text="-", command=r_sub, bg='red', fg='white')
btn3 = Button(tela, text="*", command=r_mult, bg='orange', fg='white')
btn4 = Button(tela, text="/", command=r_div, bg='purple', fg='white')

num1= Button(tela, text="1", command=r_soma, bg='blue', fg='white')
num1.place=(x=10,y=120)
num2= Button(tela, text="2", command=r_soma, bg='blue', fg='white')
num2.place=(x=50,y=120)
num3= Button(tela, text="3", command=r_soma, bg='blue', fg='white')
num3.place=(x=90,y=120)
num4= Button(tela, text="4", command=r_soma, bg='blue', fg='white')
num4.place=(x=130,y=120)
num5= Button(tela, text="5", command=r_soma, bg='blue', fg='white')
num5.place=(x=10,y=150)
num6= Button(tela, text="6", command=r_soma, bg='blue', fg='white')
num6.place=(x=50,y=150)
num7= Button(tela, text="7", command=r_soma, bg='blue', fg='white')
num7.place=(x=90,y=150)
num8= Button(tela, text="8", command=r_soma, bg='blue', fg='white')
num8.place=(x=130,y=150)
num9= Button(tela, text="9", command=r_soma, bg='blue', fg='white')
num9.place(x=50,y=180)
num0= Button(tela, text="0", command=r_soma, bg='blue', fg='white')
num0.place=(x=130,y=180)

btn1.place(x=20, y=80)
btn2.place(x=70, y=80)
btn3.place(x=120, y=80)
btn4.place(x=170, y=80)

tela.mainloop()
