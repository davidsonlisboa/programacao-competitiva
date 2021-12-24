#Davidson Lisboa Della Piazza, 169786
#CodeForces 1475A	Odd Divisor

n = int(input())

for i in range(n): 
    x = int(input())
    flag = 0
    if(x%2 != 0):
        print("YES")
    else:
        while(x>2):
            x=x/2
            if(x%2 != 0):
                print("YES")
                flag = 1
                break
        if(flag == 0):
            print("NO")
