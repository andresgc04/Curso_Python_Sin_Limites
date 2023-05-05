edad = int(input('Introduce tú edad: '))

veintes = edad >= 20 and edad < 30

treintas = edad >= 30 and edad < 40

if veintes or treintas:
    #print('Dentro del rango de 20 años o 30 años.')

    if veintes:
        print('Dentro de los 20 años.')
    elif treintas:
        print('Dentro de los 30 años')
    else:
        print('Fuera de rango.')
else:
    print('No esta dentro de los 20 años y ni de los 30 años.')