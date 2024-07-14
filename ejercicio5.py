showsVistos = int(input('Ingrese cuántos shows musicales ha visto en el último año: '))

if showsVistos >3:
    condicion=True
    print(f'{condicion}\nEl usuario ha visto más de 3 shows')

else:
    condicion=False
    print(f'{condicion}\nEl usuario no ha  visto más de 3 shows')

