"""
Opdracht 13 - Heen en terug

https://dodona.ugent.be/nl/exercises/738605545/
"""


# input zin
def print_string_input():
    # teruggeven van zin input
    return input("Zin: ")


# input breedte kolommen
def print_width_input():
    # teruggeven van breedte input
    return int(input("Breedte: "))


# decodeer functie
def decodeer(input, width):
    # opslaan van input en breedte in de array dmv een loop
    input_array = [input[i:i + width] for i in range(0, len(input), width)]
    # loopen door de gehele input array
    for i in range(0, len(input_array)):
        if i % 2 != 0:
            input_array[i] = input_array[i][::-1]
    # result als leeg
    result = ""
    # loopen voor de juiste kolommen input
    for i in range(0, width):
        for j in range(0, len(input_array)):
            result += input_array[j][i]

    # printen van result
    print(result)


def main():
    # definieren input string
    input_string = print_string_input()
    # definieren input kolombreedte
    width = print_width_input()

    # decoderen van het bericht
    decodeer(input_string, width)


if __name__ == '__main__':
    main()
