"""
Opdracht 16 - Game of Life

https://dodona.ugent.be/nl/exercises/511272034/
"""


# tonen van de generatie
def showGeneration(generation):
    # loopen door de generatie
    for row in generation:
        # lege string neerzetten
        converted_row = ""
        # loopen door elke positie van de verkregen rij
        for position in row:
            # kijken of de positie true is
            if position:
                # zo ja voeg dan een X toe
                converted_row += "X "
            # anders
            else:
                # voeg dan een 0 toe
                converted_row += "O "
        # uitprinten van het resultaat
        print(converted_row)


# methode aantal buren
def number_of_neighbours(generation, ownx, owny):
    # X omzetten - 1 als input
    newX = ownx - 1
    # Y omzetten - 1 als input
    newY = owny - 1
    # aantal buren op 0 zetten
    neighbours = 0

    # loopen voor de nieuwe Y en X + 3 voor het grid
    for y in range(newY, newY + 3):
        # loopen voor de nieuwe Y en X + 3 voor het grid
        for x in range(newX, newX + 3):
            # Kijk of de range niet negatief is
            if not check_negative(x, y):
                # Kijken of het niet out of scope is
                if y < len(generation) and x < len(generation[0]):
                    # Kijken of die niet op zijn eigen positie staat
                    if ownx != x or owny != y:
                        # Als alles klopt qua y en x positie heeft die buren
                        if generation[y][x]:
                            # Na deze check telt hij de buren op
                            neighbours += 1
    # teruggeven van aantal buren
    return neighbours


# methode voor kijken of de X en Y as negatief zijn
def check_negative(x, y):
    # returned een boolean of het negatief is
    return x < 0 or y < 0


# Methode voor volgende generatie
def next_generation(generation):
    # lege array zetten
    new_gen = []

    # loopen over de Y over het aantal nummers van generatie
    for y, row in enumerate(generation):
        # lege array zetten
        new_row = []
        # loopen over X en cel van het aantal rijen van generation
        for x, cel in enumerate(row):
            # boolean op false zetten zodat die werkt als toggle
            new_cel = False
            # als die true is
            if not new_cel:
                # regel nummer 1
                if cel and number_of_neighbours(generation, x, y) in [2, 3]:
                    # cel op true zetten
                    new_cel = True
            # als die true is dus niet false
            if not new_cel:
                # regel nummer 2
                if not cel and number_of_neighbours(generation, x, y) is 3:
                    # cel op true zetten
                    new_cel = True
            # nieuwe cel aan new row appenden
            new_row.append(new_cel)
        # new row appenden aan nieuwe generatie
        new_gen.append(new_row)
    # teruggeven nieuwe generatie
    return new_gen


# Main methode
def main():
    # definieeren van generation
    generation = [[True] + [False] * 7 for _ in range(6)]
    # tonen van de huidigde generatie
    showGeneration(generation)

    # printe van buren
    print(number_of_neighbours(generation, 0, 0))
    print(number_of_neighbours(generation, 1, 1))
    print(number_of_neighbours(generation, 2, 2))

    # volgende generatie
    next_gen = next_generation(generation)
    # tonen nieuwe generatie
    showGeneration(next_gen)

    print("")

    # volgende generatie & tonen generatie
    next_gen = next_generation(next_gen)
    showGeneration(next_gen)

    print("")

    # volgende generatie & tonen generatie
    next_gen = next_generation(next_gen)
    showGeneration(next_gen)

    print("")

    # volgende generatie & tonen generatie
    next_gen = next_generation(next_gen)
    showGeneration(next_gen)


if __name__ == '__main__':
    main()
