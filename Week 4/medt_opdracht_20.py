"""
Opdracht 20 - Zomertijd

https://dodona.ugent.be/nl/exercises/116986379/
"""
from datetime import date, timedelta


# zomertijd methode
def summertime(year):
    # teruggeven van de laatste zondag
    return return_sunday(year, 3, 31)


# wintertijd methode
def wintertime(year):
    # teruggeven van de laatste zondag
    return return_sunday(year, 11, 1)


# laatste zondag van de maand methode
def return_sunday(year, month, day):
    # nieuwe datum methode
    last_sunday = set_date(year, month, day)
    # als de datum nog niet gelijk is aan zondag
    while last_sunday.isoweekday() is not 7:
        # haal er dagen af totdat het zondag is
        last_sunday -= timedelta(1)
    # teruggeven van de datum (laatste zondag)
    return last_sunday


# omschrijven van datum methode
def set_date(year, month, day):
    # teruggeven nieuwe datum
    return date(year, month, day)


# klok methode
def clock(date_obj):
    # splitten van de opgegeven callback
    day = int(date_obj[0:2])
    month = int(date_obj[3:5])
    year = int(date_obj[6:10])

    # nieuwe datum samenstellen aan de hand van de ingegeven parameters
    final_date = set_date(year, month, day)

    # zomer datum
    summer_date = summertime(int(year))
    # winter datum
    winter_date = wintertime(int(year))

    # checks voor zomertijd
    if winter_date > final_date > summer_date:
        return "zomertijd"
    # checks voor wintertijd
    elif winter_date < final_date > summer_date:
        return "wintertijd"
    # check als de datum gelijk is aan de huidige zomertijd datum
    elif final_date == summer_date:
        return "omschakeling van wintertijd naar zomertijd"
    # check als de datum gelijk is aan de huidige wintertijd datum
    elif final_date == winter_date:
        return "omschakeling van zomertijd naar wintertijd"


def main():
    # printen van zomertijd
    print(summertime(2013))
    print(summertime(2014))
    print(summertime(2015))

    # lege string
    print(" ")

    # printen van wintertime
    print(wintertime(2013))
    print(wintertime(2014))
    print(wintertime(2015))

    # lege string
    print(" ")

    # printen van klok methode
    print(clock('27/06/2013'))
    print(clock('27/11/2013'))
    print(clock('31/03/2013'))
    print(clock('27/10/2013'))


if __name__ == '__main__':
    main()
