#Davidson Lisboa Della Piazza, 169786
#CodeForces 26A	Almost Prime

def crivo(n, bits):
    n+=1
    primos = []
    for i in range(2,n):
        if(bits[i]):
            for j in range(i*i, n, i):
                bits[j] = 0
            primos.append(int(i))
    return primos


def quasePrimo(primos, bits):
    almostPrime = 0
    for i in range(len(bits)):
        count = 0
        if(not bits[i]):
            for j in primos:
                if(i%j==0):
                    count+=1
            if(count==2):
                almostPrime+=1

    print(almostPrime)

n = int(input())
bits = []
for i in range(n+1):
    bits.append(int(1))
primos = crivo(n, bits)
quasePrimo(primos, bits)
