#Davidson Lisboa Della Piazza, 169786
#CodeForces 99A	Help Far Away Kingdom

import math

x = input()
x = list(x)
flag = 0
decdigs = []
intdigs = []
for i in range(len(x)):
    if(x[i]=='.'):
        flag = 1
    if(flag==0):
        intdigs.append(x[i])
    elif(x[i]!='.'):
        decdigs.append(x[i])

five = '5'
dec = ''
for i in decdigs:
    dec= dec+i
    five = five+'0'
dec = int(dec)
five = int(five[:-1])

inte = ''
for i in intdigs:
    inte = inte+i
inte = int(inte)

if(intdigs[-1]!='9'):
    if(dec<five):
        print(inte)
    else:
        print(inte+1)
else:
    print("GOTO Vasilisa.")
