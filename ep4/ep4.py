#***************************************************************#
#**                                                           **#
#**   Fernando Talietta                 Número USP:8582828    **#
#**   Exercício-Programa 4                                    **#
#**   Professor: José Augusto                                 **#
#**   Turma: 1                                                **#
#**                                                           **#
#***************************************************************#

import random

def main():#pronto
    """ nothing in nothing hill->vácuo

    É a estrutura principal (dã), a primeira parte é usada para coletar
    os dados para criar o tdorm.(seja por um arquivo ou por input)
    A segunda é dedicada a execução da partida e para receber os comandos do jogador
    durante ela.
    A terceira é para mostrar os resultados do jogador depois dele ter desistido ou vencido."""
    # Coloque aqui o corpo da sua função main
    moves=0 #parte 1
    destruído=False
    a=input("(s)ortear ou (l)er um turtledorm de arquivo:")
    if a=="s":
        b=int(input("O quanto megamalomaniáco você é?(inteiro não nulo):"))
        c=int(input("Defina seu sucker punch(inteiro):"))
        d=input("O quanto a teoria do caos te afeta?(f,m ou d):")
        tdorm=sorteie_turtle_dorm(b,c,d)
    else:
        a=input("digite o nome do arquivo:")
        try:
            arquivo=open(a,"r")
        except:
            print("FAIL")
        tdorm=leia_turtledorm(arquivo)
    while todos_dormindo_no(tdorm)==True or destruído==True: #parte 2
        comando=input("digite as duas coordenas(linha e coluna,separadas por espaço) ou digite 'a' para arregar\
ou 'd' se seu cérebro derreteu")
        if comando=="a":
            resolva_turtle_dorm(tdorm)
        elif comando=="d":
            destruído=True
        else:
            moves=moves +1
            coordenadas=comando.split()
            coordenadas[0]=int(coordenadas[0])
            coordenadas[1]=int(coordenadas[1])
            atualize_turtledorm(tdorm,coordenadas[0],coordenadas[1])
    print("O jogador fez",moves,"até") #parte 3
    if destruído==True:
        print("se mostrar um perdedor, o que droga vc está fazendo na poli?!")
    else:
        print("mostrar que não é do Mackenzie!!!")
    


# Escreva as demais funções
def leia_turtledorm(arquivo):#pronto
    pronto=[]
    for linha in arquivo:
        work=linha.split()
        for i in range(len(work)):
            work[i]=int(work[i])
        pronto.append(work)
    arquivo.close()
    mostre_turtledorm(pronto,"c")
    return(pronto)
    """A função recebe o arquivo e transforma-o em uma matriz operável para o programa, a qual é devolvida"""

def mostre_turtledorm(tdorm,c):#pronto
    linha_inicial="     |"
    linha_de_divisão="-----+"
    for i in range (len(tdorm)):
        número=str(i)
        linha_inicial= linha_inicial + "  "+número+"  |"
        linha_de_divisão+="-----+"
    print(linha_inicial)
    for k in range(0,len(tdorm),1):
        print(linha_de_divisão)
        print(" ",k," ",end="|")
        for l in range(len(tdorm)):
            print(" ",acordado(tdorm[k][l],c)," ", end="|")
        print("")
    print(linha_de_divisão)
    """A função recebe o tdorm e uma string para ser o símbolo, e não devolve nada
    mas gera um print com a imagem do dormitório"""

def acordado(lugar,c):#tirar isso
    if lugar==1:
        d=c
    else:
        d=" "
    return(d)
    """A função recebe um lugar do turtledorm e o símbolo,
    e devolve qual string é que deve ser impressa no mostre_turtledorm""" 
        
def atualize_turtledorm(tdorm,lin,col):#pronta
    mudados=[[col,lin],[col-1,lin],[col+1,lin],[col,lin-1],[col,lin+1]]
    medida=(len(tdorm))
    for i in range(len(mudados)):
        if mudados[i][0]>=0 and mudados[i][0]<=medida-1 and mudados[i][1]>=0 and mudados[i][1]<=medida-1:
            if tdorm[mudados[i][1]][mudados[i][0]]== 0:
                tdorm[mudados[i][1]][mudados[i][0]]=1
            else:
                tdorm[mudados[i][1]][mudados[i][0]]=0
    mostre_turtledorm(tdorm,"c")
    """A função recebe a matriz(lista com listas),a linha e a coluna digitadas
    ela devolve uma versão atualizada da matriz, com as modificações realizadas.

    A função verifica cada tartaruga individualmente e não tenta acordar tartarugas além dos limites
    do turtledorm"""

def todos_dormindo_no(tdorm): #pronta
    pentelho=False
    y=len(tdorm)
    for i in range (y):
        for z in range (y):
            if tdorm[z][i] == 1:
                pentelho=True
    return(pentelho)
    """A função recebe a matriz(lista com listas)
    e devolve se algum das tartarugas está acordada
    na forma de uma bullerana.

    Ela vasculha todos os valores da matriz usando duas listas."""

def sorteie_turtle_dorm(tam,semente,dif): #pronta #escrever melhor o docstring
    tdorm=[]
    a=[]
    for i in range(tam):
        tdorm.append([])
        for j in range(tam):
            tdorm[i].append(0)
    print(tdorm)
    random.seed(semente)
    ref=tam*tam
    if dif=="f":
        inferior=ref*5//100
        superior=ref*20//100
    elif dif=="m":
        inferior=ref*25//100
        superior=ref*50//100
    else:
        inferior=ref*55//100
        superior=ref*85//100
    cont=random.randrange(inferior,superior)#checar se é o certo
    for g in range (cont):
        lin=random.randrange(0,tam)
        col=random.randrange(0,tam)
        atualize_turtledorm(tdorm,lin,col)
    mostre_turtledorm(tdorm,"c")
    return(tdorm)
    """A função recebe o tamanho desejado,a semente para o processo e a dificuldade desejada, e devolve uma matriz
    quadrada de lado pedido, com o intervalo de número de tapinhas desejados definido pela dificuldade """

def resolva_turtle_dorm(tdorm): #aplicar o digito diretamente
    print("é não deu tempo... pode ler o código imcompleto a vontade")
    linha=len(tdorm)
    tam=linha*linha
    best_hits=tam+1
    best=0
    for tenta in range(tam):
        bi=""
        back=tdorm
        conta_chute=0
        teste=[]
        l=0
        for i in range(linha):
            teste.append([])
        for i in range(tam):
            if tenta==0:
                bi=bi + "0"
            else:
                if tenta%2==1:
                    conta_chute=conta_chute+1
                bi=bi+str(tenta%2)
                tenta=tenta//2
        bi=int(bi)
        for i in range(tam):
            teste[l].append(bi%10)
            bi=bi//10
            if len(teste[l])==linha:
                l=l+1
        for lin in range(linha):#tá configurada pra receber uma matriz
            for col in range(linha):
                if teste[lin][col]==1:
                    atualize_turtledorm(back,lin,col)
        if todos_dormindo_no(back)==False and conta_chute < best_hits:
            best_hits = conta_chute
            best = teste
    if best==tam+1:
        print("não há solução")
    else:
        mostre_turtledorm(best,"c")
    
    """a função recebe uma matriz e printa qual é a melhor solução para o caso
    a função utiliza o método da tentativa por força bruta

    """
main()
