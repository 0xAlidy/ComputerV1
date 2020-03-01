#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
# -*-coding:Latin-1 -*
#import parsing
import sys

# parsing.start() Pas de parsing d'apres le sujet

            

def print_params():
    print("\narguments : ", end = "")
    for i in sys.argv:
        print(i, end = " , ")
    print("\n\n", end = "")

def remove_all(liste, item):
    while (liste.count(item)):
        liste.remove(item)

def fill_poly(poly, liste, inv):
    nb = 1 if inv == 0 else -1
    res, check, cpt = 0, 0, 0
    for i in liste:
        if i[0] == 'X' or check:
            pui = int(i[2])
            for k in poly:
                if k[1] == pui:
                    check = -1
                if check != -1:
                    cpt += 1
            if check != -1:
                poly.append([0, pui])
            poly[cpt][0] += nb
            res = pui if pui > res and nb != 0 else res
            check = 0
            cpt = 0
        elif i == '-':
            nb = -1 if inv == 0 else 1
        elif i == '+':
            nb = 1 if inv == 0 else -1
        else:
            nb *= int(i) if i.find('.') == -1 else float(i)
            check = 1
    return res

def print_reduced_form(poly):  # i de la forme (index, [nb, pui])
    print("Forme reduite    : ", end = "")
    for i in enumerate(poly):
        if i[1][0]:
            if (i[1][0] < 0):
                print(" - ", end = "")
                i[1][0] *= -1
            elif (i[0] != 0):
                print (" + ", end = "")
            print(i[1][0], end = "")
            if (i[1][1]):
                print(" *" , end = "")
            if i[1][1]:
                print(" X^", i[1][1], end = "", sep = "")
    print(" = 0")
            

def reduce_equation():
    poly = []
    temp = sys.argv[1].split('=')   
    left_equ = list(filter(None, temp[0].split(" ")))
    remove_all(left_equ, "*")
    right_equ = list(filter(None, temp[1].split(" ")))
    remove_all(right_equ, "*")
    print("gauche : ",left_equ,"\n\ndroite : ", right_equ, "\n")
    res = fill_poly(poly, left_equ, 0)
    res2 = fill_poly(poly, right_equ, 1) 
    res = res2 if res2 > res else res
    print_reduced_form(poly)
    print ("Polynome de degre:", res)
    return res
        

print_params()
res = reduce_equation()
if res > 2:
    print ("Je ne peux pas resoudre un polynome de degre superieur a 2.")
