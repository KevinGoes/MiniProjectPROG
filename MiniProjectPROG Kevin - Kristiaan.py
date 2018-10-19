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
            omgezet = terugomzettenASCII(regel['pq^ifkd'])
            stallingBezet.append(omgezet)
        return aantalRegels, stallingBezet


def infoPersoonlijk(invoerStalling, invoerWachtwoord):
    aantalRegels, stallingBezet = infoPubliek()
    while True:
        if invoerStalling in stallingBezet:
            while True:
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
                        return 'fout wachtwoord'
        else:
            return 'fout stalling'


def ophalenGegevens():
    with open('stalling.csv', 'r', newline='') as myCSVFile:
        reader = csv.DictReader(myCSVFile, delimiter=',')
        stalling = []
        registratienummer = []
        wachtwoorden = []
        datum = []
        for row in reader:
            omgezet = terugomzettenASCII(row['pq^ifkd'])
            stalling.append(omgezet)
            omgezet = terugomzettenASCII(row['t^`eqtlloa'])
            wachtwoorden.append(omgezet)
            omgezet = terugomzettenASCII(row['a^qrj'])
            datum.append(omgezet)
            omgezet = terugomzettenASCII(row['uhjlvwudwlhqxpphu'])
            registratienummer.append(omgezet)
        return stalling, wachtwoorden, datum, registratienummer

def ophalen():
    stalling, wachtwoorden, datum, registratienummers = ophalenGegevens()
    del registratienummers[indexRegistratienummer]
    del wachtwoorden[indexRegistratienummer]
    return stalling, wachtwoorden, datum, registratienummers


def gegevensTerugzetten():
    stalling, wachtwoorden, datum, registratienummers = ophalen()
    stallingNieuw = []
    wachtwoordenNieuw = []
    datumNieuw = []
    registratienummerNieuw = []
    for regel in stalling:
        omgezet = omzettenASCII(regel)
        stallingNieuw.append(omgezet)
    for regel in wachtwoorden:
        omgezet = omzettenASCII(regel)
        wachtwoordenNieuw.append(omgezet)
    for regel in datum:
        omgezet = omzettenASCII(regel)
        datumNieuw.append(omgezet)
    for regel in registratienummers:
        omgezet = omzettenASCII(regel)
        registratienummerNieuw.append(omgezet)
    combined = [stallingNieuw, wachtwoordenNieuw, datumNieuw, registratienummerNieuw]
    with open('stalling.csv', 'w', newline='') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter=',')
        writer.writerow(['pq^ifkd', 't^`eqtlloa', 'a^qrj', 'uhjlvwudwlhqxpphu'])
        for i in zip(*combined):
            writer.writerow(i)


print('1: Informatie')
print('2: Fiets ophalen')
invoerOptie = input('Optie: ')
if invoerOptie == '1':
    print('\n1: Publieke informatie')
    print('2: Persoonlijke informatie')
    invoerOptie = input('Optie: ')
    if invoerOptie == '1':
        vrij, stalling = infoPubliek()
        if vrij == 1:
            print('Er is nog {} stalling vrij, stalling {} is bezet'.format(vrij, stalling))
        else:
            print('Er zijn nog {} stallingen vrij, stallingen {} zijn bezet'.format(vrij, stalling))
    elif invoerOptie == '2':
        while True:
            while True:
                try:
                    invoerStalling = int(input('Welke stalling heeft u? '))
                    invoerStalling = str(invoerStalling)
                    break
                except ValueError:
                    print('Voer een geldig stallingsnummer in!')
            invoerWachtwoord = input('Welk wachtwoord heeft u voor stalling {}? '.format(invoerStalling))
            if infoPersoonlijk(invoerStalling, invoerWachtwoord) == 'fout wachtwoord':
                print('Fout wachtwoord, probeer nogmaals!')
            elif infoPersoonlijk(invoerStalling, invoerWachtwoord) == 'fout stalling':
                print('Stalling niet in gebruik, probeer nogmaals!')
            else:
                print('U heeft toegang tot uw stalling!')
                break

elif invoerOptie == '2':
    stalling, wachtwoorden, datum, registratienummer = ophalenGegevens()
    while True:
        invoerRegistratienummer = input("Geef alstublieft uw registratienummer: ")
        if invoerRegistratienummer in registratienummer:
            while True:
                indexRegistratienummer = registratienummer.index(invoerRegistratienummer)
                invoerWachtwoord = input("Geef alstublief uw wachtwoord: ")
                if invoerWachtwoord in wachtwoorden[indexRegistratienummer]:
                    gegevensTerugzetten()
                    break
            break
else:
    print('Geen optie')