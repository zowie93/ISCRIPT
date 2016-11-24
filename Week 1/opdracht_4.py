"""
Opdracht 4 - Paardensprong

https://dodona.ugent.be/nl/exercises/56374393/
"""
import string


def get_position():
    # inputs voor de stap posities
    pos_1 = input("Startpositie : ")
    pos_2 = input("Positie na de Zet : ")

    # terug geven van de positie
    return pos_1, pos_2


def calc_step(pos_1, pos_2):
    # beide posities worden omgezet naar een array
    pos_1 = list(pos_1)
    pos_2 = list(pos_2)

    # gegevens posities splitten in losse variables
    pos_1_letter, pos_1_number = pos_1
    pos_2_letter, pos_2_number = pos_2

    # opvragen van de huidige positie van het gegeven letter
    pos_1_index = int(string.ascii_lowercase.index(pos_1_letter.lower()) + 1)
    pos_2_index = int(string.ascii_lowercase.index(pos_2_letter.lower()) + 1)

    # de mogelijke stappen laten zien
    steps = horse_step(int(pos_1_index), int(pos_1_number))

    # geef terug of de sprong gemaakt kan worden of niet
    return (pos_2_index, int(pos_2_number)) in steps


def horse_step(x, y):
    # array voor de posities
    array_positions = []

    # 8 mogelijke combinaties voor de stappen
    offset_steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    # controleer de stappen loop
    for steps in offset_steps:

        # nieuwe x en y waarden
        new_x_value = x + steps[0]
        new_y_value = y + steps[1]

        # check of het paard niet van het speelbord afvalt
        if new_x_value >= 9 or new_x_value < 1 or new_y_value >= 9 or new_y_value < 1:
            continue

        # toevoegen aan de array
        else:
            array_positions.append((new_x_value, new_y_value))

    # terug geven van de posities
    return array_positions


def print_possibilities(pos_1, pos_2, possible):
    # uitprinten van mogelijkheid met formatting
    if possible:
        print('het paard kan springen van', pos_1, 'naar', pos_2)
    else:
        print('het paard niet springen van', pos_1, 'naar', pos_2)


def main():
    # posities inputs weergeven
    (pos_1, pos_2) = get_position()
    # berekenen van de stappen
    possible = calc_step(pos_1, pos_2)
    # uitprinten van de mogelijkheid
    print_possibilities(pos_1, pos_2, possible)


if __name__ == '__main__':
    main()
