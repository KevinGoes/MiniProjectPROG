from tkinter import *
import csv
import tkinter as tk
from tkinter import font  as tkfont

def toonHome():
    RegistrerenFrame.pack_forget()
    StallenFrame.pack_forget()
    OphalenFrame.pack_forget()
    InformatieFrame.pack_forget()
    homeFrame.pack()

def toonRegistreren():
    homeFrame.pack_forget()
    StallenFrame.pack_forget()
    OphalenFrame.pack_forget()
    InformatieFrame.pack_forget()
    RegistrerenFrame.pack()

def toonStallen():
    RegistrerenFrame.pack_forget()
    homeFrame.pack_forget()
    OphalenFrame.pack_forget()
    InformatieFrame.pack_forget()
    StallenFrame.pack()

def toonOphalen():
    RegistrerenFrame.pack_forget()
    StallenFrame.pack_forget()
    homeFrame.pack_forget()
    InformatieFrame.pack_forget()
    OphalenFrame.pack()

def toonInformatie():
    RegistrerenFrame.pack_forget()
    StallenFrame.pack_forget()
    OphalenFrame.pack_forget()
    homeFrame.pack_forget()
    InformatieFrame.pack()

def toonInformatiePersoonlijk():
    InformatieFrame.pack_forget()
    InformatiePersoonlijk.pack()

def toonInformatiePubliek():
    InformatieFrame.pack_forget()
    InformatiePubliek.pack()

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
                        with open('registreren.csv', 'r', newline='') as myCSVFile:
                            return 'U kunt uw nu bij uw fiets'
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

def plekVrij(invoerRegistratienummer, invoerNieuwStallingNummer, wachtwoordStallingsplaats):
    with open('registreren.csv', 'r', newline='') as myCSVFile:
        lezer = csv.DictReader(myCSVFile, delimiter=',')
        lijst = []
        aantalRegels = 0
        for regel in lezer:
            aantalRegels += 1
            omgezet = terugomzettenASCII(regel['uhjlvwudwlhqxpphu'])
            lijst.append(omgezet)
        if invoerRegistratienummer in lijst:
                if invoerNieuwStallingNummer in infoPubliek():
                    return 'Kluisnietvrij'
                elif len(invoerNieuwStallingNummer) > 2:
                    return 'Stallingnummertehoog'
                elif ',' in wachtwoordStallingsplaats:
                    return 'KommaInWachtwoord'
                else:
                    wachtwoord = omzettenASCII(wachtwoordStallingsplaats)
                    vandaag = datetime.datetime.today()
                    s = vandaag.strftime("%d-%b-%Y, %I:%M:%S")
                    datum = omzettenASCII(s)
                    invoer = omzettenASCII(invoerNieuwStallingNummer)
                    invoerRegistratienummer = omzettenASCII(invoerRegistratienummer)
                    return invoer, wachtwoord, datum, invoerRegistratienummer
        else:
            return 'Registratienummernietgoed'

def stallen():
    with open('stalling.csv', 'a', newline='') as myCSVFile:
        schrijven = csv.writer(myCSVFile)
        schrijven.writerow(plekVrij(invoerRegistratienummer, invoerNieuwStallingNummer, wachtwoordStallingsplaats))

def registreren(invoerNaam, invoerANaam, invoerAGebDatum, invoerMerkFiets):
    Nummer = range(10 ** 8)
    RandomGetal = random.choice(Nummer)
    while True:
        fileOpen = open("registreren.csv", "r")
        fileOpen.readlines()
        if RandomGetal in fileOpen:
            Nummer = range(10 ** 8)
            RandomGetal = random.choice(Nummer)
        else:
            omgezetteGetal = omzettenASCII(str(RandomGetal))
            fileOpen.close()
            break
    voornaam = omzettenASCII(invoerNaam)
    achternaam = omzettenASCII(invoerANaam)
    geboortedatum = omzettenASCII(invoerAGebDatum)
    fietsenmerk = omzettenASCII(invoerMerkFiets)
    omgezetteGetal = omzettenASCII(str(RandomGetal))
    with open("registreren.csv", "a+") as MyCSVfile:
        MyCSVfile.write(voornaam)
        MyCSVfile.write("," + achternaam)
        MyCSVfile.write("," + geboortedatum)
        MyCSVfile.write("," + fietsenmerk)
        MyCSVfile.write("," + str(omgezetteGetal) + "\n")
    return RandomGetal


root = Tk()
root.title = ('home')
root.configure(background='yellow')
homeFrame = Frame(master=root, background='yellow')
homeFrame.pack(fill="both", expand=True)
homeLabel = Label(master=homeFrame, text='Welkom bij de NS', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
homeLabel.pack(padx=20, pady=20)
Registreren = Button(master=homeFrame, text='Registreren', height=10, width=45, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonRegistreren)
Registreren.place(x=150, y=150)
Stallen = Button(master=homeFrame, text='Stallen', height=10, width=45, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonStallen)
Stallen.place(x=775, y=150)
Ophalen = Button(master=homeFrame, text='Ophalen', height=10, width=45, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonOphalen)
Ophalen.place(x=150, y=450)
Informatie = Button(master=homeFrame, text='Informatie', height=10, width=45, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatie)
Informatie.place(x=775, y=450)

RegistrerenFrame = Frame(master=root, background='yellow')
RegistrerenFrame.pack(fill="both", expand=True)
RegistrerenLabel = Label(master=RegistrerenFrame, text='Registreren', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
RegistrerenLabel.pack(padx=20, pady=20)
RegistrerenButton = Button(master=RegistrerenFrame, text='Informatie', height=10, width=45, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatie)
RegistrerenButton.place(x=150, y=150)

StallenFrame = Frame(master=root, background='yellow')
StallenFrame.pack(fill="both", expand=True)
StallenLabel = Label(master=StallenFrame, text='Stallen', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
StallenLabel.pack(padx=20, pady=20)

OphalenFrame = Frame(master=root, background='yellow')
OphalenFrame.pack(fill="both", expand=True)
OphalenLabel = Label(master=OphalenFrame, text='Ophalen', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
OphalenLabel.pack(padx=20, pady=20)

InformatieFrame = Frame(master=root, background='yellow')
InformatieFrame.pack(fill="both", expand=True)
InformatieLabel = Label(master=InformatieFrame, text='Informatie', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
InformatieLabel.pack(padx=20, pady=20)

PubliekeInformatieButton = Button(master=InformatieFrame, text='Publieke Informatie', height=10, width=45, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatiePubliek)
PubliekeInformatieButton.pack(side=LEFT)
PersoonlijkeInformatieButton = Button(master=InformatieFrame, text='Persoonlijke Informatie', height=10, width=45, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatiePersoonlijk)
PersoonlijkeInformatieButton.pack(padx=1, pady=20)

InformatiePubliek = Frame(master=root, background='yellow')
InformatiePubliek.pack
aantalKluizenVrij, kluizenVrij = infoPubliek()
InformatiePubliekLabel = Label(master=InformatiePubliek, text='Er zijn in totaal {} kluizen vrij, kluizen {} zijn bezet'.format(aantalKluizenVrij, kluizenVrij), background='yellow', foreground='blue', width=100, height=10, font=('Helvetica', 15, 'bold'))
InformatiePubliekLabel.pack()
InformatiePersoonlijk = Frame(master=root, background='yellow')
InformatiePersoonlijk.pack

toonHome()
root.mainloop()



