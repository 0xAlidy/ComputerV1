import sys
import parsing
import libmath

def f_poly(poly, i, nb):
    cpt = 0
    check = 0
    if parsing.check_unknow(i) == 1: # X
        pui = 1
    elif parsing.check_unknow(i) == 2: # X^x
        pui = int(i[2])
    else:
        pui = 0
    for k in poly:
        if k[1] == pui:
            check = -1
        if check != -1:
            cpt += 1
    if check != -1:
        poly.append([0, pui])
    poly[cpt][0] += nb

def fill_poly(poly, liste, inv):
    nb = 1 if inv == 0 else -1
    check = 0
    for i in liste:
        if (i[0] == 'X' or check) and i != '*':
           f_poly(poly, i, nb)
           check = 0
        elif i == '*' or i == '-' or i == '+':
            pass
        else:
            nb *= int(i) if i.find('.') == -1 else float(i)
            check = 1
        if i == '-':
            nb = -1 if inv == 0 else 1
        elif i == '+':
            nb = 1 if inv == 0 else -1
    if check == 1:
        f_poly(poly, i, nb)

def print_reduced_form(poly):  # i de la forme (index, [nb, pui])
    print("Forme reduite    : ", end = "")
    before = 0
    degre = 0
    for i in enumerate(poly):
        if i[1][0]:
            if (i[1][0] < 0):
                print(" - ", end = "")
            elif (before == 1):
                print (" + ", end = "")
            if (i[1][0] != 1):
                print(libmath.ft_abs(i[1][0]), end = "")
            if (i[1][1]):
                if (i[1][0] != 1):
                    print(" *" , end = "")
            if i[1][1] == 1:
                print(" X", end = "")
                degre = 1 if degre == 0 else degre
            elif i[1][1] > 1:
                print(" X^", i[1][1], end = "", sep = "")
                degre = i[1][1] if degre < i[1][1] else degre
            before = 1
    if before == 0:
        pass
    else:
        print(" = 0")
    return degre

def get_degre(poly):
    degre = 0
    for i in poly:
        degre = i[1] if i[1] > degre and i[0] != 0 else degre
    return degre

def reduce_equation():
    poly = []
    temp = sys.argv[1].split('=')   
    left_equ = list(filter(None, temp[0].split(" ")))
    right_equ = list(filter(None, temp[1].split(" ")))
    fill_poly(poly, left_equ, 0)
    degre = get_degre(poly)
    fill_poly(poly, right_equ, 1)
    degre2 = get_degre(poly)
    if (degre == 0 and degre2 == 0):
        print("ERREUR: Il n'y a aucuns monomes")
        return 0
    res = print_reduced_form(poly)
    if ((degre > 0 or degre2 > 0) and res == 0):
        print ("0 (Le cote gauche est equivalent au cote droit)\nPolynome de degre: 0\nLa solution est:\nUne infinite")
    else:
        print ("Polynome de degre:", res)
    return [res, poly]
