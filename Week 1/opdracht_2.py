"""
Opdracht 2 - Radialen naar graden

https://dodona.ugent.be/nl/exercises/975017137/
"""
import math


# functie voor het converteren van radial naar hoek, minuten en seconden
def convert_radials(radials):
    result = single_radial(radials)
    print_result(result)


# input voor het aantal radialen
def input_radials():
    return float(input('Voer hier het aantal radialen in: '))


def single_radial(rad):
    return int(180) / math.pi * rad


def print_result(result):
    # variabelen voor het converteren naar graden minuten en seconden
    degrees = int(result)
    minuts = (result - int(result)) * 60
    seconds = int((minuts - int(minuts)) * 60)

    # printen van de uitkomsten
    print(int(degrees), "\n", int(minuts), "\n", int(seconds))


# main functie
def main():
    # aanroepen van de functie
    input_radial = input_radials()
    convert_radials(input_radial)

# runtime methode
if __name__ == '__main__':
    main()
