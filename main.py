#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
# -*-coding:Latin-1 -*
import parsing
import operator
import reduction
import solve

def program():
    if parsing.run() == 0:
        return 0
    res = reduction.reduce_equation()
    poly = res[1]
    res = res[0]
    if res > 2:
        print ("Impossible de resoudre un polynome de degre superieur a 2.")
    poly = sorted(poly, key=operator.itemgetter(1)) # tri le tableau en fonction du degre
    print(poly)
    if res == 1:
        solve.solve_first_degre(poly)
    elif res == 2:
        solve.solve_second_degre(poly)
    return 1

program()