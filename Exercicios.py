# O Primeiríssimo exercício diz assim: 
# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
def nota_010():
    while True:
        n1 = input("Digite uma nota de 0 a 10: ")
        try:
            n1 = float(n1)
            if n1 < 0:
                print("Sua nota não pode ser menor que 0!")
            elif n1 > 10:
                print("Sua nota não pode ser maior que 10!")
            else:
                break
        except:
            False
    return n1

#print("Sua nota é %.2f"%nota_010())

# Hoje vamos fazer um peça três idades dos aluno de, e em seguida calcule a media de idade dos alunos, 
# e classifique a sala como jovem criança, etc
def idade():
    while True:
        idade1 = input("Digite sua idade / Pessoa 1: ")
        try:
            idade1 = float(idade1)
            if idade1 < 0:
                print("Sua idade não pode ser menor que 0!")
            elif idade1 > 120:
                print("Voce é Matuzalem? , sua idade não pode ser maior que 120!")
            else:
                break
        except:
            False
    while True:
        idade2 = input("Digite sua idade / Pessoa 2: ")
        try:
            idade2 = float(idade2)
            if idade2 < 0:
                print("Sua idade não pode ser menor que 0!")
            elif idade2 > 120:
                print("Voce é Matuzalem? , sua idade não pode ser maior que 120!")
            else:
                break
        except:
            False
    while True:
        idade3 = input("Digite sua idade / Pessoa 3: ")
        try:
            idade3 = float(idade3)
            if idade3 < 0:
                print("Sua idade não pode ser menor que 0!")
            elif idade3 > 120:
                print("Voce é Matuzalem? , sua idade não pode ser maior que 120!")
            else:
                break
        except:
            False
    media = (idade1+idade2+idade3)/3
    if media >= 30 and media < 40:
        print("Classe adulta!")
    elif media < 30:
        print("Classe Jovem!")
    else:
        print("Classe de Velhos!")
    
    return ("%.2f")%media
#print(idade())

# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do “e”, da vírgula entre outros.Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidadesTestar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 
import math
def inteiro():
    while True:
        numero = input("Digite um numero interiro entre 900 e 1000: ")
        try:
            numero = float(numero)
            if numero < 900:
                print("Numero precisa ser maior ou igual a 900!")
            elif numero > 1000:
                print("Numero não pode ser maior que 1000!")
            else:
                break
        except:
            False
    centenas = math.floor(numero/100)
    dezenas = math.floor(numero/10)
    unidades = numero%100
    return dezenas, centenas, unidades
print(inteiro())