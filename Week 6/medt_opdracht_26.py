"""
Opdracht 26 - Android patroon hacking
samen met Maarten Paauw gemaakt
"""

import binascii
import os
import sqlite3
from sys import exit


def get_patterns(gesture_file, sqlite_file):
    # array voor de pattersn
    patterns = []

    # loop door de files
    for file in gesture_file:
        # toevoegen aan array
        patterns.append(get_pattern(file, sqlite_file))

    # terrugeven
    return patterns


def get_pattern(gesture_file, sqlite_file):
    # hash verkrijgen
    gesture_hash = get_gesture_hash(gesture_file)

    # pattern verkrijgen
    pattern = get_pattern_db(gesture_hash, sqlite_file)

    # cijfer array
    numbers = []

    # loopen voor chars in de file.
    for character in pattern:

        # kijken of het een nummer is
        if character.isdigit():
            # zo ja voeg toe dan
            numbers.append(int(character))

    # teruggeven nummers
    return numbers


def get_pattern_db(gesture, sqlite_file):
    # connectie aanmaken met sqlitew file
    connection = sqlite3.connect(sqlite_file)

    # connectie voorbereiden
    current_connection = connection.cursor()

    # SQL statement
    sql = "SELECT pattern FROM RainbowTable WHERE hash=\"" + gesture + "\""

    try:
        # select uitvoeren
        current_connection.execute(sql)

    # kijken of het een db file is
    except sqlite3.DatabaseError:

        # zo nee stop
        print("Geef een database file op.")
        exit()

    # databse verkrijgen
    pattern = current_connection.fetchone()

    # verbinding sluiten
    current_connection.close()

    # kijken of die niet leeg is
    if pattern is not None:
        # pattern teruggeven
        return pattern[0]

    # programma stoppen
    print("Geen pattern met de hash.")
    exit()


def get_gesture_hash(gesture_file):
    # bestand openen
    with open(gesture_file, mode='rb') as file:

        # alles lezen uit de file
        content = file.read()

        try:

            # gesture ophalen
            gesture_hash = binascii.hexlify(content).decode()

            # lengte controleren van de hash
            if len(gesture_hash) is 40:

                # teruggeven hash
                return gesture_hash

            # geen hash.
            else:

                # stoppen programma.
                print("Bestand bevat geen hash.")
                exit()

        # als die faalt
        except TypeError:

            # stoppen programma
            print("Error: bestand kan niet gedecodeerd worden.")
            exit()


def show_patterns(combination):
    # loopen door combinaties.
    for number, combination in enumerate(combination):
        # printen pattern
        print("Patroon: " + str(number + 1))

        # pattern laten zien
        show_pattern(combination)

        # empty print
        print("")


def show_pattern(combination):
    # loopen door de rijen
    for y in range(0, 3):

        # nieuwe rij array
        row = []

        # Loopen door de posities.
        for x in range(0, 3):

            # X en Y als nummer verkrijgen
            numb_pos = y * 3 + x

            # controle of het nummer in de combinatie zit
            if numb_pos in combination:

                # toevoegen in de juiste volgorde
                row.append(str(combination.index(numb_pos) + 1))

            # what else?
            else:

                # toevoegen X
                row.append('x')

        # pattern uittekenen.
        print('***** ***** *****')
        print('| ' + ' | | '.join(row) + ' |')
        print('***** ***** *****')


def get_gesture_files(files):
    # bestanden in array
    files_arr = []

    # loopen door alle files
    for x in range(0, files):
        # toevoegen aan de files array
        files_arr.append(get_file("Path naar gesture file {0}: ".format(x + 1)))

    # bestnaden teruggeven als lijst
    return files_arr


def get_files():
    # input getal vragen
    try:
        # teruggeven getal.
        return int(input("Om hoevel patterns gaat het: "))

    # als het geen nummer is
    except ValueError:

        # stoppen programma.
        print("Error: bevat geen nummer.")
        exit()


def get_file(quest):
    # bestandsnaam opvragen
    filename = str(input(quest)).replace("\ ", " ")

    # kijken of het bestand bestaat.
    if os.path.isfile(filename):
        # naam teruggeven
        return filename

    # stoppen programma
    print("Het bestand bestaat niet.")
    exit()


def main():
    # aantal gesture files
    input_files = get_files()
    # bestandnamen.
    gesture_files = get_gesture_files(input_files)
    # SQLite file.
    sqlite_file = get_file("Path naar sqlite db: ")

    # empty print.
    print("")

    # codes.
    patterns = get_patterns(gesture_files, sqlite_file)
    # patterns tonen.
    show_patterns(patterns)


if __name__ == '__main__':
    main()
