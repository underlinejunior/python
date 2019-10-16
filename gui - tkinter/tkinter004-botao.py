#importando tudo da biblioteca TKINTER - biblioteca de GUI
from tkinter import *

#CRIAR UMA JANELA
janela=Tk()

#DEFINIR TITULO PRA JANELA
janela.title('aprendendo TKINTER')

#DEFINIR O TAMANHO DA JANELA
                #largura x altura +margin-left +margin-top
janela.geometry('200x200+600+400')

def TESTE():
    label='botão TESTE funcionando'
label=Label(janela,text='teste')

#BUTTON - gria um botão
            #command - adiciona ação ao botão
btn=Button(janela,text='SAIR',command=janela.destroy)

btn2=Button(janela,text='TESTE',command=TESTE)

btn.pack()
btn2.pack()
label.pack()

#FAZER A JANELA EXECUTAR
janela.mainloop()