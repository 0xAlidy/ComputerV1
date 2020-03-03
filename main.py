#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
# -*-coding:Latin-1 -*
from parsing import *
from operator import *
from reduction import *
from solve import *

def program():
    if run() == 0:
        return 0
    res = reduce_equation()
    poly = res[1]
    res = res[0]
    if res > 2:
        print ("Impossible de resoudre un polynome de degre superieur a 2.")
    poly = sorted(poly, key=itemgetter(1)) # tri le tableau en fonction du degre
    if res == 1:
        solve_first_degre(poly)
    elif res == 2:
        solve_second_degre(poly)
    return 1

program()