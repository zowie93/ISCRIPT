"""
Opdracht 24 - Bestanden kopieren

https://dodona.ugent.be/nl/exercises/1985652400/
"""


def copycat(source, destination):
    # source file openen met leesrechten
    source_file = open(source, "r")
    # outputfile wegschrijven met schrijfrechten
    output_file = open(destination, "w+")

    # loopen door het aantal lijnen van de source file
    for lines in source_file:
        # de lijnen wegschrijven in destination
        output_file.write(lines)
    # sluiten van de connectie met de file
    source_file.close()

    # flushe van de output file
    output_file.flush()
    # sluiten van de connectie met de file
    output_file.close()


def main():
    copycat("medt_opdracht_24_source.txt", "medt_opdracht_24_output.txt")


if __name__ == '__main__':
    main()
