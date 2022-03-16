"""
Modulo janela.py
define a classe Janela().

Como utilizar:
1. crie uma janela
2. inicialize uma janela passando como argumentos:
-- um turtledorm
-- o nome da função que trata a opção (d)esistir
-- o nome da função que trata a opção (a)juda
-- o nome da função que trata o clique do mouse sobre um cubículo do turtledorm

Uma vez inicializada, a Janela entra em loop, esperando por que o usuário
clique em um cubículo, ou aperte as teclas 'd' ou 'a'.

"""

import turtle

# constantes
TAM = 30

# ======================================================================

class Janela:
    """
    A classe Janela permite criar uma interface gráfica utilizando o modulo
    turtle do Python, evitando assim a instalação de outros pacotes gráficos.
    Essa interface permite ver um turtledorm e clicar em uma coordenada (dar
    um tapinha em um turtle), para fazer o turtle despertar ou dormir.
    """
# ======================================================================

    def __init__(self):
        """ apenas inicializa o contador de jogadas. Veja também as
        funções incrementa_jogadas e quantas_jogadas.
        """
        self.conta_jogadas = 0
        
# ======================================================================

    def incrementa_jogadas(self):
        """ incrementa a variável de jogadas da janela
        """
        self.conta_jogadas += 1
        
    def quantas_jogadas(self):
        """ retorna o valor atual do contador de jogadas
        """
        return self.conta_jogadas

# ======================================================================

    def crie_janela(self, tdorm, trata_d, trata_a, clicou):
        """ cria a janela, mostra o tdorm e entra em loop
        """
        self.t = turtle.Turtle()
        self.s = turtle.Screen()
        self.s.bgcolor("lightgreen")
        self.s.tracer(3)
        self.n = len(tdorm)
        self.turtledorm = tdorm
        self.s.setworldcoordinates(0,0,(self.n+2)*TAM,(self.n+2)*TAM)

        self.s.onkey(trata_d, 'd')
        self.s.onkey(trata_a, 'a')
        self.s.onclick(clicou)
    
        self.t.penup() # sempre penup; quem baixar a cauda precisa levantar depois
        self.s.listen()
        self.desenhe_turtledorm()
        self.s.mainloop()
    
# ======================================================================

    def termine(self):
        """
        Chame essa função para fechar a janela com um clique no mouse.
        """
        print("Clique na janela para encerrar.")
        self.s.exitonclick()

# ======================================================================

    def converta_para_lincol(self,x,y):
        """ (int, int) -> (int, int)
        converte a posição de um clique na janela
        para um cubículo lin,col na matriz turtledorm.
        Observe que um clique pode ser em uma região fora do
        turtledorm, e portanto o valor de lin, col pode ser
        negativo ou maior que len(turtledorm)
        """
        lin, col = self.n + 1 - int(y/TAM) - 1, int(x/TAM) - 1
        return (lin, col)

# ============================================================

    def repinte_vizinhos(self, lin, col):
        """ (int, int) -> novo estado
        depois de um clique em lin, col, faz a tartarua
        repintar os vizinhos.
        """
        self.desenhe_casa(lin, col)

        if lin+1 < self.n:
            self.desenhe_casa(lin+1,col)
        if col+1 < self.n:
            self.desenhe_casa(lin,col+1)
        if lin-1 >= 0:
            self.desenhe_casa(lin-1,col)
        if col-1 >= 0:
            self.desenhe_casa(lin,col-1)

# ============================================================

    def desenhe_casa(self, lin, col):
        """ Faça a tartaruga desenhar uma
        casinha de tamanho TAM x TAM. """

        self.va_para(lin, col)
        self.t.pendown()
        if self.turtledorm[lin][col] == 1:
            cor = "yellow"
        else:
            cor = "black"
        self.t.fillcolor(cor)
        self.t.pencolor("white")
        self.t.setheading(90)

        self.t.begin_fill()
        for i in range(4):
            self.t.forward(TAM)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()
        self.t.hideturtle()
        
# ============================================================

    def va_para(self, lin, col):
        """ lin, col -> col, n-lin-1
            movimenta a tartaruga
        """
        self.t.goto(TAM+TAM*col, TAM+TAM*(self.n-lin-1))

# ============================================================
  
    def desenhe_turtledorm(self):
        """ Faça a tartaruga desenhar o turtledorm
        """    
        self.t.pencolor("black")
        for j in range(self.n):
            self.va_para(-1.4, j+0.5)
            self.t.write("%d"%(j+1), False, "center", ("Arial", 2*TAM//self.n, "normal"))

        for i in range(self.n):
            self.va_para(i-0.4, -0.5)
            self.t.pencolor("black")
            self.t.write("%d"%(i+1), False, "center", ("Arial", 2*TAM//self.n, "normal"))
            for j in range(self.n):
                self.desenhe_casa(i,j)

# ============================================================

    def mostre_solucao(self,solucao):
        """ (solucao) -> Faça a tartaruga desenhar a solução usando bolinhas
        """
        self.t.shape("circle")
        self.t.color("white")
        for i in range(self.n):
            for j in range(self.n):
                self.va_para(i-0.5,j+0.5)
                if solucao[i][j] == 1:
                    self.t.pendown()
                    self.t.stamp()
                    self.t.penup()
        self.t.hideturtle()
   
