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
cima.grid(row=1, column=1)
baixo.grid(row=3, column=1)
esquerda.grid(row=2, column=1)
direita.grid(row=2, column=2)

#FAZER A JANELA EXECUTAR
janela.mainloop()