# Ejercicio de práctica con funciones recursivas
"""
producto_rango(a, b)
Funcion recuresiva que calcule el producto de los numeros comprendidos
entre a y b

- Especificación:
    { Pre:  True
    {       producto_rango(a: int, b: int) -- > int
    { Post: producto_rango(n) = el producto de los nuemros comprendidos
                                entre a y b.

producto_rango(a, b) = 1 cuando a > b   (caso base)

- Lógica optmista:
producto_rango(6, 8) = 6 * 7 * 8
producto_rango(5, 8) = 5 * producto_rango(6, 8)
"""

producto_rango = lambda a, b: 1 if a > b else \
    a * producto_rango(a + 1, b)
