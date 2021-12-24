#Davidson Lisboa Della Piazza, 169786
#CodeForces 802G	Fake News (easy)

n = input()
heidi = ['h','e','i','d','i']
flag = 0
for i in n:
    if(i == heidi[0]):
        del heidi[0]
    if not heidi:
        flag = 1
        break

if(flag==1):
    print("YES")
else:
    print("NO")