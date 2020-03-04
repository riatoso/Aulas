from random import randint
import time
# CRIA ARQUIVO DE LOTERIA
def cria_txt():
    sorteado = []
    vcria = input("Digite o local e nome do arquivo. EX: C:/PYTHON/loteria.txt : ")
    cria = open(vcria,"w")
    while len(sorteado) < 6:
        jogo = randint(1,60)
        if jogo not in sorteado:
            sorteado.append(jogo)
        else:
            continue
    for x in sorteado:
        cria.write("%s"%x+"\n")
    cria.close()
cria_txt()
### LEITURA DO ARQUIVO DE LOTERIA
def ler_loteria():
    arquivo_ler = input("Digite o arquivo para leitura: ")
    ler = open(arquivo_ler,"r")
    leitura = ler.readlines()
    print("Os numeros sorteados são:")
    time.sleep(4)
    for i in leitura:
        print("Numero: %s"%i)
    ler.close()
ler_loteria()
