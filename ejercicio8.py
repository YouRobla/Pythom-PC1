time = input("Ingrese la hora en formato hh:mm: ")

hours, minutes = time.split(":")


hours = int(hours)
minutes = int(minutes)


time_in_hours = hours + (minutes / 60)

if 7 <= time_in_hours <= 8:
    print("Es la hora del desayuno.")
elif 12 <= time_in_hours <= 13:
    print("Es la hora del almuerzo.")
elif 18 <= time_in_hours <= 19:
    print("Es la hora de la cena.")
