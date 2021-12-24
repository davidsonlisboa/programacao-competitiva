#Davidson Lisboa Della Piazza, 169786
#CodeForces 981A	Antipalindrome

def isPalindrome(string):
    for i in range(len(string)):
        if(string[i] != string[len(string)-i-1]):
            return False
    return True


x = input()
x = list(x)
flag = 0 
for i in range(len(x)):
    if(not isPalindrome(x)):
        print(len(x))
        flag = 1
        break
    else:
        del x[0]

if(flag==0):
    print(0)