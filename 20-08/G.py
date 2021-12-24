#Davidson Lisboa Della Piazza, 169786
#CodeForces 913A	Modular Exponentiation

def exp(potencia,n,m):
    for i in range(0,n):
            potencia = potencia*2
            if(potencia > m):
                print(m)
                return 
    print(m%potencia)
    return

n = int(input())
m = int(input())
potencia = 1
exp(potencia,n,m)