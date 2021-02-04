d1 = {'nombre': 'paco', 'teoria': [3.5, 7.2, 8.0], 'practica': [4.0, 7.5]}
d2 = {'nombre': 'miguel', 'teoria': [1.0, 5.2, 3.8], 'practica': [2.5, 6.2]}
d3 = {'nombre': 'ana', 'teoria': [1.0, 4.2, 2.8], 'practica': [2.5, 1.2]}

def notas(dic):
    # Obtenemos la media de la teoría
    media_teoria = 0.0
    for i in dic['teoria']:
        media_teoria = media_teoria + i
    media_teoria = round(media_teoria / len(dic['teoria']), 1)
    # Obtenemos la media de la practica
    media_practica = 0.0
    for i in dic['practica']:
        media_practica = media_practica + i
    media_practica = round(media_practica / len(dic['practica']), 1)
    # Comprobamos los requisitos para obtener media
    if media_teoria < 3 or media_practica < 3:
        media = min(media_teoria, media_practica)
    else:
        media = round(media_teoria * 0.3 + media_practica * 0.7, 1)
    # Modificamos el diccionario
    del(dic['teoria'])
    del(dic['practica'])
    dic['media_teoria'] = media_teoria
    dic['media_practica'] = media_practica
    dic['media'] = media
