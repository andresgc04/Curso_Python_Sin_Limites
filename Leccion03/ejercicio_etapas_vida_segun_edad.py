"""
Proporciona tu edad:

0-10: La infancia es increíble...
10-20: Muchos cambios y mucho estudio...
20-30: Amor y comienza el trabajo...

Cualquier otro valor: Etapa de vida no reconocida.
"""

edad = int(input('Proporciona tu edad: '))

mensaje = None

"""
if edad >= 0 and edad < 10:
    mensaje = 'La infancia es increíble...'
    print(mensaje)
elif edad >= 10 and edad < 20:
    mensaje = 'Mucho cambios y mucho estudio...'
    print(mensaje)
elif edad >= 20 and edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
    print(mensaje)
else:
    mensaje = 'Cualquier otro valor: Etapa de vida no reconocida.'
    print(mensaje)
"""

# Código Refactorizado:

if 0 <= edad < 10:
    mensaje = 'La infancia es increíble...'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y muchos estudios...'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Cualquier otro valor: Etapa de vida no reconocida.'

print(f'Tú edad es: {edad}, {mensaje}')
