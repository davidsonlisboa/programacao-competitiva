#Davidson Lisboa Della Piazza, 169786
#CodeForces 490A	Team Olympiad

n = int(input())

skill = input()
skill = skill.split(" ")
base = ["1", "2", "3"]

um = 0
dois = 0
tres = 0
for i in skill:
    if(i=="1"):
        um+=1
    elif(i=="2"):
        dois+=1
    else:
        tres+=1

if(um<=dois and um<=tres):
    minV = um
elif(dois<=um and dois<=tres):
    minV = dois
elif(tres<=dois and tres<=um):
    minV = tres

print(minV)
um = 0
dois = 0
tres = 0
for i in range(minV):
    for j in base:
            if(j=="1"):
                for k in range(um,len(skill)):
                    if(j==skill[k]):
                        print((k+1),end=" ")
                        skill[k] = 0
                        um = k
                        break                   
            elif(j=="2"):
                for k in range(dois,len(skill)):
                    if(j==skill[k]):
                        print((k+1),end=" ")
                        skill[k] = 0
                        dois = k
                        break  
            else:
                for k in range(tres,len(skill)):
                    if(j==skill[k]):
                        print(k+1)
                        skill[k] = 0
                        tres = k
                        break 