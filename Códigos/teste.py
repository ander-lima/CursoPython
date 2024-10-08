def recursiva(x):
    if x == 1:
        return -x
    else:
        return -5 * recursiva(x - 1) + x

resultado = recursiva(4)
print(resultado)
