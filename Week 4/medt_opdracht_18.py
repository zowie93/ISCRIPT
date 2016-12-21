"""
Opdracht 18 - Experimentele verjaardagsparadox

https://dodona.ugent.be/nl/exercises/1257408557/
"""
import random

# methode voor duplicate lijst checken
def check_duplicates(list):
    # als de lijst niet gelijk is aan de lijst return true
    if len(set(list)) != len(list):
        return True
    # anders flase
    else:
        return False


# methode voor als het samen gebeurd
def happen_together(number1, number2):
    # lege araay voor nummers
    number_list = []

    # loop voor random nummer
    for trial in range(number2):
        # random range pakken voor nummer 1
        rand_numb = random.randrange(number1)
        # toevoegen aan de array
        number_list.append(rand_numb)
    # teruggeven of het nummer dubbel voorkomt
    return check_duplicates(number_list)


# methode voor kans dat het nummer dubbel voorkomt
def estimate_chance(number1, number2, tests):
    # dubbele nummers op 0 zetten
    duplicates = 0
    # loop als het nummer dubbel voorkomt in het aantal testen
    for trial in range(tests):
        # check of de nummers dubbel voorkomen
        if happen_together(number1, number2):
            # 1 optellen bij dubbele nummers
            duplicates += 1
    # teruggeven van dubbele nummers gedeeld door het aantal testen
    return duplicates / tests


def main():
    # printen methode happen together
    print(happen_together(3, 6))
    print(happen_together(3, 6))

    # printen berekening kansen op dubbele nummers
    print(estimate_chance(6, 2, 10000))
    print(estimate_chance(365, 23, 10000))


if __name__ == '__main__':
    main()
