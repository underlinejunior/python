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
        #SIDE DEFINE A POSIÇÃO NA JANELA(TOP,BOTTOM,LEFT,RIGHT)
cima.pack(side='top')
baixo.pack(side='bottom')
esquerda.pack(side='left')
direita.pack(side='right')

#FAZER A JANELA EXECUTAR
janela.mainloop()