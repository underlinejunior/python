from tkinter import *

font=('Arial','10')
def bt_calc():
    global v
    terra=float(et_peso.get())
    if v.get()==1:
        planeta = (terra / 10) * 0.37
        nome='Mercúrio'
    if v.get()==2:
        planeta = (terra / 10) * 0.88
        nome = 'Vênus'
    if v.get()==3:
        planeta = (terra / 10) * 0.38
        nome = 'Marte'
    if v.get()==4:
        planeta = (terra / 10) * 2.64
        nome = 'Jupiter'
    if v.get()==5:
        planeta = (terra / 10) * 1.15
        nome = 'Saturno'
    if v.get()==6:
        planeta = (terra / 10) * 1.17
        nome = 'urano'
    lb_res.configure(text='em {} o peso seria de {}kg'.format(nome,planeta),bg='yellow',font=font)



tela=Tk()
tela.title('peso nos planetas')
tela.geometry('250x200')


lb_peso=Label(tela,text='Peso na Terra (kg):')
et_peso=Entry(tela)
bt_calcular=Button(tela,text='Calcular Peso')
lb_planeta=Label(tela,text='selecione o Planeta:')
lb_res=Label(tela)

v=IntVar()
Radiobutton(tela,text='Mércurio',variable=v,command=bt_calc, value=1).place(x=10,y=90)
Radiobutton(tela,text='Vênus',variable=v,command=bt_calc, value=2).place(x=90,y=110)
Radiobutton(tela,text='Marte',variable=v,command=bt_calc, value=3).place(x=170,y=90)
Radiobutton(tela,text='Jupiter',variable=v,command=bt_calc, value=4).place(x=10,y=110)
Radiobutton(tela,text='Saturno',variable=v,command=bt_calc, value=5).place(x=90,y=90)
Radiobutton(tela,text='Urano',variable=v,command=bt_calc, value=6).place(x=170,y=110)

lb_peso.place(x=10,y=10)
et_peso.place(x=10,y=40)
bt_calcular.place(x=150,y=40)
lb_planeta.place(x=10,y=70)
lb_res.place(x=10,y=130)

bt_calcular['command']=bt_calc

tela.mainloop()