"""
Opdracht 7 - Interessante getallen

https://dodona.ugent.be/nl/exercises/211647828/
"""


# input van het aantal testen
def input_tests():
    return int(input("Aantal testen: "))


# input van aantal getallen
def input_ints():
    return int(input("getal: "))


# functie aantal keer de som
def sum(numb):
    number = int(numb)
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum


# functie uitreknen natuurlijkgetal
def calculate(numb):
    # beginnummer
    start_number = 1
    # loop voor getal vinden
    while True:
        # kijken of het deelbaar is en gelijk aan de invoer
        if (start_number % numb == 0) and sum(start_number) == numb:
            return start_number
        else:
            start_number += 1


# functie voor het vragen van de ingevoerde testen en printen getallen
def testen_check():
    # input aanroepn
    testen = input_tests()

    # array maken van de getallen
    numbers = []

    # check of de testen onder de 50 zijn
    if testen <= 50:
        # loop voor de inputs van de getallen
        for i in range(0, testen):
            # invoer getallen
            invoer = input_ints()
            # kijken of de invoer binnen de juiste scope zit
            if 0 < invoer <= 100:
                # toevoegen van getallen aan de array
                numbers.append(invoer)
            else:
                print("Dit getal is niet mogelijk")

        # for loop voor het uitprinten van de getallen
        for number in numbers:
            print(calculate(number))
    else:
        print("Getal is groter dan 50")
        testen = input_tests()

        # check of de testen onder de 50 zijn
        if testen <= 50:
            # loop voor de inputs van de getallen
            for i in range(0, testen):
                # invoer getallen
                invoer = input_ints()
                # kijken of de invoer binnen de juiste scope zit
                if 0 < invoer <= 100:
                    # toevoegen van getallen aan de array
                    numbers.append(invoer)
                else:
                    print("Dit getal is niet mogelijk")

            # for loop voor het uitprinten van de getallen
            for number in numbers:
                print(calculate(number))


def main():
    # functie uitvoeren bovenstaande functies
    getallen = testen_check()


if __name__ == '__main__':
    # definieer main
    main()
