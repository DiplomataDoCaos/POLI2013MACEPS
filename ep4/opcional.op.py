"""
Exemplo de como utilizar a classe janela, assumindo que o arquivo janela.py
esteja na mesma pasta desse exemplo.

Fica como exercício aprender a utilizar as demais funções dessa classe.
Em particular, de uma olhada nas funções:
- desenhe_turtledorm
- repinte_vizinhos
- mostre_solucao
- incrementa_jogadas
- quantas_jogadas

"""

import janela

def main():
    """
    """
    tdorm = [[0,0,1,1],
             [0,0,0,1],
             [0,0,0,0],
             [0,0,0,0]]
    # depois que a janela é criada, o programa enta em loop
    janela.crie_janela(tdorm, trata_d, trata_a, trata_clique)

def trata_d():#devem estar ultra abreviados
    """ o programa, em loop, trata esse evento: tecla d
    """
    print("Clicou em d")
    janela.termine()
    
def trata_a():#são de release
    """ trata tecla_a
    """
    print("clicou em a")

def trata_clique(x, y):
    """ trata um clique no botão esquerdo do mouse
    """
    tdorm = janela.turtledorm
    lin, col = janela.converta_para_lincol(x, y)
    print("Clique na posição (%d, %d) da janela, em pixel"%(x,y))
    print("Que corresponde a posição (%d, %d) do turtledorm"%(lin, col))

janela = janela.Janela()
main()


    
