"""
Opdracht 6 - Zweettest

https://dodona.ugent.be/nl/exercises/1173716008/
"""


def input_months():
    # terug geven aantal maanden
    return float(input("Hoeveel maanden oud ben je? "))


def input_mmol():
    # terug geven aantal mmol
    return float(input("Vul hier het gemeten chlorideconcentratie van de patiënt voor, uitgedrukt in mmol/L: "))


def calculate_diagnose():
    # definieren van maanden en mmol
    month = input_months()
    mmol = input_mmol()

    # check voor aantal maanden en mmol/L
    if month <= 6:
        if mmol <= 29:
            result = "CF is hoogst onwaarschijnlijk"
        elif 30 <= mmol <= 59:
            result = "CF is mogelijk"
        elif mmol >= 60:
            result = "CF is waarschijnlijk"
    else:
        if mmol <= 39:
            result = "CF is hoogst onwaarschijnlijk"
        elif 40 <= mmol <= 59:
            result = "CF is mogelijk"
        elif mmol >= 60:
            result = "CF is waarschijnlijk"

    return result


def main():
    # print de diagnose
    print(calculate_diagnose())


if __name__ == '__main__':
    main()
