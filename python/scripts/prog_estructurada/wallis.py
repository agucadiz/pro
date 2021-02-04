'''
def wallis(n):
    numerador = 2
    denominador = 1
    resultado = numerador / denominador

    c = 1
    while c < n:
        if c % 2 == 0:
            numerador += 2
        else:
            denominador += 2
        resultado  *= numerador / denominador
        c += 1
    return resultado * 2
'''
# wallis(5000)

def wallis(n):
    numerador = 2
    denominador = 1
    resultado = numerador / denominador

    for i in range(n):
        resultado  *= numerador / denominador
        if i % 2 == 0:
            denominador += 2
        else:
            numerador += 2
    return resultado
