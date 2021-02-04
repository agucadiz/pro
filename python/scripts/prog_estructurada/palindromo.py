cadena = 'A ti no, bonita'
def palindromo(s):

    # Descomponemos la frase con str.split()
    palabras = s.split()

    # Eliminamos puntuaciones con str.strip()
    lista_plana = []

    for p in palabras:
        q = p.strip('.').strip(',')
        lista_plana.append(q)

    frase_plana = ''.join(lista_plana)

    frase = frase_plana.lower().replace('á', 'a').replace('é', 'e')\
        .replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

    esarf = frase[::-1]

    if frase == esarf:
        return True
    else:
        return False

palindromo(cadena)
