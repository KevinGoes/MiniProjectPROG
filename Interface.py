from tkinter import *
import csv
import datetime
import random
import tkinter as tk
from tkinter import font  as tkfont

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
        stallingBezet.sort()
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
                        return 'fout'
        else:
            return 'fout'


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

def ophalen(invoerRegistratienummer, invoerWachtwoord):
    stalling, wachtwoorden, datum, registratienummer = ophalenGegevens()
    if invoerRegistratienummer in registratienummer:
        indexRegistratienummer = registratienummer.index(invoerRegistratienummer)
        if invoerWachtwoord in wachtwoorden[indexRegistratienummer]:
            del registratienummer[indexRegistratienummer]
            del wachtwoorden[indexRegistratienummer]
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
            for regel in registratienummer:
                omgezet = omzettenASCII(regel)
                registratienummerNieuw.append(omgezet)
            combined = [stallingNieuw, wachtwoordenNieuw, datumNieuw, registratienummerNieuw]
            with open('stalling.csv', 'w', newline='') as myCSVFile:
                writer = csv.writer(myCSVFile, delimiter=',')
                writer.writerow(['pq^ifkd', 't^`eqtlloa', 'a^qrj', 'uhjlvwudwlhqxpphu'])
                for i in zip(*combined):
                    writer.writerow(i)
        else:
            return 'fout'
    else:
        return 'fout'


def plekVrij(invoerRegistratienummer, invoerNieuwStallingNummer, wachtwoordStallingsplaats):
    with open('registreren.csv', 'r', newline='') as myCSVFile:
        lezer = csv.DictReader(myCSVFile, delimiter=',')
        lijst = []
        aantalRegels = 0
        for regel in lezer:
            aantalRegels += 1
            omgezet = terugomzettenASCII(regel['obdfpqo^qfbkrjjbo'])
            lijst.append(omgezet)
        if invoerRegistratienummer in lijst:
                if invoerNieuwStallingNummer in infoPubliek():
                    return 'fout'
                elif len(invoerNieuwStallingNummer) > 2:
                    return 'fout'
                elif ',' in wachtwoordStallingsplaats:
                    return 'fout'
                else:
                    wachtwoord = omzettenASCII(wachtwoordStallingsplaats)
                    vandaag = datetime.datetime.today()
                    s = vandaag.strftime("%d-%b-%Y, %I:%M:%S")
                    datum = omzettenASCII(s)
                    invoer = omzettenASCII(invoerNieuwStallingNummer)
                    invoerRegistratienummer = omzettenASCII(invoerRegistratienummer)
                    return invoer, wachtwoord, datum, invoerRegistratienummer
        else:
            return 'fout'

def stallen():
    with open('stalling.csv', 'a', newline='') as myCSVFile:
        schrijven = csv.writer(myCSVFile)
        schrijven.writerow(plekVrij(invoerRegistratienummer.get(), invoerNieuwStallingNummer.get(), invoerStallenWachtwoord.get()))

def registreren(invoerNaam, invoerANaam, invoerGeboorteDatum, invoerFietsMerk):
    Nummer = range(10000000, 99999999)
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
    geboortedatum = omzettenASCII(invoerGeboorteDatum)
    fietsenmerk = omzettenASCII(invoerFietsMerk)
    omgezetteGetal = omzettenASCII(str(RandomGetal))
    with open("registreren.csv", "a+") as MyCSVfile:
        MyCSVfile.write(voornaam)
        MyCSVfile.write("," + achternaam)
        MyCSVfile.write("," + geboortedatum)
        MyCSVfile.write("," + fietsenmerk)
        MyCSVfile.write("," + str(omgezetteGetal) + "\n")
    return RandomGetal


def tijd():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%H")
    s = int(s)
    if s < 12:
        return('Goedemorgen')
    elif s >= 12 and s < 18:
        return('Goedemiddag')
    elif s > 18:
        return('Goedenavond')

def tijdKlok():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%H:%M:%S")
    return s

def datum():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d-%m-%Y")
    return s

def toonHome():
    RegistrerenFrame.pack_forget()
    StallenFrame.pack_forget()
    OphalenFrame.pack_forget()
    InformatieFrame.pack_forget()
    InformatiePersoonlijkFrame.pack_forget()
    InformatiePersoonlijkFoutFrame.pack_forget()
    StallenFoutFrame.pack_forget()
    StallenOutputFrame.pack_forget()
    OphalenFoutFrame.pack_forget()
    OphalenOutputFrame.pack_forget()
    OphalenFrame.pack_forget()
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
    InformatiePersoonlijkFrame.pack()

def toonInformatiePubliek():
    InformatieFrame.pack_forget()
    InformatiePubliekFrame.pack()

def toonInformatiePersoonlijkOutput():
    InformatiePersoonlijkFrame.pack_forget()
    InformatiePersoonlijkFoutFrame.pack_forget()
    if infoPersoonlijk(invoerStalling.get(), invoerWachtwoord.get()) == 'fout':
        InformatiePersoonlijkFoutFrame.pack()
    else:
        InformatiePersoonlijkOutputFrame.pack()

def toonStallenOutput():
    StallenFoutFrame.pack_forget()
    StallenFrame.pack_forget()
    if plekVrij(invoerRegistratienummer.get(), invoerNieuwStallingNummer.get(), invoerStallenWachtwoord.get()) == 'fout':
        StallenFoutFrame.pack()
    else:
        stallen()
        StallenOutputFrame.pack()

def toonRegistrerenOutput():
    x = registreren(invoerNaam.get(), invoerANaam.get(), invoerGeboorteDatum.get(), invoerFietsMerk.get())
    RegistrerenFrame.pack_forget()
    # RegistrerenOutput
    RegistrerenOutputFrame = Frame(master=root, background='yellow')
    RegistrerenOutputFrame.pack(fill="both", expand=True)
    RegistrerenOutputLabel = Label(master=RegistrerenOutputFrame, text='Registreren', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
    RegistrerenOutputLabel.pack(padx=20, pady=20)
    RegistrerenOutputLabel1 = Label(master=RegistrerenOutputFrame, text=x,  background='yellow', foreground='blue', width=50, height=3, font=('Helvetica', 25, 'bold'))
    RegistrerenOutputLabel1.pack(padx=20, pady=20)

def toonOphalenOutput():
    OphalenFrame.pack_forget()
    if ophalen(OphalenRegistratienummer.get(), OphalenWachtwoord.get()) == 'fout':
        OphalenFoutFrame.pack()
    else:
        OphalenOutputFrame.pack()


root = Tk()
root.title = ('home')
root.configure(background='yellow')
homeFrame = Frame(master=root, background='yellow')
homeFrame.pack(fill="both", expand=True)
vandaag = Label(master=root, text='Vandaag' + '\n' + datum() + '\n' + tijdKlok(), background='yellow', foreground='blue', width=80, height=5, font=('Helvetica', 14, 'bold'))
vandaag.place(x=970, y=700)
homeLabel = Label(master=homeFrame, text=tijd() +',\nWelkom bij NS', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 25, 'bold'))
homeLabel.pack(padx=20, pady=20)
Registreren = Button(master=homeFrame, text='Registreren', height=7, width=30, font=('Helvetica', 15, 'bold'),background='blue',foreground='white', command=toonRegistreren)
Registreren.place(x=390, y=250)
Stallen = Button(master=homeFrame, text='Stallen', height=7, width=30, font=('Helvetica', 15, 'bold'),background='blue',foreground='white', command=toonStallen)
Stallen.place(x=775, y=250)
Ophalen = Button(master=homeFrame, text='Ophalen', height=7, width=30, font=('Helvetica', 15, 'bold'),background='blue',foreground='white', command=toonOphalen)
Ophalen.place(x=390, y=450)
Informatie = Button(master=homeFrame, text='Informatie', height=7, width=30, font=('Helvetica', 15, 'bold'),background='blue',foreground='white', command=toonInformatie)
Informatie.place(x=775, y=450)


#Registreren
RegistrerenFrame = Frame(master=root, background='yellow')
RegistrerenFrame.pack(fill="both", expand=True)
RegistrerenLabel = Label(master=RegistrerenFrame, text='Registreren', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
RegistrerenLabel.pack(padx=20, pady=20)
invoerNaamLabel = Label(master=RegistrerenFrame, text='Voer hieronder uw naam in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
invoerNaamLabel.pack(padx=20, pady=10)
invoerNaam = Entry(master=RegistrerenFrame, background='blue')
invoerNaam.pack(padx=20, pady=30)
invoerANaamLabel = Label(master=RegistrerenFrame, text='Voer hieronder uw achternaam in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
invoerANaamLabel.pack(padx=20, pady=10)
invoerANaam = Entry(master=RegistrerenFrame, background='blue')
invoerANaam.pack(padx=20, pady=30)
invoerGeboorteDatumLabel = Label(master=RegistrerenFrame, text='Voer hieronder uw geboortedatum in! (dd-mm-jjjj)', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
invoerGeboorteDatumLabel.pack(padx=20, pady=10)
invoerGeboorteDatum = Entry(master=RegistrerenFrame, background='blue')
invoerGeboorteDatum.pack(padx=20, pady=30)
invoerFietsmerkLabel = Label(master=RegistrerenFrame, text='Voer hieronder het merk van uw fiets in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
invoerFietsmerkLabel.pack(padx=20, pady=10)
invoerFietsMerk = Entry(master=RegistrerenFrame, background='blue')
invoerFietsMerk.pack(padx=20, pady=10)
RegistrerenDoorgaan = Button(master=RegistrerenFrame, text='Doorgaan', height=3, width=14, font=('Helvetica', 10, 'bold'),background='blue',foreground='white', command=toonRegistrerenOutput)
RegistrerenDoorgaan.pack(padx=20, pady=30)
invoerFietsmerkLabel.pack()

#Stallen
StallenFrame = Frame(master=root, background='yellow')
StallenFrame.pack(fill="both", expand=True)
StallenLabel = Label(master=StallenFrame, text='Stallen', background='yellow', foreground='blue', width=50, height=3, font=('Helvetica', 25, 'bold'))
StallenLabel.pack(padx=20, pady=20)
StallingenVrij, StallingNummers = infoPubliek()
StallenLabelStallingenBezet = Label(master=StallenFrame, text='Stallingen {} zijn bezet!'.format(StallingNummers), background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
StallenLabelStallingenBezet.pack(padx=20, pady=20)
NieuwStallingNummerLabel = Label(master=StallenFrame, text='Voer hieronder uw toekomstige stallingnummer in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
NieuwStallingNummerLabel.pack()
invoerNieuwStallingNummer = Entry(master=StallenFrame, text='Voer hier uw stallingnummer in!', background='blue')
invoerNieuwStallingNummer.pack(padx=20, pady=20)
WachtwoordLabel = Label(master=StallenFrame, text='Voer hieronder een wachtwoord in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
WachtwoordLabel.pack()
invoerStallenWachtwoord = Entry(master=StallenFrame, text='Voer hieronder een wachtwoord in!', background='blue')
invoerStallenWachtwoord.pack(padx=20, pady=20)
RegistratieNummer = Label(master=StallenFrame, text='Voer hieronder uw registratienummer in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
RegistratieNummer.pack()
invoerRegistratienummer = Entry(master=StallenFrame, text='Voer hieronder uw registratienummer in!', background='blue')
invoerRegistratienummer.pack(padx=20, pady=20)
StallenDoorgaan = Button(master=StallenFrame, text='Doorgaan', height=3, width=14, font=('Helvetica', 10, 'bold'),background='blue',foreground='white', command=toonStallenOutput)
StallenDoorgaan.pack(padx=20, pady=20)

#StallenOutputFrame
StallenOutputFrame = Frame(master=root, background='yellow')
StallenOutputFrame.pack(fill="both", expand=True)

StallenOutputLabel = Label(master=StallenOutputFrame, text='Stallen', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
StallenOutputLabel.pack(padx=20, pady=20)
StallenOutputLabel1 = Label(master=StallenOutputFrame, text='Uw fiets staat nu gestalt!', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
StallenOutputLabel1.pack(padx=20, pady=200)

#StallenFoutFrame
StallenFoutFrame = Frame(master=root, background='yellow')
StallenLabel = Label(master=StallenFoutFrame, text='Stallingnummer bezet / Registratienummer niet bekend / Wachtwoord voldoet niet aan de eisen', background='yellow', foreground='red', width=100, height=1, font=('Helvetica', 15, 'bold'))
StallenLabel.pack(padx=20, pady=20)
StallingenVrij, StallingNummers = infoPubliek()
StallenLabelStallingenBezet = Label(master=StallenFoutFrame, text='Stallingen {} zijn bezet!'.format(StallingNummers), background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
StallenLabelStallingenBezet.pack(padx=20, pady=20)
NieuwStallingNummerLabel = Label(master=StallenFoutFrame, text='Voer hieronder uw toekomstige stallingnummer in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
NieuwStallingNummerLabel.pack()
invoerNieuwStallingNummer = Entry(master=StallenFoutFrame, text='Voer hier uw stallingnummer in!', background='blue')
invoerNieuwStallingNummer.pack(padx=20, pady=20)
WachtwoordLabel = Label(master=StallenFoutFrame, text='Voer hieronder een wachtwoord in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
WachtwoordLabel.pack()
invoerStallenWachtwoord = Entry(master=StallenFoutFrame, text='Voer hieronder een wachtwoord in!', background='blue')
invoerStallenWachtwoord.pack(padx=20, pady=20)
RegistratieNummer = Label(master=StallenFoutFrame, text='Voer hieronder uw registratienummer in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
RegistratieNummer.pack()
invoerRegistratienummer = Entry(master=StallenFoutFrame, text='Voer hieronder uw registratienummer in!', background='blue')
invoerRegistratienummer.pack(padx=20, pady=20)
StallenDoorgaan = Button(master=StallenFoutFrame, text='Doorgaan', height=3, width=14, font=('Helvetica', 10, 'bold'),background='blue',foreground='white', command=toonStallenOutput)
StallenDoorgaan.pack(side=TOP)
StallenFoutFrame.pack(fill="both", expand=True)


#Ophalen
OphalenFrame = Frame(master=root, background='yellow')
OphalenFrame.pack(fill="both", expand=True)
OphalenLabel = Label(master=OphalenFrame, text='Ophalen', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
OphalenLabel.pack(padx=20, pady=20)
OphalenRegistratienummerLabel = Label(master=OphalenFrame, text='Voer hieronder uw registratienummer in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
OphalenRegistratienummerLabel.pack()
OphalenRegistratienummer = Entry(master=OphalenFrame, background='blue')
OphalenRegistratienummer.pack(padx=20, pady=20)
OphalenWachtwoordLabel = Label(master=OphalenFrame, text='Voer hieronder uw wachtwoord in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
OphalenWachtwoordLabel.pack()
OphalenWachtwoord = Entry(master=OphalenFrame, background='blue')
OphalenWachtwoord.pack(padx=20, pady=20)
OphalenDoorgaan = Button(master=OphalenFrame, text='Doorgaan', height='3', width='14', background='blue', foreground='white', command=toonOphalenOutput)
OphalenDoorgaan.pack(padx=20, pady=20)

#OphalenOutputFrame
OphalenOutputFrame = Frame(master=root, background='yellow')
OphalenOutputFrame.pack(fill="both", expand=True)
OphalenOutputLabel = Label(master=OphalenOutputFrame, text='Ophalen', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
OphalenOutputLabel.pack(padx=20, pady=20)
OphalenOutputLabel = Label(master=OphalenOutputFrame, text='U kunt uw fiets ophalen!', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
OphalenOutputLabel.pack(padx=20, pady=20)

#OphalenFoutFrame
OphalenFoutFrame = Frame(master=root, background='yellow')
OphalenFoutFrame.pack(fill="both", expand=True)
OphalenFoutLabel = Label(master=OphalenFoutFrame, text='Registratienummer niet bekend / wachtwoord verkeerd!', background='yellow', foreground='red', width=50, height=1, font=('Helvetica', 15, 'bold'))
OphalenFoutLabel.pack(padx=20, pady=20)
OphalenFoutRegistratienummerLabel = Label(master=OphalenFoutFrame, text='Voer hieronder uw registratienummer in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
OphalenFoutRegistratienummerLabel.pack()
OphalenFoutRegistratienummer = Entry(master=OphalenFoutFrame, background='blue')
OphalenFoutRegistratienummer.pack(padx=20, pady=20)
OphalenFoutWachtwoordLabel = Label(master=OphalenFoutFrame, text='Voer hieronder uw wachtwoord in!', background='yellow', foreground='blue', width=100, height=2, font=('Helvetica', 15, 'bold'))
OphalenFoutWachtwoordLabel.pack()
OphalenFoutWachtwoord = Entry(master=OphalenFoutFrame, background='blue')
OphalenFoutWachtwoord.pack(padx=20, pady=20)
OphalenFoutDoorgaan = Button(master=OphalenFoutFrame, text='Doorgaan', height='3', width='14', background='blue', foreground='white', command=toonOphalenOutput)
OphalenFoutDoorgaan.pack(padx=20, pady=20)

#Informatie
InformatieFrame = Frame(master=root, background='yellow')
InformatieFrame.pack(fill="both", expand=True)
InformatieLabel = Label(master=InformatieFrame, text='Informatie', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
InformatieLabel.pack(padx=20, pady=20)
PubliekeInformatieButton = Button(master=InformatieFrame, text='Publieke Informatie', height=7, width=30, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatiePubliek)
PubliekeInformatieButton.pack(side=TOP)
PersoonlijkeInformatieButton = Button(master=InformatieFrame, text='Persoonlijke Informatie', height=7, width=30, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatiePersoonlijk)
PersoonlijkeInformatieButton.pack(side=TOP)


#Informatie Publiek
InformatiePubliekFrame = Frame(master=root, background='yellow')
InformatiePubliekFrame.pack
aantalStallingenVrij, stallingenVrij = infoPubliek()
InformatiePubliekLabel = Label(master=InformatiePubliekFrame, text='Informatie Publiek', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
InformatiePubliekLabel.pack(padx=20, pady=20)
InformatiePubliekLabel1 = Label(master=InformatiePubliekFrame, text='Er zijn in totaal {} stallingen vrij, stallingen {} zijn bezet'.format(100 - aantalStallingenVrij, stallingenVrij), background='yellow', foreground='blue', width=100, height=10, font=('Helvetica', 15, 'bold'))
InformatiePubliekLabel1.pack()
InformatiePersoonlijk = Frame(master=root, background='yellow')
InformatiePersoonlijk.pack


#Informatie Persoonlijk Output fout!
InformatiePersoonlijkFoutFrame = Frame(master=root, background='yellow')
InformatieFoutLabel = Label(master=InformatiePersoonlijkFoutFrame, text='Wachtwoord en/of Stalling is verkeerd ingevoerd!', background='yellow', foreground='red', width=50, height=1, font=('Helvetica', 15, 'bold'))
InformatieFoutLabel.pack(padx=50, pady=50)
invoerStallingLabel = Label(master=InformatiePersoonlijkFoutFrame, text='Voer hieronder uw Stalling nummer in:', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 15, 'bold'))
invoerStallingLabel.pack(padx=10, pady=0)
invoerStallingFout = Entry(master=InformatiePersoonlijkFoutFrame, background='blue')
invoerStallingFout.pack(padx=20, pady=20)
invoerWachtwoordLabel = Label(master=InformatiePersoonlijkFoutFrame, text='Voer hieronder uw Wachtwoord van uw stalling in:', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 15, 'bold'))
invoerWachtwoordLabel.pack(padx=10, pady=0)
invoerWachtwoordFout = Entry(master=InformatiePersoonlijkFoutFrame, background='blue')
invoerWachtwoordFout.pack(padx=20, pady=20)
InformatiePersoonlijkDoorgaan = Button(master=InformatiePersoonlijkFoutFrame, text='Doorgaan', height='3', width='14', background='blue', foreground='white', command=toonInformatiePersoonlijkOutput)
InformatiePersoonlijkDoorgaan.pack(padx=20, pady=20)
InformatiePersoonlijkFoutFrame.pack


#Informatie Persoonlijk output
InformatiePersoonlijkOutputFrame = Frame(master=root, background='yellow')
InformatieLabel = Label(master=InformatiePersoonlijkOutputFrame, text='Persoonlijke Informatie', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
InformatieLabel.pack(padx=20, pady=20)
InformatiePersoonlijkOutputLabel = Label(master=InformatiePersoonlijkOutputFrame, text='U kunt nu bij uw fiets!', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
InformatiePersoonlijkOutputLabel.pack(padx=20, pady=20)
InformatiePersoonlijkOutputFrame.pack


#Informatie Persoonlijk invoer
InformatiePersoonlijkFrame = Frame(master=root, background='yellow')
InformatieLabel = Label(master=InformatiePersoonlijkFrame, text='Persoonlijke Informatie', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 25, 'bold'))
InformatieLabel.pack(padx=20, pady=20)
invoerStallingLabel = Label(master=InformatiePersoonlijkFrame, text='Voer hieronder uw Stalling nummer in:', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 15, 'bold'))
invoerStallingLabel.pack(padx=10, pady=0)
invoerStalling = Entry(master=InformatiePersoonlijkFrame, background='blue')
invoerStalling.pack(padx=20, pady=20)
invoerWachtwoordLabel = Label(master=InformatiePersoonlijkFrame, text='Voer hieronder uw Wachtwoord van uw stalling in::', background='yellow', foreground='blue', width=50, height=1, font=('Helvetica', 15, 'bold'))
invoerWachtwoordLabel.pack(padx=10, pady=0)
invoerWachtwoord = Entry(master=InformatiePersoonlijkFrame, background='blue')
invoerWachtwoord.pack(padx=20, pady=20)
InformatiePersoonlijkDoorgaan = Button(master=InformatiePersoonlijkFrame, text='Doorgaan', height=3, width=14, background='blue', foreground='white', command=toonInformatiePersoonlijkOutput)
InformatiePersoonlijkDoorgaan.pack(padx=20, pady=20)
InformatiePersoonlijkFrame.pack


toonHome()
root.mainloop()