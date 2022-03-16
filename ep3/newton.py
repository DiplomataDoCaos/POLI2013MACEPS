#***************************************************************#
#**                                                           **#
#**   Nome do aluno: Fernando Talietta    Número USP:8582828  **#
#**   Exercício-Programa 3                                    **#
#**   Professor: José Augusto                                 **#
#**   Turma: 1                                                **#
#**                                                           **#
#***************************************************************#

#############################################################
#                                                           #                 
#  MÓDULO newton.py                                         #
#                                                           #
#  Modulo responsável pela aplicação da lei da gravitação   #
#  universal.                                               #
#                                                           #
#  Você deverá escrever as três funções neste módulo.       #
#  Faça e teste uma função por vez.                         #
#  Para testar utilize o Python Shell                       # 
#                                                           #
#  Não altere o nome do arquivo.                            #
#                                                           #
#  Não importe outros módulos além do math.                 #
#                                                           #     
#############################################################

# módulo necessário para a função raiz quadrada
import math

#------------------------------------------------------------#
'''(ponto, ponto [, teste]) -> float

    Recebe dois pontos ponto_1=[x1, y1] e ponto_2=[x2, y2] e
    retorna a distância entre ponto_1 e ponto_2. 

    Se teste == True imprime a coordenadas dos pontos e a distância
    entre eles. Nesse caso, imprima as coordenadas e distâncias
    utilizando o formato "%.2f".

    >>> distância([1,1],[0,0])
    1.4142135623730951
    >>> distância([1,0],[1,1])
    1.0
    >>> distância([0,1],[1,1])
    1.0
    >>> distância([1,1],[0,0],True)
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    TESTE: distância
    TESTE:   ponto_1 = (1.00,1.00)
    TESTE:   ponto_2 = (0.00,0.00)
    TESTE:   dist(ponto_1,ponto_2) = 1.41
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    1.4142135623730951
    '''
    # TAREFA 1: escreva e teste esta função

def distância(ponto_1, ponto_2, teste = False):
    a = ponto_1[0] - ponto_2[0]
    b = ponto_1[1] - ponto_2[1]
    c = math.sqrt(a*a + b*b)
    if teste==True:
        print("Coordenadas de ponto_1:", "%.2f" %ponto_1[0],"%.2f"%ponto_1[1])
        print("Coordenadas de ponto_2:", "%.2f" %ponto_2[0],"%.2f"%ponto_2[1])
        print("Distância:","%.2f"%c)
    return (c)

#------------------------------------------------------------#
'''(astro, ponto [, teste]) -> [float,float]

    Recebe um astro = [[x_a,y_a],massa_a,...] e um ponto =
    [x,y], onde
 
        - [x_a,y_a] é a posição de um astro celeste;
        - massa_a   é a massa de um astro celeste; e
        - [x, y]    é a posição de um objeto.

    Retorna o vetor aceleração [a_x,a_y] da força gravitacional 
    exercida pelo astro sobre um objeto no ponto [x,y].

    Se o parâmetro ´teste´  for True a função deve imprimir:

        - posição do astro;
        - massa do astro;
        - posição do ponto; e
        - aceleração resultante.

    Para imprimir coordenadas utilize o formato "%.2f" e para
    imprimir a massa do astro utilize o formato "%.2e".

    Esta função DEVE utilizar a função distância.
    
    Pré-condição: a distância entre [x_a,y_a] e [x,y] não é
                    "próxima" de zero.

    >>> aceleração_gravitacional([[0,0],5.97e+24],[300000,300000])
    [-20.286304296591066, -20.286304296591066]
    >>> aceleração_gravitacional([[0,0],5.97e+24],[6563,0])
    [-119890.73704206462, -0.0]
    >>> aceleração_gravitacional([[0,0],5.97e+24],[0,6563])
    [-0.0, -119890.73704206462]
    >>> aceleração_gravitacional([[0,0],5.97e+24],[30000,0])
    [-5737.833333333336, -0.0]
    >>> aceleração_gravitacional([[0,0],5.97e+24],[90000,0])
    [-637.5370370370372, -0.0]
    >>> aceleração_gravitacional([[0,0],5.97e+24],[180000,0])
    [-159.3842592592593, -0.0]
    >>> aceleração_gravitacional([[0,0],5.97e+24],[300000,300000],True)
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    TESTE: aceleração gravitacional
    TESTE:   posição do astro = (0.00,0.00)
    TESTE:   massa   do astro = 5.97e+24
    TESTE:   posição do ponto = (300000.00,300000.00)
    TESTE:   vetor aceleração = (-20.29,-20.29)
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    [-20.286304296591066, -20.286304296591066]


    '''
    # TAREFA 2: escreva e teste esta função
def aceleração_gravitacional(astro, ponto, teste = False):
    d = distância(astro[0],ponto)
    a= astro[1]*8.65*(10**-13)/(d*d)
    b=a*(float(astro[0][0])-ponto[0])/d
    c=a*(float(astro[0][1])-ponto[1])/d
    if teste==True:
        print("posição do astro:","%.2f" %astro[0][0],"%.2f" %astro[0][1])
        print("massa do astro:", "%.2e" %astro[1])
        print("posição do ponto:","%.2f" %ponto[0],"%.2f" %ponto[1])
        print("aceleração resultante:","%.2f" %b,"%.2f" %c)
    return [b,c]

#------------------------------------------------------------#
'''aceleração_resultante( lista de astros, ponto, [, teste]) -> [float,float]

    Recebe em ´lista_astros´ uma lista de astros celestes e um
    ponto = [x,y] e retorna o vetor aceleração [a_x,a_y] da força
    gravitacional exercida pelos astros sobre um objeto no ponto.

    Cada item da lista representa um astro. A parte relevante de cada 
    item tem a forma

        [[x_a,y_a],massa_a,...] 

    onde:

        - [x_a,y_a] e a posição do astro; e
        - massa_a   é a sua massa.

    Se o parâmetro ´teste´  for True a função deve imprimir:

        - posição e massa de cada astro;
        - posição do ponto; e
        - aceleração resultante.

    Para imprimir coordenadas utilize o formato "%.2f" e para
    imprimir massa de astros utilize o formato "%.2e".

    Esta função DEVE utilizar a função aceleração_gravitacional.

    >>> aceleração_resultante([[[0,0],5.97e+24], [[384400,0],7.35e+22]], [192200,0])
    [-138.0713730386207, -0.0]
    >>> aceleração_resultante([[[0,0],8.97e+22], [[100000,0],5e+21]], [80000,0])
    [-1.3110156249999996, -0.0]
    >>> aceleração_resultante([[[0, 0],8.0e+22], [[100000,0], 5e+21]], [80000,0])
    [0.0, 0.0]
    >>> aceleração_resultante([[[0,0],5.97e+24], [[384400,0],7.35e+22]], [192200,0], True)
    -------------------------------------------------------------
    TESTE: aceleração resultante
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    TESTE:   posição do astro = (0.00,0.00)
    TESTE:   massa   do astro = 5.97e+24
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    TESTE:   posição do astro = (384400.00,0.00)
    TESTE:   massa   do astro = 7.35e+22
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    TESTE:   posição do ponto      = (192200.00,0.00)
    TESTE:   aceleração resultante = (-138.07,0.00)
    -------------------------------------------------------------
    [-138.0713730386207, 0.0]
    '''
    # TAREFA 3: Escreva e teste esta função
def aceleração_resultante(lista_astros, ponto, teste = False):
    total_h=total_v=0
    for i in range(0,len(lista_astros),1):
        d=aceleração_gravitacional (lista_astros[i],ponto)
        total_h= total_h +d[0]
        total_v= total_v +d[1]
    if teste==True:
        for i in range(0,len(lista_astros),1): #checar se i reseta
            print("posição do astro",i,":","%.2f" % lista_astros[i][0][0],"%.2f" % lista_astros[i][0][1])
            print("massa do astro",i,":","%.2e"% lista_astros[i][1])
        print("posição do ponto:", "%.2f" % ponto[0],"%.2f" % ponto[1])
        print("aceleração resultante","%.2f" %total_h, "%.2f" %total_v)
    return[total_h,total_v]
