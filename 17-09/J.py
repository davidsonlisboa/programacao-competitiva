#Davidson Lisboa Della Piazza, 169786
#CodeForces 267A	Subtractions

n = int(input())

for i in range(n):
    li = input()
    li = li.split()
    a = int(li[0])
    b = int(li[1])
    x = 0
    aux = 1
    while(a>0 and b>0):
        if(a>b):
            aux = a//b 
            a = a%b
            x = x+aux
        else:
            aux = b//a
            b = b%a
            x = x+aux 

    print(x)