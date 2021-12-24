#Davidson Lisboa Della Piazza, 169786
#Maratona de programacao do IC 2021

n = int(input())

Lset = 0
Kset = 0
Lp = 0
Kp = 0
flag33 = 0
for i in range(n):
    if((Lset==2 and Kset==0) or (Kset==2 and Lset==0)):
        break
    if(Lset==3 or Kset==3):
        break

    x = input()
    if(x=="Kira"):
        Kp+=1
    elif(x=="L"):
        Lp+=1
    if(Kp==3 and Lp==3):
        flag33 = 1
    if((Kp==4 or Lp==4) and flag33==0):
        if(Kp>Lp):
            Kset+=1
        else:
            Lset+=1
        Kp=0
        Lp=0
    elif(flag33==1 and ((Kp-Lp==2)or(Lp-Kp==2))):
        if(Kp>Lp):
            Kset+=1
            Kp=0
            Lp=0
            flag33=0
        elif(Lp>Kp):
            Lset+=1
            Kp=0
            Lp=0
            flag33=0           
    
if(Kset>Lset):
    print("Kira eh melhor que L!!!")
else:
    print("L eh melhor que Kira!!!")

