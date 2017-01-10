"""
Opdracht 25 - Luchthavens

https://dodona.ugent.be/nl/exercises/1748605282/
"""
from math import radians, sqrt, cos, sin, atan2, pow
from collections import OrderedDict


def readairports(filename):
    # openen van gekozen file
    source_file = open(filename, "r")
    # dictionary maken van de vliegvelden
    airports = dict()

    # loopen door de source
    for index, row in enumerate(source_file):
        # newline replacen voor niks en splitten op tab
        row = row.replace('\n', '').split('\t')

        # rij 1 overslaan
        if index > 0:
            # updaten van distionary met airport afk als key en omzetten naar floats
            airports.update({row[0][1:-1]: (
                float(row[1]), float(row[2]), row[4])})

    # sorteren van de dictionary
    airports = OrderedDict(sorted(airports.items()))
    # terrugevven van vliegvelden
    return airports


def distance(code1, code2, airports):
    # airport code 1
    airport_1 = airports[code1]
    # airport code 2
    airport_2 = airports[code2]

    # breedte 1 en lengte 1 omgezet naar radiasn
    b1 = radians(airport_1[0])
    l1 = radians(airport_1[1])

    # breedte 2 en lengte 2 omgezet naar radiasn
    b2 = radians(airport_2[0])
    l2 = radians(airport_2[1])

    # formule toepassen
    formula = 6372.795 * atan2(
        sqrt(pow(cos(b2) * sin(l1 - l2), 2) + pow(cos(b1) * sin(b2) - sin(b1) * cos(b2) * cos(l1 - l2), 2)),
        sin(b1) * sin(b2) + cos(b1) * cos(b2) * cos(l1 - l2))

    # formule afronden op 8 cijfers achter de komma
    formula = round(formula, 8)

    # teruggeven formule
    return formula


def stopover(code1, code2, airports, scope=4000):
    # afstand bepalen met de distance methode
    distance_new = distance(code1, code2, airports)

    # kleinste afstand bepalen
    smallest_distance = distance_new * 10000
    # leegmaken van airportcode
    airport_code = ""

    # loopen door de lose airports
    for airport in airports:

        # kijken hoever het is van A naar B
        distance_a_b = distance(code1, airport, airports) * distance(airport, code2, airports)

        # kijken of de afstand kleiner is dan de scope en kleinste afstanden groter is dan berekende afstand
        if distance(code1, airport, airports) <= scope and \
                        distance(airport, code2, airports) <= scope and \
                        smallest_distance > distance_a_b:
            smallest_distance = distance_a_b
            # airport code vullen met airport
            airport_code = airport
    # teruggeven aiport
    return airport_code


def main():
    # printen van de meuk
    airports = readairports('luchthavens.txt')
    print(airports)
    print(airports['ADK'])
    print(airports['DCA'])
    print(airports['4OM'])
    print(distance('P60', 'MSN', airports))
    print(distance('ADK', 'DCA', airports))
    print(stopover('ADK', 'DCA', airports, 4000))


if __name__ == '__main__':
    main()
