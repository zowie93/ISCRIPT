"""
Opdracht 22 - Cryptogrammen

https://dodona.ugent.be/nl/exercises/189652425/
"""


# printen van space tussen prints
def pr_new() -> str:
    print()
    print("---------------------------------")
    print()


def cryptogram(puzzle, solution):
    # list aanmaken van de puzzle
    puzzle_list = list(puzzle)
    # list aanmaken van de oplossing
    solution_list = list(solution)
    # enumaration van de oplossing
    solution_enumerate = enumerate(solution_list)
    # speciale characters die voor komen
    special_chars = ["?", "."]
    # vraagteken
    question_mark = "?"
    # antwoord
    answer = ""

    # herhaalse karakters
    repeated_char = {}

    # loopen voor de oplossing
    for index_solution, puzzle_solution in solution_enumerate:
        # kijken of de letter alphabetic is
        if puzzle_solution.isalpha():
            # karakter uit de puzzle
            char_puzzle = puzzle_list[index_solution].lower()
            # karakter van de solution
            char_solution = puzzle_solution.lower()

            # updaten van de array
            repeated_char.update({
                char_puzzle: char_solution
            })

    # loopen voor de oplossing
    for index, char in enumerate(solution_list):
        # kijken of de karakter niet in de speciale karakters staat
        if char not in special_chars:
            # karakter toevoegen aan het antwoord
            answer += char
        # als het speciale karakter een vraagteken is
        elif char is special_chars[0]:
            # letter van de puzzle
            puzzle_char = puzzle_list[index]
            # lowercase van de puzzle letter
            puzzle_lower = puzzle_char.lower()

            # kijken of de lowercase versie herhaalse karakters staat
            if puzzle_lower in repeated_char:
                # opslaan van karakter
                char_possible = repeated_char[puzzle_lower]
                # Als de karakter uppercase is
                if puzzle_char.isupper():
                    # opslaan van karakter als hoofdletter
                    char_possible = char_possible.upper()
                # toevoegen aan de string
                answer += char_possible
            else:
                # als de letter niet gevonden kan worden is het een vraagteken
                answer += question_mark
        else:
            # toevoegen teken
            answer += char
    # teruggeven antwoord
    return answer


def main():
    puzzle = 'Qmvrbwlf xwkd iopzlw vf zml pcwvfxzvyl.'
    solution = 'Ch?ld??? ??ow fas??r ?n ??? ?p?i?gt?me.'
    print(cryptogram(puzzle, solution))
    pr_new()

    puzzle = 'Zhp suxobpuw sbmtkopw Nxwkdnx.'
    solution = '?h? p?n???a? ?rod?ces I???l??.'
    print(cryptogram(puzzle, solution))
    pr_new()

    puzzle = 'Jujso ldmtq wyjqi tvadi ltek tq lads tw t wcqnej xjee.'
    solution = '?v?ry ??ma? ?p??? ?bout h??f ?? ???? ?s ? ??ng?e c?l?.'
    print(cryptogram(puzzle, solution))
    pr_new()

    puzzle = "V atult'a amrdd qvl zr nrbrqbrn zx v wumvl v medr vivx."
    solution = "? ????k's ???l? ??n ?? ??t???ed ?y a hum?? ? ?i?? ?w??."
    print(cryptogram(puzzle, solution))


if __name__ == '__main__':
    main()
