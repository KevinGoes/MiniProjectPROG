def ophalenGegevens():
    with open('stalling.csv', 'r', newline='') as myCSVFile:
        reader = csv.DictReader(myCSVFile, delimiter=',')
        registratienummer = []
        wachtwoorden = []
        for row in reader:
            omgezet = terugomzettenASCII(row['uhjlvwudwlhqxpphu'])
            wachtwoordOmgezet = terugomzettenASCII(row['t^`eqtlloa'])
            registratienummer.append(omgezet)
            wachtwoorden.append(wachtwoordOmgezet)
        return registratienummer, wachtwoorden

def ophalen():
    registratienummers, wachtwoorden = ophalenGegevens()
    invoerRegistratienummer = input("Geef alstublieft uw registratienummer: ")
    while True:
        if invoerRegistratienummer in registratienummers:
            while True:
                indexRegistratienummer = registratienummers.index(invoerRegistratienummer)
                invoerWachtwoord = input("Geef alstublief uw wachtwoord: ")
                if invoerWachtwoord in wachtwoorden[indexRegistratienummer]:
                    print("U kunt uw fiets nu ophalen! heb een prettige dag!")
                    del registratienummers[indexRegistratienummer]
                    del wachtwoorden[indexRegistratienummer]
                    return wachtwoorden, registratienummers
                else:
                    print("Dit wachtwoord hoord niet bij het registratienummer dat u heeft gegeven, probeer het opnieuw")
            return wachtwoorden, registratienummers
        else:
            print("Dit registratienummer is niet in gebruik, probeer het nog een keer!")
            invoerRegistratienummer = input("Geef alstublieft uw registratienummer: ")
        break

def gegevensTerugzetten():
    registratienummers, wachtwoorden = ophalen()
    combined = [registratienummers, wachtwoorden]
    with open('newfile.csv', 'w', newline='') as myCSVFile:
        write = csv.writer(myCSVFile, delimiter=',')
        for i in zip(*combined):
            write.writerow(i)

gegevensTerugzetten()