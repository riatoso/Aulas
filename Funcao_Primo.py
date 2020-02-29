### FUNÇÃO PRIMOS ###
def primo():
    while True:
        numero = input("Digite o numero a partir de 0 para calcular os primos: ")
        primos = []
        lista = []
        try:
            numero = int(numero)
            break
        except:
            print("Digite um numero inteiro!")
    for i in range(0,numero):
        if i == 1 or i == 2 or i == 3 or i == 5 or i == 7:
            primos.append(i)
        elif (i%2 == 0) or (i%3 == 0) or (i%5 == 0) or (i%7 == 0):
            lista.append(i)
        else:
            primos.append(i)
    return primos
print(primo())