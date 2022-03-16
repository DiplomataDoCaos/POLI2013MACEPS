print (1/3)
a=1/3
print ("teste",'%.2f' % a)
lista=[]
lista.append(3)
print (lista)
z=3
print (z)
for z in range (10):
    print(z)
print(z)

import math

def distância(ponto_1, ponto_2, teste = False):
    a = ponto_1[0] - ponto_2[0]
    b = ponto_1[1] - ponto_2[1]
    c = math.sqrt(a*a + b*b)
    if teste==True:
        print("Coordenadas de ponto_1:", "%.2f" %ponto_1[0],"%.2f"%ponto_1[1])
        print("Coordenadas de ponto_2:", "%.2f" %ponto_2[0],"%.2f"%ponto_2[1])
        print("Distância:","%.2f"%c)
    return (c)

def aceleração_gravitacional(astro, ponto, teste = False):
    d = distância(astro[0],ponto)
    print(d)
    print(astro)
    a= astro[1]*8.65*(10**-13)/(d*d)
    print(a)
    print (ponto[0])
    print (astro[0][0])
    print (ponto[0])
    d=astro[0][0]-ponto[0]
    print(d)
    b=a*(astro[0][0]-ponto[0])/d #a subtração dá defeito
    c=a*(astro[0][1]-ponto[1])/d #preciso achar uma maneria de determinar o seno e cosseno
    if teste==True:
        print("posição do astro:","%.2f" %astro[1])
        print("massa do astro:", "%.2e" %astro[2])
        print("posição do ponto:","%.2f" %ponto[0],"%.2f" %ponto[1])
        print("aceleração resultante:","%.2f" %b,"%.2f" %c)
    return [b,c]

#aceleração_gravitacional([10,10,10],[15,15],True)
def aceleração_resultante(lista_astros, ponto, teste = False):
    total_h=total_v=0
    for i in range(0,len(lista_astros),1):
        d=aceleração_gravitacional (lista_astros(i),ponto)
        total_h= total_h +d[0]
        total_v= total_v +d[1]
    if teste==True:
        for i in range(0,len(lista_astros),1): #checar se i reseta
            print("posição do astro",i,":","%.2f" % lista_astros[i[0]],"%.2f" % lista-astros[i[1]])
            print("massa do astro",i,":","%.2f"% lista_astros[i[2]])
        print("posição do ponto:", ponto)
        print("aceleração resultante","%.2f" %total_h, "%.2f" %total_v)
    return[total_h,total_v]
