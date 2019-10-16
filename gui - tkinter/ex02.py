from tkinter import *
numeros=''

def bt_ok_click():
    global numeros
    numeros=et_numeros.get()
    numeros=numeros.split(',')
    for x in range(len(numeros)):
        numeros[x]=int(numeros[x])


def bt_exibir_click():
    et_maior.delete(0)
    et_menor.delete(0)
    et_media.delete(0,(len(et_media.get())))

    global numeros
    maior=max(numeros)
    menor=min(numeros)
    media=sum(numeros)/len(numeros)

    et_maior.insert(0,str(maior))
    et_menor.insert(0,str(menor))
    et_media.insert(0,str(media))



font=('arial','10','bold')
tela=Tk()
tela.title('numeros')
lb_digite=Label(tela,text='Digite um numero:',font=font)
lb_maior=Label(tela,text='Maior>>>',font=font)
lb_menor=Label(tela,text='Menor>>>',font=font)
lb_media=Label(tela,text='Media>>>',font=font)

et_numeros=Entry(tela)
et_maior=Entry(tela)
et_menor=Entry(tela)
et_media=Entry(tela)

bt_ok=Button(tela,text='OK', width=15,font=font)
bt_exibir=Button(tela,text='Exibir', width=15,font=font)

lb_digite.grid(row=1, column=1)
lb_maior.grid(row=4, column=1)
lb_menor.grid(row=5, column=1)
lb_media.grid(row=6, column=1)

et_numeros.grid(row=2, column=1)
et_maior.grid(row=4, column=2)
et_menor.grid(row=5, column=2)
et_media.grid(row=6, column=2)

bt_ok.grid(row=2, column=2)
bt_exibir.grid(row=5, column=3)


bt_ok['command']=bt_ok_click
bt_exibir['command']=bt_exibir_click


tela.mainloop()
