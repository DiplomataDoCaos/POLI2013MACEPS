#############################################################
#                                                           #                 
#  MÓDULO animacao.py                                       #
#                                                           #
#  Módulo responsável pela animação.                        #
#                                                           #
#  Não altere este arquivo.                                 #
#                                                           #
#  Não altere o nome do arquivo.                            #
#                                                           #     
#  A documentação sobre "Turtle graphic for Tk" pode ser    #
#  vista em http://docs.python.org/2/library/turtle.html    #
#                                                           #
#############################################################


# módulo responsável pela animação
import turtle

# módulo para geração de números aleatorios
import random

# módulo necessário para usarmos a função cos, sin, atan e degrees
import math

# módulo usado para dar um delay antes de começar a animação
import time

# def crie_quadrante(l_cantos, l_astros, l_turtleships):
#   a declaração acima deixava os cantos variáveis,
#     llx, lly, urx, ury poderiam ser dados de entrada...
#   outro parâmetro que poderia ser dado de entrada é a 
#     dimensão da janela em número de pixels ou porcentagem
#     da tela...
#   o inconveniente de ter muitos parâmetros é o arquivo 
#     de dados... ele acaba ficando complicado e introduzindo
#     uma distração desnecessária...

#----------------------------------------------------------#
#                                                          #
# CRIE_QUADRANTE                                           #
#                                                          #
#----------------------------------------------------------#

def crie_quadrante(l_astros, l_turtleships):
    '''(lista de astros, lista de turtleship) -> [janela, lista de turtles]

    Recebe uma referência ´l_astros´ a uma lista de astros e uma
    referência ´l_turtleships´ a uma lista de tutleShips.  O
    formato de cada item da lista de astros e de cada item da
    lista de turtleships está descrito mais adiante.

    Está função cria todo o aparato gráfico necessário para a
    animação:

      - cria uma janela w_quadrante para representar um 
        quadrante;
      - desenha na janela as estrelas;
      - desenha na janela cada um dos astros e
      - desenha na janela cada uma das turtleships.

    Além disso, para cada turtleship é criada uma turtle.
    Essas turtles serão guardadas em uma lista de turtles.
    A janela e a lista de turtles serão retornadas pela função
    para serem mais tardes usadas pela função atualize.
    ''' 
    #------------------------------------------------------#
    # PARTE 1. Criação da janela para representrar o 
    #          quadrante
    # 

    # cria a janela da simulação = window do quadrante
    w_quadrante = turtle.Screen()

    # cor de fundo da janela será preto
    w_quadrante.bgcolor("black")

    # Coloca um título na barra superior da janela
    w_quadrante.title("Turtlenautas")

    # a janela representará a região do espaço que 
    # tem o canto inferior esquerdo na coordenada (llx,lly) e
    # tem o canto superior direito  na coordenada (rux,ruy) 
    llx = -320000 # l_cantos[0]
    lly = -300000 # l_cantos[1]
    urx =  320000 # l_cantos[2]
    ury =  300000 # l_cantos[3]

    # Fixamos a área do 'quadrante' como sendo de 
    # 96.000.000.000 km**2 = 96 bilhões de quilômetros quadrados
    w_quadrante.setworldcoordinates(llx,lly,urx,ury)

    # definimos o tamanho da janela em pixels?
    # hmmm, será que é bom fixar?!
    # os valores default são uma porcentagem da tela: 
    #
    #      width  == 0.5  que corresponde a 50% da largura da tela
    #      height == 0.75 que corresponde a 75% da altura  da tela
    # 
    # se os valores de width e height forem inteiros, então 
    # eles são considerados como sendo número de pixels.
    # por exemplo:
    # 
    #    width  = 800
    #    height = 675
    #
    # depois basta fazermos 
    #
    #    w_quadrante.setup(width,height)
    #
    # hmmm, vamos deixar width e height variáveis em função da tela 
    # do computador, ok?!
    width  = w_quadrante.window_width()
    height = w_quadrante.window_height()

    # estamos considerando que a janela tem width x height
    # s_pixel é aproximadamente o 'comprimento de um pixel' 
    # em relação  ao quadrante        
    s_pixel = (urx - llx)/width # chute aproximado

    # vamos enfrescurar a janela com algumas estrelas
    # delay 1 para desenhar as estrelas na janela mais 
    # rapidamente
    w_quadrante.delay(1)

    # aumentando o valor do argumento de tracer tornamos
    # o surgimento das estrelas na janela aparentemente instantâneo
    w_quadrante.tracer(500)

    # desenhe 200 estrelas
    n_estrelas = 200
    desenhe_estrelas(w_quadrante,llx,lly,urx,ury,n_estrelas)

    # vamos agora dimibuir o valor do argumento de tracer 
    #   para que não de impressão que as turtleships estão se 
    #   "teletransportando" ou passando por um "wormehole" na janela.
    w_quadrante.tracer(100)
 
    #------------------------------------------------------#
    # PARTE 2. Desenho do astros na janela w_quadrante
    # 

    # agora vamos desenhar os astros

    # cada astro é representado por uma lista
    #
    #   [[x_a,y_a], massa_a, raio_a, cor_a, nome_a]
    #
    # onde 
    #
    #    - [x_a,y_a] é a posição do astro
    #    - massa_a   é a massa do astro
    #    - raio_a    é o raio do astro
    #    - cor_a     é a cor do astro
    #    - nome_a    é o nome do astro
    #

    # cria uma tartaruga para desenhar os astros
    t = turtle.Turtle()

    # não queremos deixar rastros no espaço enquanto desenhamos
    t.penup()

    # esconde a tartaruga
    t.hideturtle() 
    for astro in l_astros: 
        # pegue os dados do astro 
        x_a       = astro[0][0]
        y_a       = astro[0][1]
        # massa_a = astro[1]  para desenhar não precisamos da massa
        raio_a    = astro[2]
        cor_a     = astro[3]
        # nome_a    = astro[4] para desenhar não precisamos do nome

        # coloque t na posição do astro
        t.setposition(x_a,y_a)

        # vamos definir o tamanho do planeta proporcional ao seu raio
        # Vixe!
        # ? multiplicar por 2 para não ficar muito pequeno...
        diâmetro = 2*int(raio_a/s_pixel) 

        # print("--- ra = %f size = %d cor = %s" %(raio_a,sz,cor_a))

        # hmmm. o diâmetro de um astro deve ser pelo menos 4
        # se não for assim, não dá para enxergar a lua...
        if diâmetro < 4: diâmetro = 4 

        # desenhamos um ponto e acabou esta parte... ufa!
        t.dot(diâmetro,cor_a) 

   
    #------------------------------------------------------#
    # PARTE 3. Desenho da turtleships e criação de uma lista
    #      de turtles: para cada turtleship teremos uma 
    #      turtle na lista
    # 
 
    # bem, agora vamos desenhar as turtleships e criar uma
    # lista de referências para cada uma das turtles: uma
    # turtle para cada turtleship
    # Vixe! Vixe!
    l_turtle_turtleships =[]

    # cada turtleship é representada por uma lista
    #
    #  [[x_t,y_t], [v_x_t,v_y_t], cor_t, nome_t, ativa_t]
    # 
    # onde 
    # 
    #  - (x_t,y_t)     é a posição inicial da nave
    #  - (v_x_t,v_y_t) é a velocidade inicial da nave
    #  - cor_t         é a cor da nave
    #  - nome_t        é o nome da nave
    #  - ativa_t       é um flag que indica se a nave está ativa

    for turtleship in l_turtleships:
        #pegue os dados das turtleship
        x_t       = turtleship[0][0] # float
        y_t       = turtleship[0][1] # float
        v_x_t     = turtleship[1][0] # float
        v_y_t     = turtleship[1][1] # float
        cor_t     = turtleship[2]    # string
        # nome_t  = turtleship[3]    # string, não vamos usar
        # ativa_t = turtleship[4]    # boolean, não vamos usar aqui
                                     # sabemos que inicialmente ativa_t == True
        # crie uma tartaruga
        t = turtle.Turtle() 

        # o desenho da turtle será o de uma tartaruga
        t.shape("turtle")

        # vamos definir a cor desta turtle
        t.color(cor_t)

        # vamos fazer as turtles um pouco menores 
        # (0.5,0.5) é um chute ... o tamanho original é o dobro...
        t.shapesize(0.5,0.5)

        # ainda não queremos que haja rastro
        t.penup()

        # levamos a turtle para sua posição inicial
        t.setposition(x_t,y_t)

        # agora queremos que o rastro seja mostrado 
        t.pendown()

        # hmmm, agora temos que virar a turtle para olhar
        # no sentido em que está se movendo 
        # t.radians()  # parece que é melhor trabalhar com radianos
        #              # ... voltamos  para graus ...

        # calculamos uma aproximação do ângulo do vetor (v_x_t,v_y_t)
        ang = ângulo(v_x_t,v_y_t) # aproximação do ângulo em graus

        # viramos a turtle para que 'olhe por onde anda'
        t.setheading(ang) # vira a tartaruga

        # print("Ângulo = %f" %t.heading())
        l_turtle_turtleships.append(t)

    # acaba de desenhar tudo antes de esperar um pouquinho para 
    # começar a animação
    w_quadrante.update()

    # espera 1 segundo antes de começar a animação
    # assim dá para ver onde estão os astros e as turtleships
    # e depois começa tudo
    time.sleep(1)
    
    return [w_quadrante, l_turtle_turtleships]

#----------------------------------------------------------#
#                                                          #
# ATUALIZE                                                 #
#                                                          #
#----------------------------------------------------------#

def atualize(quadrante, l_turtleships):
    ''' ([janela, lista de turtle], lista de turtleSips) ->  None

        Recebe a janela da simulação, a lista de turtles e a lista de
        turtleships, onde:

            - quadrante[0]  é a referência para a janela;
            - quadrante[1]  é a referência para a lista de turtles, e
            - l_turtleships é a lista de turtleships.

        Cada item na lista ´l_turtleships´ tem a seguinte forma

              [[x_t,y_t], [v_x_t,v_y_t], cor_t, nome_t, ativa_t]
         
        onde 
         
             - [x_t,y_t]     é a posição da nave
             - [v_x_t,v_y_t] é a velocidade da nave
             - cor_t         é a cor da nave
             - nome_t        é o nome da nave
             - ativa_t       indica se a nave está operacional

        Nessa função cor_t, nome_t são irrelevantes.

    '''
    # vamos recuperar a janela da simulação = window do quadrante
    # w_quadrante = quadrante[0] # não está usando aqui, mas
    # usamos no final da função simule em ep3.py

    # vamos recuperar a lista das turtles
    l_turtle_turtleships = quadrante[1]
 
    # bem, agora vamos mover as turtles associadas às turtleships, 
    # uma após outra
    i = 0
    for turtleship in l_turtleships:
        #pegue os dados da turtleships
        x_t     = turtleship[0][0] # float
        y_t     = turtleship[0][1] # float
        v_x_t   = turtleship[1][0] # float
        v_y_t   = turtleship[1][1] # float
        ativa_t = turtleship[4]    # bool
 
        # pegue uma turtle
        t = l_turtle_turtleships[i]
       
        # vixe, a ordem das turtleships nas listas
        # l_turtleships e l_turtle_turtleships deve ser
        # compatível 
        i = i + 1
         
        if  not ativa_t or fora_do_quadrante(x_t,y_t):
            # tornamos a turtle invisível, pois a turtleship deve 
            #   ter colidido com algum planeta ou saído do quadrante
            t.hideturtle()
            t.penup()  # para quando a turtle voltar ao quadrante

        else:
            # hmmm. aqui tem uma coisa perigosa...
            # não temos muito controle sobre os valores de x_t e y_t
            # que podem ser muuuiito grande
            # 
            # ok, paramos de atualizar a posição da turtle 
            #     se ela estiver fora do quadrante...

            # levamos a turtle para a sua nova posição 
            t.setposition(x_t,y_t)

            # hmmm. como agora estamos escondendo a turtle sempre que 
            # ela sai do quadrante precisamos torná-la visivel quando
            # volta...
            if not t.isvisible():
                t.showturtle()
                t.pendown()
                
            # hmmm, agora temos que virar a tartaruga para olhar
            # no sentido em que está se movendo 
            ang = ângulo(v_x_t,v_y_t) # aproximação do ângulo
            t.setheading(ang)         # vira a tartaruga


    # não precisamos retornar nada
    # return quadrante


#----------------------------------------------------------#
#                                                          #
# DESENHE_ESTRELA                                          #
#                                                          #
#----------------------------------------------------------#

def desenhe_estrelas(w, llx, lly, urx, ury, n):
    '''(janela, número, número, número, número, natural) -> None

        Recebe uma janela w e um número inteiro n e desenha na 
        janela n estrelas de  diâmetro 1 (chute).
    '''

    # inicialize a semente do gerador (como no EP1)
    # como feito no EP1
    random.seed()

    # hmmm, precisamos acerta o diâmetro das estrelas...
    diâmetro = 1 # hmmm, este diâmetro é um chute.
    cor = "white" # estrelas serão brancas

    t = turtle.Turtle()
    t.penup() # não queremos deixar rastros no espaço
    t.hideturtle() # não queremos que a tartaruga seja vista
    for i in range(n):
        # sorteie uma posição do espaço
        x = random.randint(llx,urx)
        y = random.randint(lly,ury)

        # vá para está posição 
        t.setpos(x,y)

        # coloque um ponto
        t.dot(diâmetro,cor)
 
#----------------------------------------------------------#
#                                                          #
# ÂNGULO                                                   #
#                                                          #
#----------------------------------------------------------#

def ângulo(v_x,v_y): 
    '''(número,número) -> int

        Recebe o vetor (v_x,v_y) e retorna uma aproximação do 
        ângulo  que o vetor forma com o eixo das abscissas.
        O ângulo é retornado em graus.
        
    '''

    try:
        # atan retorna ângulo em radianos
        ang = math.atan(v_y/v_x)

        # degrees converte para graus
        ang = math.degrees(ang)

        # arredonda para inteiro
        ang = round(ang)

        # acerta os quadrantes
        if v_x < 0:
            ang = ang + 180
        elif ang < 0:
            ang = ang + 360
    except:
        # v_x é zero ou quase zero
        # isto faz que tenhos uma "excessão"
        if v_y > 0:
           ang = 90
        else:
           ang = 270

    return ang

#----------------------------------------------------------#
#                                                          #
# FORA_DO_QUADRANTE                                        #
#                                                          #
#----------------------------------------------------------#
def fora_do_quadrante(x,y):
    '''(número, número) -> bool

       Recebe a posição (x,y) de uma turtleship e retorna True
       se ela estiver fora do quadrante. Em caso contrário 
       a função retorna False.
    '''

    # a janela representará a região do espaço que 
    # tem o canto inferior esquerdo na coordenada (llx,lly) e
    # tem o canto superior direito  na coordenada (rux,ruy) 
    llx = -320000 # l_cantos[0]
    lly = -300000 # l_cantos[1]
    urx =  320000 # l_cantos[2]
    ury =  300000 # l_cantos[3]
  
    if x < llx or x > urx or y < lly or y > ury:
        return True

    return False
