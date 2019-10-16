#importando tudo da biblioteca TKINTER - biblioteca de GUI
from tkinter import *

#CRIAR UMA JANELA
janela=Tk()

#DEFINIR TITULO PRA JANELA
janela.title('aprendendo TKINTER')

#DEFINIR O TAMANHO DA JANELA
                #largura x altura +margin-left +margin-top
janela.geometry('200x200+600+400')

#ADICIONAR LABEL (widget)
        #LOCAL,CONTEUDO BG=COR DE FUNDO)
cima = Label(janela, text='cima', bg='red',fg='white')
baixo = Label(janela, text='baixo',bg='blue',fg='white')
esquerda = Label(janela, text='esquerda',bg='yellow')
direita = Label(janela, text='direita',bg='green',fg='white')

#GERENCIADOR DE LAYOUT (PACK, GRID,PLACE)
        #PLACE - POSIÇÃO EM COORDENADAS
cima.place(x=80,y=1)
baixo.place(x=100,y=180)
esquerda.place(x=1,y=100)
direita.place(x=150,y=100)

#FAZER A JANELA EXECUTAR
janela.mainloop()