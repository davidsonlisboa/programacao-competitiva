#Davidson Lisboa Della Piazza, 169786
#CodeForces 722B	Verse Pattern

n = int(input())
sylls = list(map(int, input().strip().split(' ')))
strs = []
for i in range(n):
    aux = input()
    strs.append(aux)

aux = []
for i in range(len(strs)):
    aux.append(list(strs[i]))


flag = 0
x = 0
for i in range(n):
    for j in range(len(strs[i])):
        if(aux[i][j]=='a' or aux[i][j]=='e' or aux[i][j]=='i' or aux[i][j]=='o' or aux[i][j]=='u' or aux[i][j]=='y'):
            x +=1
    if(x!=sylls[i]):
        print("NO")
        flag = 1
        break
    x=0

if (flag==0):
    print("YES")