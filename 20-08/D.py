#Davidson Lisboa Della Piazza, 169786
#CodeForces 560A	Currency System in Geraldion

n = int(input())
x = 1
z = input()
lst = z.split()

for i in range(n):
    if(lst[i]=="1"):
        x = -1

print(x)