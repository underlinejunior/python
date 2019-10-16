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
nome = Label(janela, text='nome:')
endereco = Label(janela, text='endereço:')
telefone = Label(janela, text='telefone:')
email = Label(janela, text='e-mail:')

#CAIXA DE ENTRADA DE TEXTO
nome_ent=Entry(janela)
endereco_ent=Entry(janela)
telefone_ent=Entry(janela)
email_ent=Entry(janela)

#BUTTON - gria um botão
            #command - adiciona ação ao botão
btn=Button(janela,text='SAIR',command=janela.destroy)
btn
#GERENCIADOR DE LAYOUT (PACK, GRID,PLACE)
        #PLACE - POSIÇÃO EM COORDENADAS
nome.grid(row=1, column=1)
endereco.grid(row=2, column=1)
telefone.grid(row=3, column=1)
email.grid(row=4, column=1)

nome_ent.grid(row=1, column=2)
endereco_ent.grid(row=2, column=2)
telefone_ent.grid(row=3, column=2)
email_ent.grid(row=4, column=2)

btn.grid(row=5,column=2)

#FAZER A JANELA EXECUTAR
janela.mainloop()