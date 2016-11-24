"""
Opdracht 5 - Territorial wateren

https://dodona.ugent.be/nl/exercises/587558403/
"""

import math


def get_coordinates():
    # coordinaten array
    coordinates = []

    # inputs voor alle assen
    x1 = float(input("X1: "))
    y1 = float(input("Y1: "))
    x2 = float(input("X2: "))
    y2 = float(input("Y2: "))
    x3 = float(input("X3: "))
    y3 = float(input("Y3: "))

    # appenden aan de array
    coordinates.append((x1, y1))
    coordinates.append((x2, y2))
    coordinates.append((x3, y3))

    # terug geven van de coordinaten
    return coordinates


def get_voetpunt(cor_x_y_1, cor_x_y_2, cor_x_y_3):
    # opsplitsen coordinaten in verschillende assen (tulps)
    x1, y1 = cor_x_y_1
    x2, y2 = cor_x_y_2
    x3, y3 = cor_x_y_3

    # bereking u
    u = ((x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)) / (math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    # bereking xv en yv
    xv = x1 + u * (x2 - x1)
    yv = y1 + u * (y2 - y1)

    # voet punt tuple
    punt = (xv, yv)

    # terug geven van de coordinaten
    return punt


def get_afstand(cor_xv, cor_yv, cor_x3, cor_y3):
    # terug geven van de afstand
    return math.sqrt(math.pow(cor_xv - cor_x3, 2) + math.pow(cor_yv - cor_y3, 2))


def get_zone(afstand_zone):
    # if else statemant voor de zones bepaling voor elke zone
    if 0.0 <= afstand_zone <= 12.0:
        result = "territoriale wateren"
    elif 12.0 <= afstand_zone <= 24.0:
        result = "aansluitende zone"
    elif 24.0 <= afstand_zone <= 200.0:
        result = "exclusieve economische zone"
    else:
        result = "internationale wateren"

    return result


def main():
    # coordinaten opsplitsen
    coordinates_x_y_1, coordinates_x_y_2, coordinates_x_y_3 = get_coordinates()

    # voetpunt verkrijgen
    voet_punt = get_voetpunt(coordinates_x_y_1, coordinates_x_y_2, coordinates_x_y_3)

    # voetpunt opsplitsen in xv en yv
    xv, yv = voet_punt
    x3, y3 = coordinates_x_y_3

    # afstand berekenen
    afstand = get_afstand(xv, yv, x3, y3)

    # zone bepalen
    zone = get_zone(afstand)

    # outputs voor elke methode
    print('voetpunt:', voet_punt)
    print('afstand:', afstand, 'zeemijl')
    print('zone:', zone)


if __name__ == '__main__':
    main()
