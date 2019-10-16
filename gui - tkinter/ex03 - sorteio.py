from tkinter import *
from random import randint
font=('Arial','15')
numero=''
def bt_num_sorteio():
    global num
    num=randint(1,100)
    lb_num.configure(text='Tenho um número entre 1 e 100',bg='yellow', fg='black')
    et_palpite.config(state='normal')



def bt_conf():
    palpite = int(et_palpite.get())
    bt_num.config(state='disabled')
    if palpite==num:
        lb_num.configure(text='CORRETO', bg='green',font=font, fg='white')
        et_palpite.config(state='disabled')
        bt_num.config(state='normal')
    else:
        if palpite<num:
            lb_num.configure(text='tente outra vez! meu numero é MAIOR', bg='red',fg='white')
        else:
            lb_num.configure(text='tente outra vez! meu numero é MENOR', bg='red',fg='silver')





tela=Tk()
tela.title('Adivinhe o Número')
tela.geometry('300x200')
lb_num=Label(tela,text='Adivinhe o Número!')
lb_palpite=Label(tela,text='qual seu palpite:')
et_palpite=Entry(tela)
bt_num=Button(tela,text='sortear')
bt_conferir=Button(tela,text='conferir')

lb_num.pack()
bt_num.pack()
lb_palpite.pack()
et_palpite.pack()
bt_conferir.pack()
bt_num['command']=bt_num_sorteio
bt_conferir['command']=bt_conf

tela.mainloop()