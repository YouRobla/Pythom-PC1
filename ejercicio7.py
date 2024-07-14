num1=int(input('Ingrese el primer número a operar:'))
num2=int(input('Ingrese el segundo número a operar:'))

while True:
    alternativa=input('OPERACIONES DISPONIBLES \n1.Mostrar una suma de los dos números \n2.Mostrar una resta de los dos números (el primero menos el segundo) \n3.Mostrar una multiplicación de los dos números \nIngrese alternativa(1,2,3):')
    if alternativa in ['1','2','3']:
        break
    else:
        print('Ingrese una opcion validad.')

if alternativa=='1':
    respuesta=num1+num2
elif alternativa=='2':
    respuesta=num1-num2
elif alternativa=='3':
    respuesta=num1*num2

print(f'La solucion es {respuesta}')
