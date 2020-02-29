### VERIFICA QUANTOS ITENS REPETIDOS EXISTEM NA LISTA ###
from random import randint as gera
def conta():
    x = 0
    lista = []
    lista2 = []
    while x < 8:
        numero = gera(0 , 15)
        lista.append(numero)
        x += 1
    for i in range(0 ,len(lista)):
        for y in lista:
            if y == lista[i]:
                lista2.append(" Existe(m) %i "%lista.count(y)+"numero %i na lista"%y)
    lista3 = list(set(lista2))
    return lista, lista3
#print(conta())

#Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve a tabuada de 1 até N. Mostre a tabuada na forma: 
#1 x N = N
#2 x N = 2N
#...
#N x N = N2
def tabuada():
    lista = []
    while True:
        numero = input("Digite o numero para ver a tabuada: ")
        try:
            numero = int(numero)
            break
        except:
            print("Digite um numero inteiro!")

    for i in range(0,10):
        #print(i)
        solucao = (numero * i)
        print("%i x "%i+" %i "%numero+" = %i"%solucao)
tabuada()