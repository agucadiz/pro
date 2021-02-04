"""
digitos:
Función que devuelve el número de dígitos de un número

- Especificación:
    { Pre:  n >= 0
    {       digitos(n: int) -> int
    { Post: digitos(n) = el número de dígitos de n

- Ejemplo de una implementación ad-hoc (Evitar!)
    digitos = lambda n: 1 if n < 10 else \
                        2 if n < 100 else \
                        [...]

- Planteamientos (Buscando casos base)
 - Si el número es menor de diez, está claro que tiene sólo un dígito
 - 1 si n < 10 (caso base)

Imaginemos que tenemos el número 7548
Si supiesemos obtener el numero de digitos de 754, significaría que:
    digitos(7548) = digitos(754) + 1
    digitos(7548) = digitos(75) + 1 + 1
    [...]

- Evaluemos un ejemplar de digitos:
digitos(235)                                                        # evalúa digitos y devuelve lambda
= lambda n: 1 if n < 10 else 1 + digitos(n // 10)(235)              # evalúa 235
= lambda n: 1 if n < 10 else 1 + digitos(n // 10)(235)              # beta-reducción
= (1 if 235 < 10 else 1 + digitos(23))                              # evalúa el if
= 1 + (digitos(23))                                                 # evalúa digitos y devuelve lambda
= 1 + lambda n: 1 if n < 10 else 1 + digitos(n // 10)(23)           # beta-reducción
= 1 + (1 if 23 < 10 else 1 + digitos(2))                            # evalúa el if
= 1 + (1 + digitos(2))                                              # evalúa digitos y devuelve lambda
= 1 + (1 + lambda n: 1 if n < 10 else 1 + digitos(n // 10)(2))      # beta reducción
= 1 + (1 + (1 if 2 < 10 else digitos(0)))                           # evalúa el if
= 1 + (1 + 1)                                                       # evalua (1 + 1)
= 1 + 2                                                             # evalua (1 + 2)
= 3                                                                 # devuelve 3

- Evaluación de forma resumida
digitos(235)
= 1 + digitos(23)
= 1 + (1 + digitos(2))
= 1 + (1 + 1)
= 1 + 2
= 3

"""

digitos = lambda n: 1 if n < 10 else 1 + digitos(n // 10)
