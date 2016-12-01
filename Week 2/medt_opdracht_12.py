"""
Opdracht 12 - Rorschahtest

https://dodona.ugent.be/nl/exercises/695254392/
"""


# functie voor omdraaien multiple line string input
def reflect_input(strings):
    # loop door de ingevulde strings
    for string in strings:
        # elke string apart printen
        print(string, end="")
        # omdraaien van eerdergeprint strings
        for c in range(len(string) - 1, 0 - 1, -1):
            print(string[c], end="")
        print("\n", end="")


def main():
    # input is leeg in het begin
    input_string = ' '
    # arraylist van strings
    strings = []
    # wanneer de string niet leeg zijn print dan alle strings achterstevoren
    while input_string != "":
        input_string = input()
        strings.append(input_string)

    # omdraaien ingevoerde strings
    reflect_input(strings)


if __name__ == '__main__':
    main()
