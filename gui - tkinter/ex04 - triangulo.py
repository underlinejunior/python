from tkinter import *

def bt_tipo_click():
    a=float(et_lado01.get())
    b=float(et_lado02.get())
    c=float(et_lado03.get())
    if a<b+c and b<a+c and c<b+a:
        if a==b==c:
            tipo.configure(text='Triângulo Equilátero')
        else:
            if a==b or a==c or b==c:
                tipo.configure(text='Triangulo Isoceles')
            else:
                tipo.configure(text='Triangulo Escaleno')
    else:
        tipo.configure(text='Não forma um Triangulo')
tela=Tk()
tela.title('Triangulos')
tela.geometry('350x150')
lb_lado01=Label(tela,text='lado 1:')
lb_lado02=Label(tela,text='lado 2:')
lb_lado03=Label(tela,text='lado 3:')
et_lado01=Entry(tela)
et_lado02=Entry(tela)
et_lado03=Entry(tela)
tipo=Label(tela)

lb_lado01.place(x=10, y=10)
lb_lado02.place(x=10, y=40)
lb_lado03.place(x=10, y=70)
et_lado01.place(x=50, y=10)
et_lado02.place(x=50, y=40)
et_lado03.place(x=50, y=70)
tipo.place(x=200, y =50)
bt_tipo=Button(tela,text='Verificar Tipo')
bt_tipo.place(x=10,y=120, width=165)
bt_tipo['command']=bt_tipo_click

tela.mainloop()