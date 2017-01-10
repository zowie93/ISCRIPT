"""
Opdracht 21 - Forsyth-Edwards notatie

https://dodona.ugent.be/nl/exercises/867899652/
"""


# printen van space tussen prints
def pr_new() -> str:
    print()
    print("---------------------------------")
    print()


def fen2grid(fen, spacer='*'):
    # splitten op de slash
    rows = fen.split('/')
    # enumerate de rijen
    rows_enum = enumerate(rows)
    # speciale teken opslaan
    space_char = str(spacer)
    # nieuwe grid zetten
    grid = ""

    # loopen door elke rij
    for row_numb, row in rows_enum:
        # character opslaan in een list zodat we erdoorheen kunnen loopen
        chars = list(row)
        # loopen door het aantal karakters
        for char in chars:
            # kijken of de karakter een letter is
            if char.isalpha():
                # voeg karakter toe aan eht grid
                grid += char
            # anders
            else:
                # loopen door de posities
                for position in range(0, int(char)):
                    # check als het leeg is
                    if not space_char:
                        # voeg standaard speciale charater toe
                        grid += "*"
                    # anders
                    else:
                        # voeg het speciale tegen toe
                        grid += space_char
        # check als het niet de laatste rij is
        if row_numb is not (len(rows) - 1):
            # newline toevoegen aan grid
            grid += "\n"
    # teruggeven van grid
    return grid


def grid2fen(grid, spacer='*'):
    # newline replacen met slash
    rows = grid.replace('\n', '/')
    # rijen splitten op de slash
    splitted_rows = rows.split('/')
    # enumerate aantal rijen
    rows_enum = enumerate(splitted_rows)
    # new grid maken
    new_grid = ""

    # loopen door elke rij
    for row_numb, row in rows_enum:
        # character opslaan in een list zodat we erdoorheen kunnen loopen
        chars = list(row)
        # enumerate aantal chars
        enum_chars = enumerate(chars)
        # lege plek op 0 zetten
        empty = 0
        # loopen door het aantal karakters
        for char_numb, char in enum_chars:
            # kijk of het karakter niet gelijk is aan de vooraf ingevuld char
            if char is not spacer:
                # kijken of empty niet null is
                if empty is not 0:
                    # aantel lege plekken toevoegen
                    new_grid += str(empty)
                    # weer op null zetten
                    empty = 0
                # char appenden aan grid
                new_grid += char
            # anders
            else:
                # aantal lege plekken + 1
                empty += 1
                # check of de lege plekken een vooledige rij zijn
                if (char_numb + 1) is len(row) and empty is not 0:
                    # aantal plekken toevoegen
                    new_grid += str(empty)
                    # op null zetten
                    empty = 0
        # check als het niet de laatste rij is
        if row_numb is not (len(rows) - 1):
            # newline toevoegen aan grid
            new_grid += "\n"
    # replacen van newlines en spaces
    clear_grid = new_grid.replace('\n', '/').replace(" ", "")
    # return van nieuwe grid zonder laatste slash
    return clear_grid[:-1]


def main():
    print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'))
    pr_new()
    print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '.'))
    pr_new()
    print(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+'))
    pr_new()
    grid = """rnbqkbnr
              pppppppp
              ********
              ********
              ********
              ********
              PPPPPPPP
              RNBQKBNR"""
    pr_new()
    print(grid2fen(grid))
    pr_new()
    print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')))
    pr_new()
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '.'), '.'))
    pr_new()
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', '+'), '+'))


if __name__ == '__main__':
    main()
