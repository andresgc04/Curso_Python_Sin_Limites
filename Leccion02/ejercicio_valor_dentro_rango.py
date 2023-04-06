valor = int(input('Por favor, escribe el valor: '))

valor_minimo = 0
valor_maximo = 5

dentro_rango = valor >= valor_minimo and valor <= valor_maximo

if dentro_rango:
    print(f'El valor de {valor} está dentro del rango.')
else:
    print(f'El valor de {valor} está fuera del rango.')