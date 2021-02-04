from es_vocal import es_vocal
"""
# vocales(cadena: str) -> int
Función que devuelve el número de vocales en una cadena

- Especificación
    {Pre:       True
    {           vocales(s: string) -> int
    {Post:      vocales(s) = El número de vocales de s

    Pista: La especificación del profesor está en GitHub
"""

vocales = lambda s: 0 if s == '' else \
                    1 + vocales(s[1:]) if es_vocal(s[0]) else \
                        0 + vocales(s[1:])

vocales('aquí tenemos once vocales')
