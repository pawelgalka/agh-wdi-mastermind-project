import random

def min(a,b):
    if a<=b:
        return a
    else:
        return b

def podaj_kod():
    kod=(input())
    while len(kod)!=4:
        print("Podaj czterocyfrowy kod !!!")        
        kod=(input())
    return kod

    
def possibilities():
    tab=[]
    num=[1,2,3,4,5,6,7,8]
    for i in range (0,8):
        for j in range (0,8):
            for k in range (0,8):
                for l in range (0,8):
                    pos=1000*num[i]+100*num[j]+10*num[k]+num[l]
                    tab.append(pos)
    return tab

possib=possibilities()

def hintblack(code,proba):
    black=0
    proba=int_to_list(proba)
    for i in range (0,4):
        if code[i]==str(proba[i]):
            black+=1
    return black
    
def hintwhite(code,proba):
    white=0
    proba=int_to_list(proba)
    """for i in range (0,4):
        for j in range (0,4):
            if code[i]==str(proba[j]):
                white+=1
                break"""
    for i in range (1, 9):
            white += min(code.count(str(i)), proba.count(i))
    return white

    

def first_move():
    return 1122
    
def reduce(possib,code,ruch):
    for i in range (0,len(possib)):
        if possib[i]!=0:
            pos=str(possib[i])
            if hintblack(code,ruch)!=hintblack(pos,ruch) or hintwhite(code,ruch)!=hintwhite(pos,ruch):
                possib[i]=0
    return possib
    
def int_to_list(n):
    l = []
    while n != 0:
        l = [n % 10] + l
        n = n // 10
    return l
    
def move(possib):

    x=0
    for i in range (0,len(possib)):
        if possib[i]==0:
            break
        x+=1
    x=random.randint(0,x-1)
    return possib[x]
    
#code=str(podaj_kod())
code=str(possib[random.randint(0,4095)])

print(code)


attempts=0
while attempts<8:
    if attempts==0:
        ruch=first_move()
        
    else:
        ruch=move(possib)

    attempts+=1

    print(attempts," ruch komputera ",ruch)
    black=hintblack(code,ruch) 
    print("Black: ",black)

    if black==4:
        print("Komputer wygrał ")
        break
    white=hintwhite(code,ruch)-hintblack(code,ruch)
    print("White: ",white)
    possib=reduce(possib,code,ruch)
    possib.sort()
    possib.reverse()
    #print(possib)

else:
    print("Komputer przegrał" )      

