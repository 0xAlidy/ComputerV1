import libmath

def solve_first_degre(poly):
    if poly[0][1] == 0 and poly[0][0] != 0: #ax + b
        a = poly[1][0]
        b = poly[0][0]
    else:
       print("L'unique solution est :\n0")
       return
    x = - b / a
    print("L'unique solution est :\n",x)

def solve_second_degre(poly): # ax^2 + bx + c
    a,b,c = 0, 0, 0
    for i in poly:
        if i[1] == 0:
            c = i[0]
        elif i[1] == 1:
            b = i[0]
        elif i[1] == 2:
            a = i[0]
    delta = libmath.ft_pui(b, 2) - 4 * a * c
    if delta > 0:
        print("Le discriminant est positif, les deux solutions reels sont :")
        print((- b + libmath.ft_sqrt(delta)) / (2 * a))
        print((- b - libmath.ft_sqrt(delta)) / (2 * a))
    elif delta == 0:
        print("Le discriminant est nul, l'unique solution reel est :")
        print(- b / (2 * a))
    else:
        print("Le discriminant est negatif, les deux solutions complexes sont :")
        print(- b , "+i *", libmath.ft_sqrt(libmath.ft_abs(delta)), "/", (2 * a))
        print(- b , "-i *", libmath.ft_sqrt(libmath.ft_abs(delta)), "/", (2 * a))