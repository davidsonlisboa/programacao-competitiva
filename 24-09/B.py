#Davidson Lisboa Della Piazza, 169786
#CodeForces 1328A	Divisibility Problem

n = int(input())

for k in range(n):
    x = input()
    x = x.split()
    a =  int(x[0])
    b = int(x[1])
    
    if(a%b==0):
        print(0)
    else:
        z = a//b
        z = z*b
        z = a-z
        z = b-z
        print(z)

