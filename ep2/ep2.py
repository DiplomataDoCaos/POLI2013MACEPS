#***************************************************************#
#**                                                           **#
#**   Fernando Talietta          Número USP: 8582828          **#
#**   Exercício-Programa 2                                    **#
#**   Professor: José Augusto                                 **#
#**   Turma: 1                                                **#
#**                                                           **#
#***************************************************************#
x=10
Trocou = GTrocou = GNTrocou = NTrocou = 0
Reptori=Rept= int(input("Quantas simulações vc quer?:"))
while Rept > 0:
  x = (22695477*x+1)%(2**32)
  if x/(2**32)<=1/3:
    carro=1
  elif x/(2**32) <= 2/3:
    carro=2
  else:
    carro=3
  x = (22695477*x+1)%(2**32)
  if x/(2**32)<=1/3:
    porta_escolhida = 1
  elif x/(2**32)<=2/3:
    porta_escolhida = 2
  else:
    porta_escolhida = 3
  if porta_escolhida == 1:
    if carro==1:
      x = (22695477*x+1)%(2**32)
      if x/(2**32)<=1/2:
         Aberta =3
      else:
         Aberta =2
    if carro==2:
      Aberta=3
    if carro==3:
      Aberta=2
  if porta_escolhida == 2:
    if carro==2:
      x = (22695477*x+1)%(2**32)
      if x/(2**32)<=1/2:
         Aberta =1
      else:
         Aberta =3
    if carro==1:
      Aberta=3
    if carro==3:
      Aberta=1
  if porta_escolhida == 3:
    if carro==3:
      x = (22695477*x+1)%(2**32)
      if x/(2**32)<=1/2:
         Aberta =1
      else:
         Aberta =2
    if carro==2:
      Aberta=1
    if carro==1:
      Aberta=2
  x = (22695477*x+1)%(2**32)
  if x/(2**32)<=1/2:
    Trocou= Trocou + 1
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
    if porta_escolhida == carro:
      GTrocou= GTrocou +1
  else:
    NTrocou = NTrocou +1
    if porta_escolhida == carro:
      GNTrocou= GNTrocou +1
  Rept = Rept - 1
if Trocou ==0:
  print("Não houve troca de porta")
else:
  print("Frenquência de ganho de carro trocando a porta:",GTrocou/Trocou)
if NTrocou ==0:
  print("A porta foi trocada toda vez")
else:
  print("Frequência de ganho de carro não trocando a porta:",GNTrocou/NTrocou)
  print("Frequenica de vezes que se trocou a porta:",Trocou/Reptori)
