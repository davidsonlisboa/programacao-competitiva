#Davidson Lisboa Della Piazza, 169786

from decimal import *

x = Decimal(input())

inte = x//1
dec = x % 1

intdigs = [int(a) for a in str(inte)]
decdigs = []
for i in str(dec):
    if(i!="."):
        decdigs.append(i) 

print(decdigs)

if(intdigs[-1]!=9):
    if(dec<0.5):
        print(inte)
    else:
        print(inte+1)
else:
    print("GOTO Vasilisa.")