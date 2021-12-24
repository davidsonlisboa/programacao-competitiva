#Davidson Lisboa Della Piazza, 169786
#CodeForces 122B	Lucky Substring

def isLucky(n):
    for x in n:
        if(x!=4 and x!=7):
            return False
    return True

def luckySub(n):
    n4 = 0
    n7 = 0
    if(isLucky(n)):
        


sub = int(input())
sub = list(map(int, str(sub)))
print(luckySub(sub))