# Subtipos - Transitividad

|   Subtipodirecto:    |       subtipo:        |     subtipo propio:     |
|----------------------|-----------------------|-------------------------|
| ``float <1 double``  |   ``float <: double`` |     ``float < double``  |
| ``long <1 float``    |   ``long <: float``   |     ``long < float``    |

## Ejemplos:
- ``long <: double``

    Es correcto, porque donde se espera un double, puedo poner un long

- ``double <: long``

    Esto no es posible, porque se pierde información (su parte fraccionaria).
> ``long`` es subtipo de ``double``. ``double`` es supertipo de ``long``.

## Subtipados de tipos referencia
> Dado un tipo referencia C, el supertipo directo de C es la superclase directa de C.

A diferecnia de python, donde todos los tipos son clases, en Java no.
Aquí tenemos muchos tipos: Unos son clases, otros primitivos, otros arrays, etc.

> "Tipo" es el concepto general, que engloba a todos éstos.

## Conversiones entre datos primitivos

Es posible convertir valores de un tipo a otro, siempre u ciando se cumplan ciertas condiciones y teniendo en cuenta que, en determinadas ocasiones... [apuntes].

### Casting
El asting o moldeado de tipos, es una operacion de conversión entre tipos.

En el caso de primitivos, el casting se usa para:

- Convertir un valor de un tipo numerico a un valor similar de otro tipo numérico.
- Garantizar nosequé [...]

```java
(short) (4 + 3) // Afecta a la expresión 4 + 3. Devuelve short.
(short) 4 + 3 // Afecta sólo a la expresión 4. Devuelve int.
```

### De Ampliación (Widening)

Existen 19 conversiones de ampliacion

- De byte a short, int, long, float, double.
- De short a int, long, float, double.
- De char a int, long, float, double.
- De int a long, float, double.
- De long a float o double.
- De float a a double.

Una conversión de ampliación de primitivos, nunca pierde información sobre la magnitud general de un valor numérico.

Una conversion de ampliacion de un valor int a ong a float, o de un valor long a double puede producir una perdida de precsión.

Ejemplo:
```java
(float) 9.22337208457661269869484L
==> 9.223372E18     // 9223372000000000000
```
> Como se puede observar, hemos pérdido varias cifras,pero la posición de sus cifras es correcta.

### De reduccion (narrowing)

- De short a byte o char.
- De char a byter o short.
- De int a byte, short o char.
- De long a int, byte, short o char.
- De float a long, int, byte, short o char.
- De double a float, long, int, byte, short o char.

En una conversión de reducción se puede perder información sobre la magitud general de un valor numérico, su precisión y su rango.

> Se hace mediante las reglas de redondeo de IEEE-754.
