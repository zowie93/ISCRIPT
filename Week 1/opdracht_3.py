"""
Opdracht 3 - Poolcoordinaten

https://dodona.ugent.be/nl/exercises/333498206/
"""

import math


# converteren van x en y coordinaten
def convert_cordinates(x_cor, y_cor):
    # formule met wortel en kwardraat
    r = math.sqrt(math.pow(x_cor, 2) + math.pow(y_cor, 2))

    # check voor als de x coordinaat 0 is dan is de hoek 90 graden anders rekend die hem zelf uit
    if x_cor == 0:
        result = math.pi * 0.5
    else:
        result = math.atan(y_cor / x_cor)

    # uitprinten van het resultaat
    print(r, "\n", result)


# main methode
def main():
    # x en y var voor de coordinaten
    x = float(input("Vul hier de X-as in: "))
    y = float(input("Vul hier de Y-as in: "))

    # aanroepen methode convert_cordinates
    convert_cordinates(x, y)


# runtime methode
if __name__ == '__main__':
    main()
