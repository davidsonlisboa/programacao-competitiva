#Davidson Lisboa Della Piazza, 169786
#CodeForces 233A	Perfect Permutation

def perm(n):
    if(n%2==1):
        print("-1")
        return

    base = []
    for i in range(1,n+1):
        base.append(i)
    i=0

    while True:
        aux = base[i]
        base[i] = base[i+1]
        base[i+1] = aux
        if((i+2)==n):
            break
        i+=2

    for i in range(n):
        if(i==n):
            print(base[i])
            return
        else:
            print(base[i], end = " ")

n = int(input())
perm(n)