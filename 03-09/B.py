#Davidson Lisboa Della Piazza, 169786
#CodeForces 1293B	JOE is on TV!

n = float(input())
x = float(0)

for i in range(int(n)):
    x = (x) + (1/(n-i))

print(x)

