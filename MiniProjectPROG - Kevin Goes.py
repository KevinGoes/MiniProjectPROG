import csv


def omzettenASCII(omzetWaarde):
    lijst = list(omzetWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) - 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin


def terugomzettenASCII(omgezetteWaarde):
    lijst = list(omgezetteWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) + 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin


def infoPubliek():
    with open('stalling.csv', 'r', newline='') as myCSVFile:
        lezer = csv.DictReader(myCSVFile, delimiter=',')
        aantalRegels = 0
        stallingBezet = []
        for regel in lezer:
            aantalRegels += 1
            omgezet = terugomzettenASCII(regel['pq^iifkd'])
            stallingBezet.append(omgezet)
        return aantalRegels, stallingBezet


def infoPersoonlijk():
    aantalRegels, stallingBezet = infoPubliek()
    while True:
        invoerStalling = input('Welke stalling heeft u? ')
        if invoerStalling in stallingBezet:
            while True:
                invoerWachtwoord = input('Welk wachtwoord heeft u voor stalling {}? '.format(invoerStalling))
                with open('stalling.csv', 'r', newline='') as myCSVFile:
                    aantalRegels = 0
                    wachtwoord = []
                    lezer = csv.DictReader(myCSVFile, delimiter=',')
                    for regel in lezer:
                        aantalRegels += 1
                        omgezet = terugomzettenASCII(regel['t^`eqtlloa'])
                        wachtwoord.append(omgezet)
                    regel = stallingBezet.index(invoerStalling)
                    if wachtwoord[regel] == invoerWachtwoord:
                        return 'U heeft toegang tot uw stalling!'
                    else:
                        print('Verkeerd wachtwoord voor stalling {}, probeer het nogmaals \n'.format(invoerStalling))
        else:
            print('Stalling {} is niet in bezet, probeer het nogmaals \n'.format(invoerStalling))


vrij, stalling = infoPubliek()
print('Er zijn nog {} stallingen vrij, {} stallingen zijn bezet'.format(vrij, stalling))
print(infoPersoonlijk())