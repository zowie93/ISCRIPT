"""
Opdracht 11 - Sterke wachtwoorden

https://dodona.ugent.be/nl/exercises/417422714/
"""


def input_passwords_count():
    return int(input("Aantal wachtwoorden: "))


def give_input_password():
    return input("Wachtwoord: ")


def input_passwords(count):
    passwords = []

    for i in range(0, count):
        password = give_input_password()
        passwords.append(password)

    return passwords


def check_password_length(password):
    if len(password) >= 8:
        return True
    else:
        return False


def check_password_capital(password):
    for character in password:
        if character.isupper():
            return True
        else:
            continue
    return False


def check_password_lower(password):
    for character in password:
        if character.islower():
            return True
        else:
            continue
    return False


def check_password_digit(password):
    for character in password:
        if character.isdigit():
            return True
        else:
            continue
    return False


def check_password_specialchar(password):
    if set('[~!@#$%^&*()_+{}":;\']+$').intersection(password):
        return True
    else:
        return False


def check_strength(passwords):
    for password in passwords:
        strength = 0
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

        print(password_strength(strength))


def password_strength(strength):
    if strength < 3:
        return "Zwak"
    elif strength < 5:
        return "Matig"
    else:
        return "Sterk"


def main():
    count = input_passwords_count()
    passwords = input_passwords(count)
    check_strength(passwords)


if __name__ == '__main__':
    main()
