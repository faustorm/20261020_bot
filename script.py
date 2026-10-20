"""
Bot sencillo que interactúa

Vamos a calcular la edad a mano, como animales
"""
import datetime

HOY = datetime.datetime.now()
CURRENT_YEAR = HOY.year
CURRENT_MONTH = HOY.month
CURRENT_DAY = HOY.day

meses = {
    "enero" : 1,
    "febrero": 2,
    "marzo" : 3,
    "abril" : 4,
    "mayo": 5,
    "junio": 6,
    "octubre": 10
}

#pedir nombre
name = input("¿Cómo te llamas? ")

#pedir año
year = int(input("Dime tu año de nacimiento: "))

#pedir mes
month = input("Dime tu mes de nacimiento en español: ")
#convertir mes a número

month_number = meses[month.lower()]

#pedir dia
day = int(input("Qué dia? "))

#calculamos la edad
print("Día:", day, "Mes:", month, "Mes en número:", month_number, "Año", year)

edad = CURRENT_YEAR - year

if month_number == CURRENT_MONTH:
    if day == CURRENT_DAY:
        print(f"Felicidades {name}, a qué te invitas?")
    elif day > CURRENT_DAY:
        edad -= 1
elif month_number > CURRENT_MONTH:
    edad -= 1

if edad > 25 and edad <= 40:
    print(f"¿Tienes {edad} años? Ojalá llegues a la edad que aparentas")
elif edad > 40:
    print(f"¿Qué tal el pádel con Marcos a los {edad}?")
else:
    print(f"¿{edad} quién los pillara?")