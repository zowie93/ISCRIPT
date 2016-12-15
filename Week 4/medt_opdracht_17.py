"""
Opdracht 17 - 3 + 1 gratis

https://dodona.ugent.be/nl/exercises/751779411/
"""


# methode voor prijzen totaal
def samen(prijzen):
    # lijst met prijzen van type float en gesorteerd
    prijzen_list = sorted(prijzen, reverse=True, key=float)

    # waardes op 0 zetten
    prijs_totaal = 0
    prijs_korting = 0

    # uitrekenen hoeveel lijsten van 4 producten erin kunnen
    laagste_prijzen = round(len(prijzen_list) / 4)
    # aantal gratis producten
    gratis_producten = prijzen_list[-laagste_prijzen:]

    # korting berekenen
    for x in gratis_producten:
        prijs_korting += x

    # totale prijs berekenen
    for i in prijzen_list:
        prijs_totaal += i

    # teruggeven van totaleprijs - korting
    return prijs_totaal - prijs_korting


# groeperen van prijzen
def groeperen(prijzen):
    # lijst met prijzen van type float en gesorteerd
    prijzen_list = sorted(prijzen, reverse=True, key=float)
    # nieuwe array maken voor aankomende tuples
    tuple_groep = []

    # loop die per 4 producten een nieuwe tuple maakt
    for x in range(0, len(prijzen_list), 4):
        tuple_groep.append(tuple(prijzen_list[x:x + 4]))

    # teruggeven van tupples
    return tuple_groep


def gegroepeerd(prijzen):
    # prijzen ophalen
    prijzen_groep = groeperen(prijzen)

    # totale prijs op 0 zetten
    prijs_totaal = 0

    # loopen door de prijzen groep
    for x in prijzen_groep:
        # als het aantal producten 4 is
        if len(x) is 4:
            # tel de eerste 3 op
            prijs_totaal += sum(x[:3])
        # anders
        else:
            # tel alle restanten op
            prijs_totaal += sum(x)

    # teruggeven van totale prijs
    return prijs_totaal


# methode voor winst
def winst(prijzen):
    # winst uitrekenen door samen en gegroepeerd van elkaar af te halen
    winst = samen(prijzen) - gegroepeerd(prijzen)
    # teruggeven van winst met 1 getal achter de komaa
    return '{0:.1f}'.format(winst)


def main():
    # prijs lijst
    prijzen_lijst = [3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23]
    # printen van prijzen samen
    print(samen(prijzen_lijst))
    # printen van groep met tupples
    print(groeperen(prijzen_lijst))
    # printen van gegroepeerde prijs
    print(gegroepeerd(prijzen_lijst))
    # printen van winst
    print(winst(prijzen_lijst))


if __name__ == '__main__':
    main()
