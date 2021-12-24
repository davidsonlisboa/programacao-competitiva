#Davidson Lisboa Della Piazza, 169786
#CodeForces 610A	Pasha and Stick

def rect(n,x):
    if(n%4==0):
        print(int(x-1))
    else:
        print(int(x-0.5))


n = int(input())
x = n/4

if(n!=0 and n%2==0):
    rect(n,x)
else:
    print(0)