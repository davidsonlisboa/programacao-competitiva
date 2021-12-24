#Davidson Lisboa Della Piazza, 169786
#CodeForces 122A	Lucky Division

def isLucky(n):
    t = [int(d) for d in str(n)]
    for x in t:
        if(x!=4 and x!=7):
            return False
    return True

def almostLucky(n):
    i = 0
    while i <= n:
        if(isLucky(i)):
            if((n%i)==0):
                print("YES")
                return
        i+=1
    print("NO")
    return

n = int(input())
almostLucky(n)