import random

def tamanho():
    s1 = input("Digite uma frase!: ").lower().strip()
    s2 = input("Digite outra frase!: ").lower().strip()
    t1 = len(s1)
    t2 = len(s2)
    igual = []
    diferente = []
    if t1 == t2:
        print("As frases são do mesmo tamanho.")
        for i in range(0, len(s1)):
            letra = s1[i]
            if letra == s2[i]:
                igual.insert(i, letra)
            else:
                diferente.append(letra)
    else:
        print("Frases com tamanhos diferentes não posso prosseguir!")
    return igual,diferente

print(tamanho())            
            