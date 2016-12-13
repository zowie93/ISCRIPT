"""
Opdracht 15 - Vigenecodering

https://dodona.ugent.be/nl/exercises/862295437/
"""

# alfabet uitschrijven
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# lengte van tekst teruggeven
def lengte_tekst(tekst):
    return len(tekst)


# lengte van de sleutel teruggeven
def lengte_sleutel(sleutel):
    return len(sleutel)


# coderen van de tekst dmv tekst en sleutel
def codeer(tekst, sleutel):
    # lengte tekst
    tekst_lengte = lengte_tekst(tekst)
    # lengte sleutel
    sleutel_lengte = lengte_sleutel(sleutel)

    # teruggeven van gecompilde tekst
    return compile_tekst(tekst, sleutel, tekst_lengte, sleutel_lengte, True)


# coderen van de tekst dmv tekst en sleutel
def decodeer(code_tekst, sleutel):
    # lengte tekst
    tekst_lengte = lengte_tekst(code_tekst)
    # lengte sleutel
    sleutel_lengte = lengte_sleutel(sleutel)

    # teruggeven van gecompilde tekst
    return compile_tekst(code_tekst, sleutel, tekst_lengte, sleutel_lengte, False)


# tekst compilen / decompilen dmv tekst, sleutel, lengte tekst, lengte sleutel
def compile_tekst(tekst, sleutel, t_length, s_length, special_char):
    # var i op 0 zetten
    i = 0
    # codetekst voor return leeg maken
    code_tekst = ""

    # zolang i kleiner is dan lengte tekst blijf doorgaan
    while i < t_length:
        # elke char uitkerven
        tekst_char = tekst[i]
        # elke sleutel char
        sleutel_char = sleutel[i % s_length]
        # als de char in het alfabet voorkomt
        if tekst_char in alfabet:
            # special char als in - en + voor compile en decompile tekst
            if special_char:
                # beide chars koppelen tot 1
                totaal = (alfabet.index(tekst_char) + alfabet.index(sleutel_char))
            else:
                # beide chars koppelen tot 1
                totaal = (alfabet.index(tekst_char) - alfabet.index(sleutel_char))
            # alle chars weer totaal 1 geheel vormen
            c = alfabet[totaal % 26]
            # appenden aan code_tekst
            code_tekst += c
        # als er een ! inzit blijft het een !
        elif tekst_char == "!":
            # toevoegen aan codeteskt !
            code_tekst += "!"
        # spaties blijven spaties
        elif tekst_char == " ":
            # spateie toevoegen aan code_tekst
            code_tekst += " "
        # teller + 1
        i += 1
    # teruggeven code tekst
    return code_tekst


def main():
    # zin 1
    print(codeer('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS'))
    # zin 2
    print(decodeer('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS'))
    # zin 3
    print(codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR'))
    # zin 4
    print(decodeer('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR'))


if __name__ == '__main__':
    main()
