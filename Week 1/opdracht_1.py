"""
Opdracht 1 - Tijdmeting op Mars

https://dodona.ugent.be/nl/exercises/1813154454/
"""

# input voor het aantal dagen
input_days = int(input('Voer hier het aantal dagen in: '))


# functie voor het converteren van tijd naar decimaal
def convert_time_to_float(time):
    # splitten van de ingevoerde tijdsbestek
    (h, m, s) = time.split(':')
    # omzetten naar seconden
    result_time = int(h) * 3600 + int(m) * 60 + float(s)
    # return van het totaal aantal seconden
    return result_time


# functie voor het converteren van seconden naar dagen uren en minuten
def convert_seconds(seconds):
    # dagen, uren, minuten en seconden omzetten van totaal aantaal seconden
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)

    # uitprinten van dagen, uren, minuten en seconden
    print(input_days, 'sol =', int(days), 'dagen,', int(hours), 'uren,', int(minutes), 'minuten en', int(seconds),
          'seconden')


# main methode
def main():
    # converteren van 24uurs notatie naar seconden
    sol_time_decimal = convert_time_to_float("24:39:35.244")
    sol_time_multiply = float(input_days * sol_time_decimal)

    # printen van seconden naar dagen uren minuten en seconden
    convert_seconds(sol_time_multiply)


# runtime methode
if __name__ == '__main__':
    main()
