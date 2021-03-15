Ejercicios de Programación orientada a objetos: Persona
---
Programación — DAW - Ricardo Pérez López - IES Doñana - Curso 2020/2021
---

6. Crear la clase Empleado con atributos nombre y apellidos. A partir de ellos, crear los
atributos nombre_completo y email de la siguiente forma:
El nombre_completo será simplemente el nombre y los apellidos unidos con un
espacio en blanco.
El email se forma con el nombre y los apellidos (todo en minúsculas) unidos con
un . intermedio y seguido de @company.com.

7. Las instancias de la clase Empleado tienen los atributos nombre, apellidos y salario.
Crear, además, el método estático desde_cadena que analiza una cadena que contiene
esos tres valores separados por un guion y los asigna a sus atributos correspondientes.
Ejemplos:
>>> emp1 = Empleados('María', 'García', 60000)
>>> emp2 = Empleados.desde_cadena('Juan-Pérez-55000')
>>> emp1.nombre
'María'
>>> emp1.salario
60000
>>> emp2.nombre
'Juan'
>>> emp2.salario
55000
