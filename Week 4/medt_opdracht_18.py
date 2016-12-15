"""
Opdracht 18 - Experimentele verjaardagsparadox

https://dodona.ugent.be/nl/exercises/1257408557/
"""
import random


def check_duplicates(list):
    if len(set(list)) != len(list):
        return False
    else:
        return True


def happen_together(number1, number2):
    number_list = []

    for trial in range(number1):
        rand_numb = random.randrange(number2)
        number_list.append(rand_numb)

    return check_duplicates(number_list)


def estimate_chance(number1, number2, tests):

    duplicates = 0

    for trial in range(tests):
        if happen_together(number1, number1):
            duplicates += 1

    print(duplicates / tests)
    return duplicates


def main():
    print(happen_together(3, 6))
    print(happen_together(3, 6))

    print(estimate_chance(6, 2, 10000))
    print(estimate_chance(365, 23, 10000))


if __name__ == '__main__':
    main()
