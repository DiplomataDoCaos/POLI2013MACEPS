#***************************************************************#
#**                                                           **#
#**   Nome do aluno: Fernando Talietta  Número USP:8582828    **#
#**   Exercício-Programa 3                                    **#
#**   Professor: José Augusto                                 **#
#**   Turma: 1                                                **#
#**                                                           **#
#***************************************************************#

#############################################################
#                                                           #                 
#  MÓDULO ep3.py                                            #
#                                                           #
#  Modulo responsável pela simulação do movimento das naves.#
#                                                           #
#  Você deverá escrever 5 funções deste módulo:             #
#                                                           #
#      - crie_turtleship;                                   #
#      - crie_lista_turtleships;                            #
#      - atualize_turtleship;                               #
#      - houve_colisão; e                                   #
#      - simule.                                            #
#                                                           #
#  Neste momento o programa já pode ser utilizado com a     # 
#  opção 'a' para o cálculo da aceleração gravitacional     #
#  e para testar a opção 'r' de cálculo da aceleração       #
#  resultante.                                              #
#                                                           #
#  Para testar a opção 's' é necessário que você escreva    #
#  e teste cada uma das funções acima.                      #
#                                                           #
#  Trabalhe somente na área indicada e não altere as demais #
#  partes do programa. A palavre "TAREFA" indica as partes  # 
#  do programa que você deve escrever                       #
#                                                           #
#  Não altere o nome do arquivo.                            #
#                                                           #
#  Não importe outros módulos além dos já importados.       #
#                                                           #     
#############################################################

# necessária para o sys.exit()
import sys

# newton é o módulo com as função: 
#     - distância;
#     - aceleração_gravitacional; e 
#     - aceleração_resultante.
# para usar essas funções use a chamada "dot notation",
# ou seja, escreva o nome do módulo seguido de ponto 
# e do nome da função. Por exemplo
#
#     newton.distância([0,0],[1,1])
#
import newton

# animacao é o nome do módulo com as funções responsáveis 
# pela animação da simulação:
#     - crie_quadrante(l_astros, l_turtleships)
#     - atualize(quadrante, l_turtleships)
# para usar estas funções neste programa escrevemos
#   animacao.crie_quadrante(...) e animacao.atualize()
#
import animacao

# CONSTANTES == opções (flags/indicadores) que para 
# serem usados na fase de desenvolvimento e 
# teste do programa

# CONSTANTES referentes ao arquivo e lista de palavras
MOSTRE_ARQUIVO    = False # mostra o conteúdo do arquivo
MOSTRE_L_PALAVRAS = False # mostra a lista de palavras do arquivo

# CONSTANTES referentes a mostrar os astros 
MOSTRE_L_ASTROS   = False # mostra a lista de astros 
MOSTRE_L_TURTLES  = False # mostra a lista de turtleships

# CONSTANTE que deve ser True enquanto as funções: 
#      - crie_turtleship;                                   
#      - crie_lista_turtleships;                            
#      - atualize_turtleship; e                              
#      - houve_colisão.
# estiverem sendo testadas através do Python Shell
TESTE_FUNÇÕES = False  # True faz com que a execução do programa 
                      # seja encerrada antes da leitura do arquivo.
                      # Desta forma quando o programa estiver sendo 
                      # executado no Idle as funções poderão ser
                      # chamadas uma a uma através do Python Shell
                     

# CONSTANTE que deve ser True enquando a função simule estiver 
# sendo testada
# ATENÇÃO: esta constante só pode ser True depois de todas as 
# demais funções já terem sido feitas e testadas
TESTE_SIMULE = False # mostra a posição das turtleships em cada 
                     # passo da simulação

# CONSTANTE que deve ser True para que a animação seja exibida
# ATENÇÃO: esta constante só pode ser True depois de todas as
# funções do módulo newton e deste arquivo tiverem sido feitas
# e testadas 
MOSTRE_ANIMAÇÃO = True # mostra a animação
                        # ATENÇÃO: esta opção só deve ser colocada 
                        #   com True quando TODO o resto do programa
                        #   tiver sido testado e passado nos testes

#----------------------------------------------------------#
#                                                          #
# MAIN: programa principal.                                #
#                                                          #
#----------------------------------------------------------#
def main():

    # PARTE 1: Manipulação do Arquivo de Dados 
    #
    # Esta parte contém:
    #   
    #   - leitura do nome do arquivo
    #   - abertura do arquivo  (open(nome_arquivo,"r"))
    #   - leitura do texto no arquivo (f_dados.read())
    #   - fechamento do arquivo  (f_dados.close())
    #   - criação de uma lista com as palavras do texto (.rsplit())
    #

    # o trecho de código a seguir será útil para testar as Tarefas 4 a 7 
    # através Python Shell
    if TESTE_FUNÇÕES:
        return # mantém as funções carregadas no Python Shell

    # leia o nome do arquivo de dados
    nome_arquivo = input("Digite o nome do arquivo: ")

    # abra o arquivo
    # a variável f_dados é uma referência ao arquivo  
    try:
        f_dados = open(nome_arquivo,"r")
        # f_dados = open(nome_arquivo,"r",encoding="utf8")
    except:
        print("Opsss. Arquivo '" + nome_arquivo + "' não pode ser aberto.")
        print("Verifique o nome do arquivo e se você está na pasta certa.")
        sys.exit()
    
    # read() lê o arquivo _inteiro_ como um string/texto que será 
    # referenciado pela variável texto_no_arquivo  
    texto_no_arquivo = f_dados.read()

    # f_dados deve ser fechado
    f_dados.close()
    
    # o trecho de código a seguir mostra o conteúdo do arquivo 
    # ('texto_no_arquivo')
    # se MOSTRE_ARQUIVO == True
    if MOSTRE_ARQUIVO:
        print("----- Início do conteúdo do arquivo")
        print(texto_no_arquivo)
        print("----- Fim    do conteúdo do arquivo\n")
        pause()

    # aqui termina a parte do programa que manipula o arquivo de entrada
    #------------------------------------------------------------------
    
    # agora criaremos uma lista de palavras do arquivo 
    # lista_palavras receberá todas as palavras (sequências sem espaços) 
    # que estão no arquivo 
    lista_palavras = texto_no_arquivo.rsplit()

    # o trecho de código a seguir mostra o conteúdo de 'lista_palavras' se 
    # MOSTRE_L_PALAVRAS == True
    if MOSTRE_L_PALAVRAS:
        print("----- Início da lista de palavras no arquivo")
        print(lista_palavras)
        print("----- Fim    da lista de palavras no arquivo\n")
        pause()

    # aqui termina a parte do programa que cria a lista de palavras
    #------------------------------------------------------------------

    #----------------------------------------------------------#
    # PARTE 2: Simulação das Instrução no Arquivo
    #
    # Neste ponto do programa `lista_palavras` é uma lista que contém 
    # as palavras do arquivo dado.
    # 
    # Nesta parte do programa percorreremos a lista de palavras e 
    # e executaremos cada uma das instruções encontradas. 
    # A variável ´i´ indica o índice da palavra que esta sendo 
    # manipulada 

    # n é o comprimento da lista de palavras
    n = len(lista_palavras)

    # i é o índice da próxima palavra a ser processada 
    i = 0
    while i < n:
        # ------------------------------------------------------#
        # calcule a aceleração gravitacional de um astro sobre  #
        # um ponto                                              #
        #-------------------------------------------------------#
        if lista_palavras[i] == 'a':
            print("Opção [a]:")            

            # pula o caractere 'a'
            i = i + 1

            # crie uma lista com informações como a posição, massa, ... 
            # do astro celeste
            astro, i = crie_astro(lista_palavras,i) 

            # crie lista com um ponto
            ponto, i = crie_ponto(lista_palavras,i)

            # calcule a aceleração gravitacional do astro no ponto
            a = newton.aceleração_gravitacional(astro, ponto, False)

            # imprima as informações sobre o astro
            imprima_astro(astro)

            # imprima o ponto e aceleração gravitacional
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
            print("  Posição do ponto = (%.2f,%.2f)" %(ponto[0],ponto[1]))
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
            print("  Aceleração       = (%.2f,%.2f)" %(a[0],a[1]))

        elif lista_palavras[i] == 'r':
        # ------------------------------------------------------#
        # calcule a aceleração gravitacional resultante da      #
        # ação de vários astros celeste sobre um ponto          #
        #                                                       #
        #-------------------------------------------------------#
            print("Opção [r]:")            
            
            # pegue primeiro o número de astros
            n_a = int(lista_palavras[i+1]) 

            # atualize o índice da próxima palavras a ser 
            # processada, pula 'r' e o valor de n_a
            i = i + 2

            # construa uma lista de astros celetes
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
            # i  é o índice da posição inicial dos dados 
            #
            lista_astros, i = crie_lista_astros(lista_palavras,i,n_a)

            # crie lista com um ponto
            ponto, i = crie_ponto(lista_palavras,i)

            # calcule a aceleração_resultante
            a = newton.aceleração_resultante(lista_astros,ponto,False)

            # imprima dados sobre os astros 
            for astro in lista_astros:
                imprima_astro(astro)

            # imprima o ponto e aceleração resultante
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
            print("  Posição do ponto = (%.2f,%.2f)" %(ponto[0],ponto[1]))
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
            print("  Aceleração       = (%.2f,%.2f)" %(a[0],a[1]))

        elif lista_palavras[i] == 's':
        # ------------------------------------------------------#
        # simule a trajetoria uma lista de turtleships sobre    # 
        # a ação gravitacional de uma lista de astros celestes. #
        #                                                       #
        #-------------------------------------------------------#
            print("Opção [s]:")            

            # pegue o número de astros
            n_a = int(lista_palavras[i+1])

            # pula a opção 's' e o valor de n_a
            i = i + 2

            # construa uma lista de astros celetes
            # cada astro é representado por uma lista
            #
            #   [[x_a,y_a], massa_a, raio_a, cor_a, nome_a]
            #
            # onde 
            #
            #    - [x_a,y_a] é a posição do astro
            #    - massa_a       é a massa do astro
            #    - raio_a é  o raio do astro
            #    - cor_a  é a cor do astro
            #    - nome_a é o nome do astro
            #
            # i  é o índice da posição inicial dos dados  
            lista_astros, i = crie_lista_astros(lista_palavras,i,n_a)

            # imprima dados sobre os astros 
            for astro in lista_astros:
                imprima_astro(astro)

            # pegue o número de turtleships
            n_t = int(lista_palavras[i])

            # pule a palavra com n_t
            i = i + 1

            # crie uma lista com ´n_t´ turtleships
            # cada turtleship é representada por uma lista
            #
            #  [[x_t,y_t], [v_x_t,v_y_t], cor_t, nome_t, ativa_t]
            # 
            # onde 
            # 
            #  - [x_t,y_t]     é a posição inicial da turtleship
            #  - [v_x_t,v_y_t] é a velocidade inicial da turtleship
            #  - cor_t         é a cor da turtleship
            #  - nome_t        é o nome da turtleship
            #  - ativa_t indica se a turtleship está operacional e 
            #            inicialmente é True
            lista_turtleships, i = crie_lista_turtleships(lista_palavras,i,n_t)

            # imprima os dados sobre a turtleship 
            for turtleship in lista_turtleships:
                imprima_turtleship(turtleship)

            # pegue o tempo máximo de simulação ´t_max´ e o 
            #   intervalo ´delta_t´ entre as 
            #   atualizações das posições e velocidade das tartarugas
            t_max   = float(lista_palavras[i])
            delta_t = float(lista_palavras[i+1])


            # imprima valores usados na simulação
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . .")            
            print("  Tempo máximo de simulação       = %10.2f horas" %t_max)
            print("  Intervalo de tempo da simulação = %10.3f horas" %delta_t)
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
            pause()
 
            # atualize o índice usado para percorrer a lista
            i = i + 2

            simule(lista_astros,lista_turtleships,t_max,delta_t) 


        # ------------------------------------------------------#
        # Opção inválida.                                       #
        # Erro no formato do arquivo de entrada?!               #
        #-------------------------------------------------------#
        else: 
            print("Opção desconhecida. Erro no arquivo de dados!?")
            sys.exit()

        # espera por ENTER antes de processar a próxima opção
        pause()

    print("\nFim do processamento\n")


#----------------------------------------------------------#
#                                                          #
# CRIE_TURTLESHIP                                          #
#                                                          #
#----------------------------------------------------------#

    '''(lista strings, int) -> [[float,float],[float,float],string,string,bool], int
  
    Recebe uma lista de palavras ´l_palavras´ e um índice ´i´
    da lista e retorna uma lista com a representação de uma 
    turtleship e um valor para a atualização do índice ´i´.

    A lista tem a forma

         [[x_t,y_t], [v_x_t,v_y_t], cor_t, nome_t, ativa_t]

    onde:

         - x_t     é o float  representado na posição i, 
         - y_t     é o float  representado na posição i+1,
         - v_x_t   é o float  representado na posição i+2,
         - v_y_t   é o float  representado na posição i+3,
         - cor_t   é o string da posição i+4.
         - nome_t  é o string da posição i+5
         - ativa_t é um bool que inicialmente será True
   
       Dica: para fazer esta função você pode se inspirar na 
             função crie_astro.

       Pré-condições: 
          A função supõe que a lista l_palavras possui itens 
          nas posição i,i+1,...,i+5.

          Além, disso a função supõe que os strings l_palavras[i] 
          l_palavras[i+1], l_palavras[i+2] e l_palavras[i+3],
          contém representações válidas de floats como string. 

    '''
    # TAREFA 4: escreva o corpo desta função (4 = 1 + 3 do módulo newton)
    
def crie_turtleship(l_palavras,i):
    lista_organizada=[]
    lista_organizada.append([float(l_palavras[i]),float(l_palavras[i+1])])
    lista_organizada.append([float(l_palavras[i+2]),float(l_palavras[i+3])])
    lista_organizada.append(l_palavras[i+4])
    lista_organizada.append(l_palavras[i+5])
    lista_organizada.append(bool(True))
    i=i+6 #a lista apresenta os dados de forma contínua, o indice é usado para se continuar o processo para outra chamada ou diferente processo
    return(lista_organizada,i)

#----------------------------------------------------------#
#                                                          #
# CRIE_LISTA_TURTLESHIP                                    #
#                                                          #
#----------------------------------------------------------#

    '''(lista strings, int, int) -> lista de turtleships, int
  
       Recebe uma lista de palavras ´l_palavras´, um índice ´i´ e um
       número ´n_t´ de turtleships e retorna uma lista com n_t itens 
       e uma valor para a atualização do índice i.

       Cada item da lista retornada representa uma turtleship e tem 
       a forma

               [[x_t,y_t],[v_x_t,v_y_t],cor_t,nome_t,ativa_t],

       onde:

           - x_t    é o float representado na posição i; 
           - y_t    é o float representado na posição i+1;
           - v_x_t  é o float representado na posição i+2;
           - v_y_t  é o float representado na posição i+3;
           - cor_t  é o string da posição i+4; e
           - nome_t é o string da posição i+5.
           - ativa_t é um bool que inicialmente é True

       Esta função DEVE utilizar a função crie_turtleship.
       
       Dica: para fazer esta função você pode se inspirar na 
             função crie_lista_astros 

       Pré-condições:
          A função supõe que a lista l_palavras possui itens 
          nas posição i,i+1,...,i+5,...,...,i+6*nt-1 
 
          Além disso, a função supõe que os strings que devem 
          representar floats são representações válidas de floats.
    '''
    # TAREFA 5: escreva o corpo desta função
    
def crie_lista_turtleships(l_palavras,i,n_t):
    lista_turtleships=[]
    for z in range (n_t):
        a,i=crie_turtleship(l_palavras,i)        
        lista_turtleships.append(a)
    return(lista_turtleships,i)

#----------------------------------------------------------#
#                                                          #
# HOUVE_COLISÃO                                            #
#                                                          #
#----------------------------------------------------------#

    '''(turtleship, lista de astros) -> bool

    Recebe 
 
        - uma referência a uma turtleship através de ´turtleship´,
        - uma referência a uma lista de astros através de ´lista_astros´

    e retorna True se a turtleship colidiu com algum astro, em
    caso contrário a função retorna False.  
 
    Em caso de colisão de uma turtleship com um astro a função DEVE 
    imprimir uma mensagem indicando que houve colisão e informar:
 
        - o nome da turtleship;
        - a cor  da turtleship;
        - o nome do astro; e
        - a cor do astro.

    Esta funcão DEVE usar a função distância do módulo newton.

    Pré-condição: 
        A função supõe que a turtleship está ativa.   
    '''
    # TAREFA 6: escreva o corpo desta função
    
def houve_colisão(turtleship, lista_astros):
    for i in range (len(lista_astros)):
        if lista_astros[i][2]>= newton.distância(turtleship[0],lista_astros[i][0]):
            print("Então...acho que alguém morreu...")
            print("Nome do azarado:",turtleship[3])
            print("Cor do infeliz",turtleship[2])
            print("Ganhou nova cratera:",lista_astros[i][4])
            print("Cor da coisa redonda:",lista_astros[i][3])
            return(True)
    return(False)

#----------------------------------------------------------#
#                                                          #
# ATUALIZE_TURTLESHIP                                      #
#                                                          #
#----------------------------------------------------------#

    '''(turtleship, lista de astros, número) -> None

    Recebe 
 
        - uma referência a uma turtleship através de ´turtleship´,
        - uma referência a uma lista de astros através de ´lista_astros´
        - um intervalo de tempo ´delta_t´

    A turtleship é representada através de uma lista que tem 
    a forma

        [[x_t,y_t], [v_x_t,v_y_t], cor_t, nome_t, ativa_t]

    onde:

        - [x_t,y_t]     é a posição da turtleship em um instante t
        - [v_x_t,v_y_t] é a velocidade da turtleship em um instante t
        - cor_t         é a cor da turtleship   (irrelevante nesta função)
        - nome_t        é o nome da turtleship  (irrelevante nesta função)
        - ativa_t indica se a turtleship está operacional e 
                        inicialmente é True.    (irrelevante nesta função)

    Esta função deve calcular a posição e velocidade da turtleship no 
    instante t+delta_t e atualizá-las. 

    Está função DEVE usar a função aceleração_resultante do módulo
    newton.

    Pré-condição: 
        A função supõe que a turtleship está ativa.   
    '''
    # TAREFA 7: escreva o corpo desta função
    
def atualize_turtleship(turtleship, lista_astros, delta_t):
    a=newton.aceleração_resultante(lista_astros,turtleship[0])
    turtleship[0][0]= turtleship[0][0]+(turtleship[1][0]*delta_t)+(1*a[0]*delta_t*delta_t/2)
    turtleship[0][1]= turtleship[0][1]+(turtleship[1][1]*delta_t)+(1*a[1]*delta_t*delta_t/2)
    turtleship[1][0]= turtleship[1][0] + (a[0]*delta_t)
    turtleship[1][1]= turtleship[1][1] + (a[1]*delta_t)

#----------------------------------------------------------#
#                                                          #
# SIMULE                                                   #
#                                                          #
#----------------------------------------------------------#

def simule(lista_astros, lista_turtleships, t_max, delta_t):
    '''(lista de astros, lista de turtleships, float, float) -> None

    Recebe 

        - uma lista de astros ´lista_astros´,
        - uma lista de turtleship ´lista_turtleships´
        - o tempo máximo ´t_max´ de simulação 
        - intervalo de tempo ´delta_t´ 

    e simula as trajetórias das turtleships em ´lista_turtleships´
    sob o efeito da força gravitacional exercida pelos pelos
    astros em ´lista_astros´. 

    O instante inicial da simulação é zero e a cada 
    passo da simulação o tempo de simulação é acrescido
    de ´delta_t´. 

    As posições da turtleships serão atualizadas em cada passo da 
    simulação. Uma turtleship será desativada assim que colodir
    com algum astro. 

    Não serão consideradas colisões entre turtleships.

    A simulação termina quando o tempo de simulação
    ultrapassar ´t_max´ ou quando não houver nenhuma turtleship
    ativa (todas turtleships colidiram com algum astro).

    Esta função DEVE usar as funções atualize_turtleship e 
    houve_colisão.
    '''
    # TAREFA 8: complete o corpo desta função
    #           comentário com números indicam os passos 
    #           que devem ser tomados para escrever esta função

    # é útil que a opção ´TESTE_SIMULE´ esteja com True durante a fase 
    # de desenvolvimento e testes desta função
    if TESTE_SIMULE:
        # no início da simulação imprima todas as informações as
        # informações sobre os astros e turtleships    
        print("\n**********************************************************")
        print("Início da simulação\n")
        # imprima informações sobre os astros 
        for astro in lista_astros:
            imprima_astro(astro)

        print("\n--------------------------------------------------------")
        print("  Tempo de simulação   = %10.3f horas\n" %0)
        for turtleship in lista_turtleships:
            imprima_turtleship(turtleship)
        pause()         

    # se a opção ´MOSTRE_ANIMAÇÃO´ for True a janela
    # com o quadrante, astros e turtleships será criada e exibida 
    if MOSTRE_ANIMAÇÃO:     
        quadrante = animacao.crie_quadrante(lista_astros, lista_turtleships)

    # 1 inicialize o cronômetro
    t=0

    # 2 determine o número de turtleships ativas
    #         inicialmente _todas_ as turtleships estão ativas
    ativas=len(lista_turtleships)


    # 3  enquanto o cronômetro não ultrapassar o tempo 
    #    máximo de simulação e houver alguma turtleship ativa faça
    while t_max>=t and ativas>0:
        # 3.1 percorra a lista de turtleships 
        for i in range(len(lista_turtleships)):
            # 3.1.1 se a turtleship está ativa 
            if lista_turtleships[i][4]==True:
                # 3.1.1.1 atualize a posição e velocidade da turtleship
                atualize_turtleship(lista_turtleships[i],lista_astros,delta_t)
                # 3.1.1.2 se a turtleship colidiu com algum astro
                if houve_colisão(lista_turtleships[i],lista_astros)==True:
                     # 3.1.1.2.1 imprima mensagem indicando que ocorreu 
                     #           uma colisão depois de %.2f horas
                     print("Alguém se ferrou às:","%.2f" %t)
                     # 3.1.1.2.2 atualize o contador de turtleships ativas
                     ativas=ativas-1
                     # 3.1.1.2.3 desative a turtleship que colidiu
                     lista_turtleships[i][4]=False

        # atualize as posições das turtleships na animação 
        if MOSTRE_ANIMAÇÃO:
            animacao.atualize(quadrante,lista_turtleships)

        # 3.2 atualize o cronômetro
        t=t + delta_t
        # é útil que a opção ´TESTE_SIMULE´ esteja com True durante a fase 
        # de desenvolvimento e testes desta função
        if TESTE_SIMULE:
            print("\n--------------------------------------------------------")
            print("  Tempo de simulação   = %10.3f horas\n" %t)
            for turtleship in lista_turtleships:
                imprima_turtleship(turtleship)
            # print("\n") # pula uma linha
            pause()         

    if MOSTRE_ANIMAÇÃO:        
        print("\nClick na janela para fechar a animação")
        quadrante[0].exitonclick()  # que feio ...

    if TESTE_SIMULE:
        print("Fim da simulação\n")
        print("**********************************************************\n")


#----------------------------------------------------------#
#                                                          #
# CRIE_PONTO                                               #
#                                                          #
#----------------------------------------------------------#

def crie_ponto(l_palavras,i):
    '''(lista de strings, int) -> [float,float], int

       Recebe uma lista de palavras ´l_palavras´ e um índice ´i´
       da lista e retorna uma lista [x,y] e a atualização para o
       índice i.

       Os elementos da lista acima são tais que: 

           - x é o float representado na posição i e 
           - y é o float representado na posição i+1.

       Pré-condição: 
          A função supõe que os strings l_palavras[i] 
          e l_palavras[i+1] são representações válidas de floats 
          como string.
     '''

    # crie lista com uma a posição
    x = float(l_palavras[i])
    y = float(l_palavras[i+1])

    # retorne o ponto e a atualização do índice
    return [x,y], i+2


#----------------------------------------------------------#
#                                                          #
# CRIE_ASTRO                                               #
#                                                          #
#----------------------------------------------------------#

def crie_astro(l_palavras,i):
    '''(lista strings, int) -> [[float,float],float,float,string,string], int
  
       Recebe uma lista de palavras ´l_palavras´ e um índice ´i´
       da lista e retorna uma lista e a atualização para o índice
       ´i´.

       A lista tem a forma

           [[x_a,y_a],massa_a,raio_a,cor_a,nome_a] 

       onde:

           - x_a     é o float representado na posição i; 
           - y_a     é o float representado na posição i+1;
           - massa_a é o float representado na posição i+2;
           - raio_a  é o float representado na posição i+3;
           - cor_a   é o string da posição i+4; e
           - nome_a  é o string da posição i+5.

       Pré-condições:
          A função supõe que a lista ´l_palavras´ possui itens 
          nas posição i,i+1,...,i+5. 
 
          Além disso, a função supõe que os strings
          l_palavras[i],l_palavras[i+1],l_palavras[i+2] e
          l_palavras[i+3] são representações válidas de floats.
     '''
 
    # crie lista com a posição do astro celeste
    posição_a, i = crie_ponto(l_palavras,i) # posição_a = [x_a,y_a]
    # i = i + 2

    # pegue massa do astro 
    massa_a   = float(l_palavras[i])

    # pegue raio do astro 
    raio_a   = float(l_palavras[i+1])
    
    # pegua a cor do astro
    cor_a = l_palavras[i+2] # strings são imutáveis

    # pegue o nome do astro
    nome_a = l_palavras[i+3]

    # crie lista com informações sobre o astro
    astro = [posição_a,massa_a,raio_a,cor_a,nome_a]

    # retorne a representação do astro e atualização do índice
    return astro, i+4

 
#----------------------------------------------------------#
#                                                          #
# CRIE_LISTA_ASTROS                                        #
#                                                          #
#----------------------------------------------------------#

def crie_lista_astros(l_palavras,i,n_a):
    '''(lista strings, int) -> lista de astros, int
    
    Recebe uma lista de palavras ´l_palavras´ e um índice ´i´ da
    lista e um número ´n_a´ de astros e retorna uma lista com ´n_a´
    itens e retorna a atualização para o índice ´i´.

    Cada item representa um astro e tem a forma 

        [[x_a,y_a],massa_a,raio_a,cor_a,nome_a]

    onde:

        - x_a     é o float representado na posição i; 
        - y_a     é o float representado na posição i+1;
        - massa_a é o float representado na posição i+2;
        - raio_a  é o float representado na posição i+3;
        - cor_a   é o string da posição i+4; e
        - nome_a  é o string da posição i+5.

    Pré-condições:
    A função supõe que a lista l_palavras possui itens 
    nas posição i,i+1,...,i+5,..., i+6*nt-1 
    
    Além disso, a função supõe que os strings que devem 
    representar floats são representações válidas de floats.
    '''

    # inicialmente a lista está vazia
    l_astros = []

    # pegue cada um dos astros e insira na lista
    for j in range(n_a): 
        # i  é o índice da posição inicial dos dados  
        # [[x_a,y_a], massa_a, raio_a, cor_a, nome_a] do astro celeste j  
        astro, i = crie_astro(l_palavras,i)

        # insira o astro no final da lista
        l_astros.append(astro)


    if MOSTRE_L_ASTROS:          
         print("----- Início da lista de astros")
         print(l_astros)
         print("----- Fim    da lista de astros\n")

    return l_astros, i

#----------------------------------------------------------#
#                                                          #
# IMPRIMA_ASTRO                                             #
#                                                          #
#----------------------------------------------------------#

def imprima_astro(astro):
    '''(astro) -> None

       Recebe uma lista ´astro´ que representa um astro e 
       imprime todas as informações referentes ao astro.
    '''
    print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
    print("  Nome do astro    =", astro[4])
    print("  Cor              =", astro[3])  
    print("  Posição          = (%.2f,%.2f)" %(astro[0][0],astro[0][1]))
    print("  Massa            =  %.2e" %astro[1])
    print("  Raio             =  %.2d" %astro[2])


#----------------------------------------------------------#
#                                                          #
# MOSTRE_TURTLESHIP                                        #
#                                                          #
#----------------------------------------------------------#

def imprima_turtleship(turtleship):
    '''(turtleship) -> None

       Recebe uma lista ´turtleship´ que representa uma turtleship
       e imprime todas as informações dessa turtleship. 
    '''
    print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
    print("  Nome da turtleship  =", turtleship[3])
    print("  Cor                 =", turtleship[2])
    print("  Posição             = (%.2f,%.2f)" %(turtleship[0][0],turtleship[0][1]))
    print("  Velocidade          = (%.2f,%.2f)" %(turtleship[1][0],turtleship[1][1]))
    print("  Ativa               =", turtleship[4])  
                  


#----------------------------------------------------------#
#                                                          #
# PAUSE                                                    #
#                                                          #
#----------------------------------------------------------#

def pause():
     '''None -> None

        Para a execução do programa até que um ENTER seja teclado.
     '''
     input("Tecle ENTER para continuar.\n")
    

#----------------------------------------------------------#
# chamada do programa principal                            #
# hmmmm.                                                   #
# uma vez programador C, sempre programador  C ... :-)     #
#                                                          #
# há razões pedagógicas e organizacionais para que a       #
# estrutura do programa seja                               #
#                                                          #
# def main()                                               #
#     [...]                                                #
#                                                          #
# # definição das demais funções                           #
# [...]                                                    #
#                                                          #
# # ponto em que o programa começa a ser executado         #
# main()                                                   #
#                                                          #
# INÍCIO DA EXECUÇÃO DO PROGRAMA É AQUI                    #
#                                                          #
#----------------------------------------------------------#

main() 
