"""
Opdracht 10 - Palindroomzinnen

https://dodona.ugent.be/nl/exercises/23570674/
"""


def input_phrases_count():
    return int(input("Aantal zinnen: "))


def give_input_phrase():
    return input("Zin: \n")


def strip_non_alpha_chars(string):
    return ''.join(ch.lower() for ch in string if ch.isalpha())


def check_if_palindroom(string):
    string = strip_non_alpha_chars(string)
    return string == string[::-1]


def input_phrases(count):
    phrases = []

    for i in range(0, count):
        phrase = give_input_phrase()
        phrases.append(phrase)

    return phrases


def main():
    count = input_phrases_count()
    phrases = input_phrases(count)

    for phrase in phrases:
        print("{}palindroom zin".format(['geen ', ''][check_if_palindroom(phrase)]))


if __name__ == '__main__':
    main()
