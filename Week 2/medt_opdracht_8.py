"""
Opdracht 8 - Pythagorese drietallen

https://dodona.ugent.be/nl/exercises/683768040/
"""

import math


def main():
    # invoeren getal
    n = int(input("Voer een getal in: "))

    # loopje voor a
    # for a = 1 to a = n-2
    for a in range(1, (n - 2) + 1):

        # loopje voor b
        # for b = 1 to b = n - a - 1
        for b in range(1, (n - a) + 1):

            # loopje voor c
            # for c = 1 to c = n - a - b
            for c in range(1, (n - a - b) + 1):

                # voor elke (a,b,c) --> check de voorwaarde
                # if (a <= b) and (a + b + c = n) and (a ^ 2 + b ^ 2 = c ^ 2)
                if a + b + c == n and a <= b and (math.hypot(a, b) == c):

                    # print(a,b,c)
                    print("(%i, %i, %i)" % (a, b, c))


if __name__ == '__main__':
    main()
