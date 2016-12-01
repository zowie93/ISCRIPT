"""
Opdracht 11 - Sterke wachtwoorden

https://dodona.ugent.be/nl/exercises/417422714/
"""


# functie aantal wachtwoorden invullen
def input_passwords_count():
    return int(input("Aantal wachtwoorden: "))


# functie invoere nwachtwoorden
def give_input_password():
    return input("Wachtwoord: ")


# functie invoeren wachtwoorden
def input_passwords(count):
    # wachtwoorden opslaan in array
    passwords = []

    # loop voor controle aantal ingevulde wachtwoorden input types printen
    for i in range(0, count):
        # print vraagstelling
        password = give_input_password()
        # wachtwoord toevoegen aan de arraylist
        passwords.append(password)

    # terugggeven van de wachtwoorden
    return passwords


# check voor wachtwoord lengte
def check_password_length(password):
    # kijkt of het ingevoerde wachtwoord langer is dan 8 chars
    if len(password) >= 8:
        return True
    else:
        return False


# check voor wachtwoord met hoofdletter
def check_password_capital(password):
    for character in password:
        # kijkt of het wachtwoord een uppercase bevat
        if character.isupper():
            return True
        else:
            continue
    return False


# check voor password met lowercase
def check_password_lower(password):
    for character in password:
        # kijkt of het wachtwoord een char heeft met lowercase
        if character.islower():
            return True
        else:
            continue
    return False


# check voor cijfer in wachtwoord
def check_password_digit(password):
    for character in password:
        # kijkt of het wachtwoord een cijfer bevat
        if character.isdigit():
            return True
        else:
            continue
    return False


# check speciale characters
def check_password_specialchar(password):
    # kijkt of het wachtwoord een speciale char heeft
    if set('[~!@#$%^&*()_+{}":;\']+$').intersection(password):
        return True
    else:
        return False


# check voor sterkte wachtwoorden
def check_strength(passwords):
    for password in passwords:
        # sterkte begint bij nul
        strength = 0
        # if statements ter controle of de wachtwoorden aan de eisen voldoen, zoja dan sterkte toevoegen
        if check_password_length(password):
            strength += 1
        if check_password_capital(password):
            strength += 1
        if check_password_lower(password):
            strength += 1
        if check_password_digit(password):
            strength += 1
        if check_password_specialchar(password):
            strength += 1

        # uitprinten van sterkte wachtwoorden
        print(password_strength(strength))


# wachtwoord returns voor de sterkste
def password_strength(strength):
    if strength < 3:
        return "zwak"
    elif strength < 5:
        return "matig"
    else:
        return "sterk"


def main():
    # uitvoeren aantal wachtwoorden die je opwilt geven
    count = input_passwords_count()
    # wachtwoord veld print x count van wachtwoorden
    passwords = input_passwords(count)
    # sterkte wachtwoorden controleren
    check_strength(passwords)


if __name__ == '__main__':
    main()
