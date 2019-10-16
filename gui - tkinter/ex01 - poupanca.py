from tkinter import *

def bt_ok_click():
    juros=float(et_juros.get())
    tempo=float(et_anos.get())
    depmensal=float(et_dep.get())
    total=('{:.2f}'.format((depmensal)*((((1+(juros/100))**(tempo*12))-1)/(juros/100))))
    resultado.configure(text=total)

def bt_clear_click():
    et_juros.delete(0,len(et_juros.get()))
    et_anos.delete(0,len(et_anos.get()))
    et_dep.delete(0,len(et_dep.get()))

tela=Tk()
tela.title("Cálculo Poupança")

lb_juros=Label(tela,text='Juros ao mês%:')
lb_juros.grid(row=1,column=1)
et_juros=Entry(tela)
et_juros.grid(row=1,column=2)

lb_anos=Label(tela,text='Num. de anos')
lb_anos.grid(row=2,column=1)
et_anos=Entry(tela)
et_anos.grid(row=2,column=2)

lb_dep=Label(tela,text='Depósito mensal R$:')
lb_dep.grid(row=3,column=1)
et_dep=Entry(tela)
et_dep.grid(row=3,column=2)
lb_total=Label(tela,text='Total poupado R$:')
lb_total.grid(row=4,column=1)
resultado=Label(tela)
resultado.grid(row=4,column=2)

bt_ok=Button(tela,text='calcular')
bt_ok.grid(row=5,column=2)
bt_ok['command']=bt_ok_click

bt_clear=Button(tela,text='limpar')
bt_clear.grid(row=5,column=1)
bt_clear['command']=bt_clear_click


tela.mainloop()