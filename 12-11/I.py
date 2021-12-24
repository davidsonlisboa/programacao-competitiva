#Davidson Lisboa Della Piazza, 169786
#CodeForces 270A	Fancy Fence

n = int(input())

for i in range(n):
    x = int(input())
    if(360%(180-x)==0):
        print('YES')
    else:
        print('NO')
