#Davidson Lisboa Della Piazza, 169786
#CodeForces 978A	Remove Duplicates

n = int(input())
arr = list(map(int, input().strip().split(' ')))
x = []
for i in reversed(arr):
    if(i not in x):
        x.insert(0, i)
    else: 
        arr = list(filter(lambda a: a!=i,arr))

print(len(x))

for i in range(len(x)):
    if(i<len(x)):
        print(x[i], end = ' ')
    else:
        print(x[i])