"""
Opdracht 23 - Nobelprijzen

https://dodona.ugent.be/nl/exercises/1392321201/
"""
import csv


def pr_new() -> str:
    print()
    print("---------------------------------")
    print()


def prizes(file, **kwargs):
    # kwargs voor het ophalen van de waarde
    kw_prize = kwargs.pop('prize', '')
    kw_discipline = kwargs.pop('discipline', '')
    kw_year = kwargs.pop('year', '')
    kw_nationality = kwargs.pop('nationality', '')
    kw_laureates = kwargs.pop('laureates', '')
    kw_motivation = kwargs.pop('motivation', '')

    # nieuwe lijst met prijzen aanmaken
    prizes_total = []
    # source file van de csv openen
    source_file = open(file, "r", encoding="utf=-8")
    # uitlezen van de source file met behulp van import csv
    read_csv = csv.reader(source_file, delimiter=';')

    # loopen door de csv
    for index, row in enumerate(read_csv):
        # als index groter is dan 0
        if index > 0:
            # de waardes in een tuple opslaan
            prize, discipline, year, laureates, motivation = tuple(row)
            # rij toevoegen met juiste arguments
            prizes_total.append(dict(zip(['prize', 'discipline', 'year', 'laureates', 'motivation'],
                                         [str(prize), str(discipline), int(year), list(str(laureates).split(', ')),
                                          str(motivation)])))

    # als prize argument gevuld is
    if kw_prize:
        # waarde toevoegen aan de lijst
        prizes_total = kw_prize_func(kw_prize, prizes_total)

    # als discipline argument gevuld is
    if kw_discipline:
        # waarde toevoegen aan de lijst
        prizes_total = kw_discipline_func(kw_discipline, prizes_total)

    # als year argument gevuld is
    if kw_year:
        # waarde toevoegen aan de lijst
        prizes_total = kw_year_func(kw_year, prizes_total)

    # als nationality argument gevuld is
    if kw_nationality:
        # waarde toevoegen aan de lijst
        prizes_total = kw_nationality_func(kw_nationality, prizes_total)

    # als laurareeats argument gevuld is
    if kw_laureates:
        # waarde toevoegen aan de lijst
        prizes_total = kw_laureates_func(kw_laureates, prizes_total)

    # als motivation argument gevuld is
    if kw_motivation:
        # waarde toevoegen aan de lijst
        prizes_total = kw_motivation_func(kw_motivation, prizes_total)

    # teruggeven van de correcte output
    return print_correct_output(prizes_total)


def kw_prize_func(prize, awards_csv):
    # prijs omzetten naar lower
    new_prize = prize.lower()
    # nieuwe awards lijst
    awards = []

    # loopen door de awards csv voor de juiste prijs
    for award in awards_csv:
        # als de opgegeven argument gelijk is aan de prijs rij in de csv
        if new_prize == award['prize'].lower().replace(" ", ""):
            # voeg hem dan toe
            awards.append(award)

    # teruggeven awards
    return awards


def kw_discipline_func(discipline, awards_csv):
    # discipline omzetten naar lower
    new_discipline = discipline.lower().replace(" ", "")
    # nieuwe awards lijst
    awards = []

    # loopen door de awards csv voor de juiste discipline
    for award in awards_csv:
        # als de opgegeven argument gelijk is aan de discipline rij in de csv
        if new_discipline.lower() == award['discipline'].lower().replace(" ", ""):
            # voeg hem dan toe
            awards.append(award)

    # teruggeven awards
    return awards


def kw_nationality_func(nationality, awards_csv):
    # nieuwe awards lijst
    awards = []

    # loopen door de awards csv voor de juiste nationality
    for award in awards_csv:
        # laureates op 0 zetten
        laureates = 0

        # loopen door de laureates
        for laureate in award['laureates']:
            # controleer de nationality
            if "({})".format(nationality.lower()) in laureate.lower():
                # optellen
                laureates += 1

        # als die groter of gelijk is aan 1
        if laureates >= 1:
            # voeg hem dan toe
            awards.append(award)

    # teruggeven awards
    return awards


def kw_year_func(year, awards_csv):
    # nieuwe awards lijst
    awards = []
    # loopen door de awards csv voor de juiste year
    for award in awards_csv:
        # als de opgegeven argument gelijk is aan de year rij in de csv
        if year == int(award['year']):
            # voeg hem dan toe
            awards.append(award)
    # teruggeven awards
    return awards


def kw_laureates_func(laureates, awards_csv):
    # nieuwe awards lijst
    awards = []
    # loopen door de awards csv voor de juiste laureates
    for award in awards_csv:
        # als de opgegeven argument gelijk is aan de laureates rij in de csv
        if len(award['laureates']) == laureates:
            # voeg hem dan toe
            awards.append(award)
    # teruggeven awards
    return awards


def kw_motivation_func(motivation, awards_csv):
    # nieuwe awards lijst
    awards = []
    # loopen door de awards csv voor de juiste motivation
    for award in awards_csv:
        # als de opgegeven argument gelijk is aan de motivation rij in de csv
        if motivation.lower() in award['motivation'].lower():
            # voeg hem dan toe
            awards.append(award)
    # teruggeven awards
    return awards


def print_correct_output(awards):
    # loopen door de opgegeven awards
    for award in awards:
        # format voor de rui die je terug krijgt
        print(award['prize'], ' in ', award['discipline'].capitalize(), '(', award['year'], '): ',
              ', '.join(award['laureates']), sep='')


def main():
    # lekker printen enzo
    prizes('prizes.csv', prize='nobelprize', year=1994)
    pr_new()
    prizes('prizes.csv', prize='nobelprize', discipline='mathematics')
    pr_new()
    prizes('prizes.csv', nationality='bel')
    pr_new()
    prizes('prizes.csv', discipline='chemistry', laureates=3)
    pr_new()
    prizes('prizes.csv', motivation='röntgen', discipline='physics', nationality='GB')
    pr_new()


if __name__ == '__main__':
    main()
