from operator import itemgetter
def media_aluno():
    lista = []
    dic = {}
    while (len(lista)) < 3:
        aluno = input("%i - "%(len(lista) + 1)+"Digite o nome do aluno: ").lower().title()
        while True:
            notau = input("Digite a nota 1 do aluno %s :"%aluno)
            try:
                notau = float(notau)
                break
            except:
                print("Digite apenas numeros!")
        while True:
            notad = input("Digite a nota 2 do aluno %s :"%aluno)
            try:
                notad = float(notad)
                break
            except:
                print("Digite apenas numeros!")
        media = ((notau+notad)/2)
        lista.append([aluno , media])
    for i in lista:
        dic.update({i[0]:i[1]})
    top_alunos = sorted(dic.items(), key=itemgetter(1), reverse=True)
    #top = sorted(dic.values(), key=float, reverse=True)
    #for x,y in zip(top, range(0, len(lista))):
    #for x,y in zip(dic.keys(),(sorted(dic.values(), key=float, reverse=True))):
    #    print(y,x) 
    return top_alunos
print(media_aluno())