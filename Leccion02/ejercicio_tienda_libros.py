"""
Instrucciones de la tarea:

Proporcione los siguientes datos del libro:

Proporcione el nombre:

Proporcione el ID:

Proporcione el precio:

Indica si el envio es gratuito (True/False):
"""

print('Proporcione los siguientes datos del libro:')

nombre_libro = input('Proporcione el nombre del libro: ')
print('')

libro_id = int(input('Proporcione el ID del libro: '))
print('')

precio_libro = float(input('Proporcione el precio del libro: '))
print('')

envio_gratuito_libro = input('Indica si el envio es gratuito (True/False): ')
print('')

if envio_gratuito_libro == 'True':
    envio_gratuito_libro = True
elif envio_gratuito_libro == 'False':
    envio_gratuito_libro = False
else:
    envio_gratuito_libro = 'Valor incorrecto, debe escribir True/False.'

print(f"""
      --------------------------------------------------
      
      Nombre del libro: {nombre_libro}

      Id del libro: {libro_id}

      Precio del libro: {precio_libro}

      Envío gratuito?: {envio_gratuito_libro}

      --------------------------------------------------
"""
      )
