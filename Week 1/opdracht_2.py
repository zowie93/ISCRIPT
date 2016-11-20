"""
Opdracht 2 - Radialen naar graden

https://dodona.ugent.be/nl/exercises/975017137/
"""
import math

# input voor het aantal radialen
input_radials = float(input('Voer hier het aantal radialen in: '))


# functie voor het converteren van radial naar hoek, minuten en seconden
def convert_radials(radials):
    # variabelen voor graden hoek en pi
    angle = int(180)
    pi = math.pi
    result = ((angle / pi) * radials)

    # variabelen voor het converteren naar graden minuten en seconden
    degrees = int(result)
    minuts = (result - int(result)) * 60
    minuts_int = int((result - int(result)) * 60)
    seconds_int = int((minuts - int(minuts)) * 60)

    # printen van de uitkomsten
    print(degrees)
    print(minuts_int)
    print(seconds_int)


# aanroepen van de functie
convert_radials(input_radials)
