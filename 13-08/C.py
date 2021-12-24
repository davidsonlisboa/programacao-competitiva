#Davidson Lisboa Della Piazza, 169786
#CodeForces 96B	Lucky Numbers (easy)

def isLucky(n):
    t = str(n)
    for x in t:
        if(x!=4 and x!=7):
            return False
    return True

def superLucky(n):
    while True:
        ns7 = 0
        ns4 = 0
        if(isLucky(n)):
            string = str(n)
            for x in string:
                if(x=="4"):
                    ns4+=1
                if(x=="7"):
                    ns7+=1
            if(ns7==ns4):
                return n
        n+=1

n = int(input())
print(superLucky(n))