#Davidson Lisboa Della Piazza, 169786
#CodeForces 71A	Way Too Long Words

n = int(input())

for i in range(n):
    words = input()
    x = list(words)
    aux = 0
    if(len(x)<=10):
        print(words)
    else:
        for i in range(1,len(x)-1):
            aux+=1
        print(x[0]+str(aux)+x[-1])