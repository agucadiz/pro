# Ejercicio de práctica con funciones recursivas
"""
# suma_rango(a, b):
Función recursiva que calcula la suma de los números comprendidos entre a y b,
siendo a y b dos números enteros que se reciben como argumentos.

## Especificación:
```
    { Pre:  True
    {       suma_rango(a: int, b: int) -> int
    { Post: suma_rango(a, b) = la suma de todos los numeros comprendidos
                                entre a y b.

    suma_rango(a, b) = 0 cuando a > b               (caso base)
    suma_rango(a, b) = a + suma_rango(1 + a, b)     (caso recursivo)
```

## Pensamiento optimista (hipótesis inductiva):
Si yo puedo hacer suma_rango(5, 7), hacer el suma_rango(4, 7) es lo mismo que:
```
4 + suma_rango(5, 7)
4 + 5 + 6 + 7 = 4 + suma_rango(5, 7)
```
"""
suma_rango = lambda a, b: 0 if a > b else \
    a + suma_rango(a + 1, b)
