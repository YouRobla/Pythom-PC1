cantPayasos = int(input('Ingrese la cantidad de payasos por enviar:'))

cantMuniecas =int(input('Ingrese la cantidad de muñecas por enviar:'))

pesoPayasos=cantPayasos*112

pesoMuniecas=cantMuniecas*75

print(f'DETALLE DE ENVIO\nPeso payasos:{pesoPayasos}g\nPeso muñecas:{pesoMuniecas}g\n-----------\nPeso Total:{pesoPayasos+pesoMuniecas}g')