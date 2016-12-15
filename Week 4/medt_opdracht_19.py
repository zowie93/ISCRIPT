"""
Opdracht 19 - Zoemzinnen

https://dodona.ugent.be/nl/exercises/1620493816/
"""

# random importeren voor de functie random choice
import random


# loop voor random woorden
def random_loop(words):
    # teller op 0 zetten
    i = 0
    # zin leeg maken met een enkele quote
    zoem_zin = "'"

    # wanneer de lengte van de woorderen groter is dan 0
    while len(words) > i:
        # pikt een random woord van 1 van de meegegeven argumenten
        rand_woord = random.choice(words[i])
        # vult de zin aan met een random woord en een spatie
        zoem_zin += rand_woord + " "
        # telt er 1 bij op
        i += 1

    # teruggeven van de zin min de extra spatie en een quote aan het einde
    return zoem_zin[:-1] + "'"


# methode voor zoemzin1
def zoemzin1(words):
    # teruggeven van de random woorden
    return random_loop(words)


# methode voor zoemzin1
def zoemzin2(*words):
    # als er 3 argumenten meegeven zijn moet die ook 3 woorden teruggeven
    if len(words) == 3:
        # teruggeven van de random woorden
        return random_loop(words)
    # als er 4 argumenten meegeven zijn moet die ook 3 woorden teruggeven
    elif len(words) == 4:
        # teruggeven van de random woorden
        return random_loop(words)


# main methode
def main():
    # buzz 1
    buzz1 = ('integrated', 'total', 'systematized', 'parallel', 'functional', 'responsive', 'optional', 'synchronized',
             'compatible', 'balanced')
    # buzz 2
    buzz2 = ('management', 'organizational', 'monitored', 'reciprocal', 'digital', 'logistical', 'transitional',
             'incremental', 'third-generation', 'policy')
    # buzz3
    buzz3 = ('options', 'flexibility', 'capability', 'mobility', 'programming', 'concept', 'time-phase', 'projection',
             'hardware', 'contingency')

    # shakespeare 1
    shakespeare1 = ['Thou']
    # shakespeare 2
    shakespeare2 = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered', 'clouted', 'craven',
                    'currish', 'dankish', 'dissembling', 'droning', 'errant', 'fawning', 'fobbing', 'froward',
                    'frothy', 'gleeking', 'goatish', 'gorbellied', 'impertinent', 'infectious', 'jarring',
                    'loggerheaded', 'lumpish', 'mammering', 'mangled', 'mewling', 'paunchy', 'pribbling', 'puking',
                    'puny', 'quailing', 'rank', 'reeky', 'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy',
                    'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous', 'warped', 'wayward',
                    'weedy', 'yeasty']
    # shakespeare 3
    shakespeare3 = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained', 'clapper-clawed',
                    'clay-brained', 'common-kissing', 'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted',
                    'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed',
                    'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged', 'guts-griping', 'half-faced',
                    'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured',
                    'knotty-pated', 'milk-livered', 'motley-minded', 'onion-eyed', 'plume-plucked', 'pottle-deep',
                    'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed', 'shard-borne',
                    'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited', 'tickle-brained',
                    'toad-spotted', 'urchin-snouted', 'weather-bitten']
    # shakespeare 4
    shakespeare4 = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', 'bum-bailey',
                    'canker-blossom', 'clack-dish', 'clotpole', 'coxcomb', 'codpiece', 'death-token', 'dewberry',
                    'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian', 'giglet', 'gudgeon',
                    'haggard', 'harpy', 'hedge-pig', 'horn-beast', 'hugger-mugger', 'jolthead', 'lewdster', 'lout',
                    'maggot-pie', 'malt-worm', 'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp',
                    'mumble-news', 'nut-hook', 'pigeon-egg', 'pignut', 'puttock', 'pumpion', 'ratsbane', 'scut',
                    'skainsmate', 'strumpet', 'varlet', 'vassal', 'whey-face', 'wagtail']

    # printen van zoemzin 1 met buzz1, buzz2, buzz3
    print(zoemzin1((buzz1, buzz2, buzz3)))
    # printen van zoemzin 2 met buzz1, buzz2, buzz3
    print(zoemzin2(buzz1, buzz2, buzz3))

    # printen van zoemzin 1 met shakespeare1, shakespeare2, shakespeare3, shakespeare4
    print(zoemzin1([shakespeare1, shakespeare2, shakespeare3, shakespeare4]))
    # printen van zoemzin 2 met shakespeare1, shakespeare2, shakespeare3, shakespeare4
    print(zoemzin2(shakespeare1, shakespeare2, shakespeare3, shakespeare4))


if __name__ == '__main__':
    main()
