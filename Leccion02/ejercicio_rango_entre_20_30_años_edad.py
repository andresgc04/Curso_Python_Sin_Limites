edad = int(input('Introduce tú edad: '))

veintes = 20 <= edad < 30

treintas = 30 <= edad < 40

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