montoConsumido = int(input('Ingrese  monto consumudio:'))

while True:
    respuesta = input('¿Desea dejar propina? (si/no): ').strip().lower()
    if respuesta in ['sí', 'si', 'no']:
        break
    else:
        print("Por favor, ingrese 'sí' o 'no'.")

if respuesta == 'si':
    porcentajeComida = int(input('Qué porcentaje de propina deseas dejar (en base a tu consumo) %: '))
    propina = montoConsumido * (porcentajeComida / 100)
    print(f'La propina es: {propina}')
else:
    propina=0
    print('No se dejará propina.')

print(f'BOLETA DE VENTA \nConsumido :{montoConsumido} \nPropina:{propina}\nTOTAL:{montoConsumido+propina}')
