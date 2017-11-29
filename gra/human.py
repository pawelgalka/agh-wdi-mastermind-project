import random
random.seed()


def losuj_kod():
    code=[]
    for i in range (0,4):
        code.append(random.randint(49,56))
    return code
    
    
def podaj_kod():
    kod=(input())
    while len(kod)!=4:
        print("Podaj czterocyfrowy kod !!!")        
        kod=(input())
    return kod

def hintblack(code,proba):
    black=0
    for i in range (0,4):
        if code[i]==ord(proba[i]):
            black+=1
    return black
    
def hintwhite(code,proba):
    white=0
    for i in range (0,4):
        for j in range (0,4):
            if code[i]==ord(proba[j]):
                white+=1
                break
    return white

    
def czy_wygrana(code,proba):
    for i in range (0,4):
        if code[i]!=ord(proba[i]):
            return 0
    return 1

code=losuj_kod()
"""for i in range (0,4):
    print(chr(code[i]),end="")"""
print()
attempts=0
while attempts<8 : 
    print("Podaj kod")
    proba=podaj_kod()        
    attempts+=1
    print ("B:",hintblack(code,proba))
    print ("W:",hintwhite(code,proba)-hintblack(code,proba))
    if czy_wygrana(code,proba):
        print("wygrałeś w ",attempts," rundzie!")
        break
else:
    print("Przegrałeś")


