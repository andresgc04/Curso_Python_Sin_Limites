'''
Instrucciones de la tarea:
- En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo,
  para ello deberemos crear las siguientes variables:

alto (int)
ancho (int)

- El usuario debe proporcionar los valores de largo y ancho,
  y después se debe de imprimir el resultado en el siguiente formato
  (no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

  Proporciona el alto:
  Proporciona el ancho:

  Area: <area>
  Perimetro: <perimetro>

  Las formulas para calcular el area y el perimetro de un rectangulo son las siguientes:
  Area: alto * ancho
  Perimetro : (alto + ancho) * 2
'''

alto = int(input('Proporciona el alto del rectangulo: '))
print('')

ancho = int(input('Proporciona el ancho del rectangulo: '))
print('')

area = alto * ancho

perimetro = (alto + ancho) * 2

print(f'El resultado del área es: {area}')
print('')

print(f'El resultado del perimetro es: {perimetro}')
print('')