"""
# es_vocal
Devuelve True o False dependiendiendo de si el carácter recibido es una vocal
## Especificación
{Pre:   True
{       es_vocal(c: string) -> bool
{Post:  es_vocal(c) = {True si c es una vocal / False en caso contrario}
"""

es_vocal = lambda c: True \
                    if c.lower() == 'a' or c.lower() == 'á' or \
                    c.lower() == 'à' or c.lower() == 'ä' or c.lower() == 'â' \
                    or c.lower() == 'e' or c.lower() == 'é' or \
                    c.lower() == 'è' or c.lower() == 'ë' or c.lower() == 'ê' \
                    or c.lower() == 'i' or c.lower() == 'í' or \
                    c.lower() == 'ì' or c.lower() == 'ï' or c.lower() == 'î' \
                    or c.lower() == 'o' or c.lower() == 'ó' or \
                    c.lower() == 'ò' or c.lower() == 'ö' or c.lower() == 'ô' \
                    or c.lower() == 'u' or c.lower() == 'ú' or \
                    c.lower() == 'ù' or c.lower() == 'ü' or c.lower() == 'û' \
                    else False
