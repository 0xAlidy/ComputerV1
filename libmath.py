def ft_abs(nb):
    nb = -nb if nb < 0 else nb
    return nb

def ft_pui(nb, pui):
    if (isinstance(pui, int) == 0 or pui < 0):
        print("La puissance doit etre un entier positif")
        return
    res = nb
    for i in range(pui - 1):
        res *= nb
    return res

def ft_sqrt(nb):
    x = 1
    y = 0.5 * (1 + nb)
    while ft_abs(y - x) > 0.0001:
        x = y
        y = 0.5 * (x + nb / x)
    return y

def ft_around(nb, precision):
    number = str(nb)
    index = number.index('.') + 1
    entier = number[:index]
    decimal = number[index:]
    if precision < len(decimal):
        save = int(decimal[precision + 1])
    else:
        save = 0
    decimal = int(decimal[:precision])
    if (save >= 5):
        decimal += 1
    decimal = str(decimal)
    number = entier + decimal
    return float(number)

