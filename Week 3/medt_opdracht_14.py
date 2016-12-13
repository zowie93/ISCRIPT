"""
Opdracht 14 - Levensverwachting

https://dodona.ugent.be/nl/exercises/849566952/
"""


# teruggeven geslacht
def return_gender(gender):
    if gender == 'man':
        return 0
    else:
        return 4


# teruggeven roker
def return_smoker(smoker):
    if smoker:
        return -5
    else:
        return 5


# teruggeven sport status
def return_sport(status):
    if status == 0:
        return -3
    else:
        return status


# teruggeven alcohol
def return_alcohol(alcohol):
    if alcohol == 0:
        return 2
    elif alcohol >= 8:
        return -(alcohol - 7) * 0.5
    else:
        return 0


# teruggeven fastfood
def return_fastfood(fastfood):
    if fastfood:
        return 0
    else:
        return 3


# methode voor levensverwachting
def levensverwachting(gender, smoker, sport, alcohol, fastfood):
    # begin leeftijd
    age = 70.0

    # optellen van het geslacht
    age += return_gender(gender)
    # optellen van wel of geen roker
    age += return_smoker(smoker)
    # optellen van wel of niet sporten
    age += return_sport(sport)
    # optellen van wel of geen alcohol
    age += return_alcohol(alcohol)
    # optellen van eten fastfood
    age += return_fastfood(fastfood)
    # printen van leeftijd
    print(age)


def main():
    # Voorbeeld 1
    levensverwachting("man", True, 2, 10, True)
    # Voorbeeld 2
    levensverwachting("man", True, 5, 5, True)
    # Voorbeeld 3
    levensverwachting("vrouw", False, 5, 0, False)
    # Voorbeeld 4
    levensverwachting("vrouw", False, 3, 14, True)
    # Voorbeeld 5
    levensverwachting("man", False, 4, 4, False)


if __name__ == '__main__':
    main()
