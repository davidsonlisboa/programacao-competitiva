#Davidson Lisboa Della Piazza, 169786
#CodeForces 452A	Eevee

x = int(input())
n = input()
n = list(n)
pok = ['vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']

aux = []
for i in range(len(pok)):
    aux.append(list(pok[i]))

flag = 0
for i in range(len(pok)):
    for j in range(len(n)):
        if(len(n)!=len(pok[i])):
            break
        if(n[j]!='.' and n[j]!=aux[i][j]):
            break
        if(j==len(n)-1):
            print(pok[i])
            flag=1
            
    if(flag==1):
        break
