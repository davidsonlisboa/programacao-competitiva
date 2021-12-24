#Davidson Lisboa Della Piazza, 169786
#CodeForces 411A	Password Check

def checkPWD(senha):
    lenght = len(senha)
    if(lenght<5):
        print("Too weak")
        return
    else:
        lenght = True
    hasUpper = False
    hasLower = False
    hasDig = False
    for i in range(len(senha)):
        if(lenght and hasUpper and hasLower and hasDig):
            print("Correct")
            return
        if(senha[i].isupper()):
            hasUpper = True
        elif(senha[i].islower()):
            hasLower = True
        elif(senha[i]=="0" or senha[i]=="1" or senha[i]=="2" or senha[i]=="3" or senha[i]=="4" or senha[i]=="5" 
        or senha[i]=="6" or senha[i]=="7" or senha[i]=="8" or senha[i]=="9"):
            hasDig = True
    print("Too weak")
    return

string = input()
string = list(string)
checkPWD(string)