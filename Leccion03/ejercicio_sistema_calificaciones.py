"""
Instrucciones de la tarea:

El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

El usuario proporcionará un valor entre 0 y 10.

Si está entre 9 y 10: Imprimir una A.

Si está entre 8 y menor a 9: Imprimir una B.

Si está entre 7 y menor a 8: Imprimir una C.

Si está entre 6 y menor a 7: Imprimir una D.

Si está entre 0 y menor a 6: Imprimir una F.

Cualquier otro valor debe imprimir: Valor incorrecto.

Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""

nota = int(input('Proporciona una nota entre 0 y 10: '))

calificacion = None

if 9 <= nota <= 10:
    calificacion = 'A'
elif 8 <= nota < 9:
    calificacion = 'B'
elif 7 <= nota < 8:
    calificacion = 'C'
elif 6 <= nota < 7:
    calificacion = 'D'
elif 0 <= nota < 6:
    calificacion = 'F'
else:
    calificacion = 'Valor incorrecto.'

print(f'Tú nota es: {nota} y tú calificación es: {calificacion}')
