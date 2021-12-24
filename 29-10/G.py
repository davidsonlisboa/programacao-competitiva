#Davidson Lisboa Della Piazza, 169786
#CodeForces 231A	Team

n = int(input())

aux = 0
for i in range(n):
    p = input()
    p = list(p)
    x = int(p[0]) + int(p[2]) + int(p[4])
    if(x>=2):
        aux+=1
print(aux)