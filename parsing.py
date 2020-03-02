import sys


#* Normal                            "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
#* naturel (sans X^0 et X^1 => X)    "5 + 4 * X - 9.3 * X^2 = nb X"

'''
PARSING :

1) 1 seul = 
2) seulement = + - * nb X(^x)    
3) + - >>> avant : X , nb , =  apres : nb , X
   =   >>> avant : X , nb      apres : X , nb , + , -
   *   >>> avant : nb          apres : X   
   X   >>> avant : *,+,-, =    apres : +,-,=,
   nb  >>> avant : +, -, =     apres : X, =, *,+,-

4) equivalent = equivalent ===> infinite de solutions
   sans monome = sans monome  ===> erreur
'''
def parsing_arguments():
    if (len(sys.argv) != 2):
        return 0
    return 1

def check_unknow(s): # 0 => erreur 1 => X 2=> X^x
    if s == 'X':
        return 1
    if len(s) < 3:
        return 0
    if s[0] == 'X' and s[1] == '^' and s[2:].isdigit() != 0:
        return 2
    return 0

def check_item(s):
    if s == '+' or s == '-':
        return 1
    if s == '=':
        return 2
    if s == '*':
        return 3
    if check_unknow(s) != 0:
        return 4
    if s.replace(".", "", 1).isdigit() != 0: # test pour les float
        return 5
    return 0
    
def check_before(s, item):
    if (item == 1 and (check_item(s) == 3 or check_item(s) == 1)):  # + - >>> avant : X , nb , =
        return 0
    if (item == 2 and (check_item(s) != 4 and check_item(s) != 5)): # =   >>> avant : X , nb 
        return 0
    if (item == 3 and check_item(s) != 5):   # *   >>> avant : nb
        return 0
    if (item == 4 and check_item(s) == 5): # X   >>> avant : *,+,-, =
        return 0
    if (item == 5 and (check_item(s) == 4 or check_item(s) == 5)): # nb  >>> avant : +, -, =
        return 0
    return 1

def check_after(s, item):
    if (item == 1 and (check_item(s) != 4 and check_item(s) != 5)):  # + - >>> apres : nb , X
        return 0
    if (item == 2 and (check_item(s) == 2 or check_item(s) == 3)): # =  >>> apres : X , nb , + , -
        return 0
    if (item == 3 and check_item(s) != 4):   # *   >>> apres : X
        return 0
    if (item == 4 and (check_item(s) == 4 or check_item(s) == 5)): # X  >>> apres : +,-,=,
        return 0
    if (item == 5 and check_item(s) == 5): # nb >>> apres : X, =, *, +, -
        return 0
    return 1

def parsing_equation():
    equ = sys.argv[1]
    lst = list(filter(None, equ.split(" ")))
    if lst.count("=") != 1:
        return 0
    for enum in enumerate(lst):
        i = enum[0]
        s = enum[1]
        res = check_item(s)
        if res > 0:  # 1 => - / + 2 => = 3 => *
            if ((res == 2 or res == 3) and (i == 0 or i == len(lst) - 1)) or (res == 1 and i == len(lst) - 1):
                return 0
            if i > 0:
                if check_before(lst[i - 1], res) == 0:
                    return 0
            if i < len(lst) - 1:
                if check_after(lst[i + 1], res) == 0:
                    return 0
        else:           # erreur si res == 0
            return 0
    return 1

def run():
    if (parsing_arguments() == 0):
        print("ERREUR : Nombre d'arguments invalide \nExemple : python3.7 ./main.py \"equation\"")
        return 0
    if (parsing_equation() == 0):
        print("ERREUR : le format de l'equation est invalide")
        return 0
    return 1
