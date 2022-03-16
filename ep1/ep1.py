#***************************************************************#
#**                                                           **#
#**   Fernando Talietta          Número USP: 8582828          **#
#**   Exercício-Programa 1                                    **#
#**   Professor: José Augusto                                 **#
#**   Turma: 1                                                **#
#**                                                           **#
#***************************************************************#

import random
random.seed()
carro = random.choice([1, 2, 3])
porta_escolhida = int(input("Qual a porta que voce se arrisca? 1, 2 ou 3:"))
if porta_escolhida == 1:
 if carro==1:
  Aberta=random.choice([2, 3])
 if carro==2:
  Aberta=3
 if carro==3:
  Aberta=2
if porta_escolhida == 2:
 if carro==2:
  Aberta=random.choice([1, 3])
 if carro==1:
  Aberta=3
 if carro==3:
  Aberta=1
if porta_escolhida == 3:
 if carro==3:
  Aberta=random.choice([1, 2])
 if carro==2:
  Aberta=1
 if carro==1:
  Aberta=2
print('e revelado que a porta',Aberta,'possui um bode do mal!')
if input ("Voce quer trocar de porta? s ou n:") == "s":
 if porta_escolhida==1 and Aberta==2:
  porta_escolhida=3
 elif porta_escolhida==3 and Aberta==2:
  porta_escolhida=1
 elif porta_escolhida==3 and Aberta==1:
  porta_escolhida=2
 elif porta_escolhida==2 and Aberta==1:
  porta_escolhida=3
 elif porta_escolhida==2 and Aberta==3:
  porta_escolhida=1
 elif porta_escolhida==1 and Aberta==3:
  porta_escolhida=2
 print ("sua nova porta e:",porta_escolhida)
if carro==porta_escolhida:
 print ("Aeee manolo ganhou um Camaro Amarelo")
else:
 print ("Aeee ganhou um evil bodao das trevas!")
