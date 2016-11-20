"""
Opdracht 1 - Tijdmeting op Mars

https://dodona.ugent.be/nl/exercises/1813154454/
"""

# input voor het aantal dagen
input_days = int(input('Voer hier het aantal dagen in: '))


# functie voor het converteren van tijd naar decimaal
def convert_time_to_float(time):
    default_time = time
    (h, m, s) = default_time.split(':')
    result_time = int(h) * 3600 + int(m) * 60 + float(s)
    return result_time


# functie voor het converteren van seconden naar dagen uren en minuten
def convert_seconds(seconds):
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    print(input_days, 'sol =', days, 'dagen,', hours, 'uren,', minutes, 'minuten en', seconds, 'seconden')


# converteren van 24uurs notatie naar seconden
sol_time_decimal = convert_time_to_float("24:39:35.244")
sol_time_multiply = int(input_days * sol_time_decimal)

# printen van seconden naar dagen uren minuten en seconden
print(convert_seconds(sol_time_multiply))
