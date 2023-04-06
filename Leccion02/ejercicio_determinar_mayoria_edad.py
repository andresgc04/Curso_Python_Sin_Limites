edad_adulto = 18

edad_persona = int(input('Por favor, proporciona tú edad: '))

if edad_persona >= edad_adulto:
    print(f'La persona con edad de {edad_persona} años, es un adulto.')
else:
    print(f'La persona con edad de {edad_persona} años, es menor de edad.')