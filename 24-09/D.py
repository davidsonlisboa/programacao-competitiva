#Davidson Lisboa Della Piazza, 169786
#CodeForces 755A	PolandBall and Hypothesis

def ehPrimo(el): 
    for i in range(2,(el//2)+1,1):
        if(el%i==0):
            return False
    return True


n = int(input())

j=1
while(True):
    x = n*j+1
    if(not(ehPrimo(x))):
        print(j)
        break
    j+=1