#Davidson Lisboa Della Piazza, 169786
#CodeForces 146A	Lucky Ticket

def isLucky(n):
    for x in n:
        if(x!=4 and x!=7):
            return False
    return True

def luckyTicket(n):
    z = 0
    y = 0
    if(isLucky(n)):
        fhalf = int(len(n)/2)
        shalf = int(len(n))
        for i in range(0, fhalf):
            z = z+int(n[i])
        for i in range(fhalf, shalf):
            y = y+int(n[i])
        if(z==y):
            print("YES")
            return
    print("NO")


n = int(input())
ticket = input()
ticket = list(map(int, str(ticket)))
luckyTicket(ticket)