### VARIACAO DE TEMPERATURA + OU - 10 GRAUS
def temperatura():
    lista = []
    while len(lista) < 7:
        temp = input("Digite a temperatura: ")
        try:
            temp = float(temp)
            if lista == []:
                lista.append(temp)
            elif temp - min(lista) >= 10 or temp - min(lista) <= -10:
                print("A temperatura esta variando em 10 graus: Adciona (S/N)")
                confimar = input("(S/N): ").lower()
                if confimar == "s":
                    lista.append(temp)
                else:
                    continue
            else:
                lista.append(temp)
        except:
            print("Tem que digitar numeros!")
    return lista
print(temperatura()) 