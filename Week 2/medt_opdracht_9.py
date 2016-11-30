"""
Opdracht 9 - Loonbrief

https://dodona.ugent.be/nl/exercises/990750894/
"""


# functie voor start amount
def get_start_amount():
    # return start amount
    return int(input("Start bedrag: "))


# functie voor salaris
def get_salary():
    # array van salaris maken
    salary = []
    # count op nul zetten
    count = 0

    # wanneer de loop niet wordt afgebroken
    while True:
        # counter bijhouden voor werknemer id
        count += 1
        # input voor het salaris betreffende werknemer
        input_salary = input("Werknemer " + str(count) + ": ")
        # lengte controleren en controleren op het woordje stop
        if len(salary) > 3 and input_salary.lower() == "stop":
            break
        # salaris toevoegen aan de array
        salary.append(int(input_salary))

    # returnen van salaris
    return salary


# functie voor gemiddeld salaris
def get_average_salary(salary):
    # totaal aantal salaris
    total = sum(salary)
    # aantal werknemmers
    contributors = len(salary)
    # gemiddeld salaris per werknemer
    average = total / contributors

    # returnen van gemiddelde
    return average


def print_salary(start_amount, salary, average):
    # count op nul zetten
    count = 0
    # begin salaris of opgegeven bedrag
    total = start_amount

    # for loop die door het salaris heen gaat
    for amount in salary:
        # telkens 1tje optellen
        count += 1
        # loon erbij optellen
        total = total + amount

        # uitprinten van totaal bedrag werknemer
        print("Werknemer #" + str(count) + " fluistert €" + str(total))

    # uitprinten gemiddelde loon
    print("Gemiddeld loon: €" + str("{0:.2f}".format(average)))


def main():
    # begin bedrag verkrijgen
    start_amount = get_start_amount()
    # salaris verkrijgen
    salary = get_salary()
    # gemiddelde verkrijgen
    average = get_average_salary(salary)

    # printen van alle benodigde dingen
    print_salary(start_amount, salary, average)


if __name__ == '__main__':
    main()
