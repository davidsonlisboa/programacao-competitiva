#Davidson Lisboa Della Piazza, 169786
#CodeForces 1461A	String Generation

n = int(input())
a = ['a', 'b', 'c']
for i in range(n):
    pal = []
    inp = list(map(int, input().strip().split(' ')))
    x = int(inp[0])
    y = int(inp[1])
    count = 0
    pos = 0
    for i in range(x):
        pal.append(a[pos])
        count+=1
        if(count==y):
            if(pos==2):
                pos=0
            else:
                pos+=1
            count=0

    pal = ''.join(pal)
    print(pal)

